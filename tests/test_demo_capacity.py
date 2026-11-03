import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import app


class DemoCapacityTests(unittest.TestCase):

    def test_session_capacity_limit(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(app, 'SESSION_SECRET', 'test-only-secret'):
                with patch.object(app, 'SESSION_DIR', Path(folder)), patch.object(app, 'MAX_DEMO_SESSIONS', 2):
                    first, _ = app.prepare_demo_session('')
                    second, _ = app.prepare_demo_session('')

                    self.assertNotEqual(first, second)

                    with self.assertRaisesRegex(
                        RuntimeError, 'temporarily at capacity'
                    ):
                        app.prepare_demo_session('')

                    # Existing visitors must still have access.
                    existing, _ = app.prepare_demo_session(
                        app.SESSION_COOKIE + '=' + app.sign_demo_session(first)
                    )
                    self.assertEqual(existing, first)


if __name__ == '__main__':
    unittest.main()
