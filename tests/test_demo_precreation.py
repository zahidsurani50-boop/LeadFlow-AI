import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import app


class DemoPrecreationTests(unittest.TestCase):

    def test_rejected_session_creates_no_database(self):
        with tempfile.TemporaryDirectory() as temp:
            session_dir = Path(temp) / "sessions"

            with patch.object(app, "SESSION_DIR", session_dir), \
                 patch.object(app, "SESSION_SECRET", "test-secret"), \
                 patch.object(
                     app,
                     "demo_new_session_allowed",
                     return_value=False
                 ) as limiter:

                with self.assertRaises(PermissionError):
                    app.prepare_demo_session(
                        "",
                        client_key="test-visitor"
                    )

                limiter.assert_called_once_with("test-visitor")

                databases = list(session_dir.glob("*.db"))
                self.assertEqual(databases, [])


if __name__ == "__main__":
    unittest.main()
