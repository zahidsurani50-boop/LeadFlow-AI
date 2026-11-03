import os
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch

import app


class DemoSessionTests(unittest.TestCase):

    def test_session_ids_are_unique(self):
        first = app.new_demo_session_id()
        second = app.new_demo_session_id()
        self.assertNotEqual(first, second)
        self.assertTrue(app.valid_demo_session_id(first))
        self.assertTrue(app.valid_demo_session_id(second))

    def test_invalid_session_ids_rejected(self):
        for value in ('', '../private', 'abc', 'z' * 48):
            self.assertFalse(app.valid_demo_session_id(value))
            with self.assertRaises(ValueError):
                app.demo_session_path(value)

    def test_visitors_have_separate_databases(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(app, 'SESSION_DIR', Path(folder)):
                first, first_db = app.prepare_demo_session('')
                second, second_db = app.prepare_demo_session('')

                self.assertNotEqual(first, second)
                self.assertNotEqual(first_db, second_db)

                with app.dbconnect(first_db) as db:
                    db.execute(
                        "INSERT INTO leads (name, company, need) "
                        "VALUES (?, ?, ?)",
                        ('Visitor A', 'Test Company', 'Test need')
                    )

                self.assertEqual(len(app.list_leads(first_db)), 1)
                self.assertEqual(len(app.list_leads(second_db)), 0)

    def test_expired_session_gets_replaced(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(app, 'SESSION_DIR', Path(folder)):
                session_id, db_path = app.prepare_demo_session('')

                old_time = time.time() - app.SESSION_TTL - 10
                os.utime(db_path, (old_time, old_time))

                cookie = (
                    app.SESSION_COOKIE + '=' + session_id
                )

                new_id, new_path = app.prepare_demo_session(cookie)

                self.assertNotEqual(session_id, new_id)
                self.assertNotEqual(db_path, new_path)


if __name__ == '__main__':
    unittest.main()
