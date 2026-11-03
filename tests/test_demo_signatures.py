import unittest
from unittest.mock import patch

import app


class DemoSignatureTests(unittest.TestCase):

    def test_valid_signed_cookie(self):
        with patch.object(app, 'SESSION_SECRET', 'test-only-secret'):
            session_id = app.new_demo_session_id()
            signed = app.sign_demo_session(session_id)

            self.assertEqual(
                app.verify_demo_session(signed),
                session_id
            )

    def test_forged_cookie_rejected(self):
        with patch.object(app, 'SESSION_SECRET', 'test-only-secret'):
            session_id = app.new_demo_session_id()

            self.assertIsNone(
                app.verify_demo_session(session_id)
            )

            signed = app.sign_demo_session(session_id)
            tampered = signed[:-1] + (
                '0' if signed[-1] != '0' else '1'
            )

            self.assertIsNone(
                app.verify_demo_session(tampered)
            )

    def test_wrong_secret_rejected(self):
        session_id = app.new_demo_session_id()

        with patch.object(app, 'SESSION_SECRET', 'first-secret'):
            signed = app.sign_demo_session(session_id)

        with patch.object(app, 'SESSION_SECRET', 'second-secret'):
            self.assertIsNone(
                app.verify_demo_session(signed)
            )


if __name__ == '__main__':
    unittest.main()
