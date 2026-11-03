import unittest
from unittest.mock import patch

import app


class DemoRateLimitTests(unittest.TestCase):

    def setUp(self):
        with app._rate_lock:
            app._rate_requests.clear()

    def tearDown(self):
        with app._rate_lock:
            app._rate_requests.clear()

    def test_requests_within_limit(self):
        with patch.object(app, 'RATE_LIMIT_MAX', 3):
            with patch('app.time.monotonic', return_value=100.0):
                self.assertTrue(app.demo_rate_allowed('visitor-a'))
                self.assertTrue(app.demo_rate_allowed('visitor-a'))
                self.assertTrue(app.demo_rate_allowed('visitor-a'))

    def test_limit_and_window_reset(self):
        with patch.object(app, 'RATE_LIMIT_MAX', 2):
            with patch('app.time.monotonic', return_value=100.0):
                self.assertTrue(app.demo_rate_allowed('visitor-a'))
                self.assertTrue(app.demo_rate_allowed('visitor-a'))
                self.assertFalse(app.demo_rate_allowed('visitor-a'))

                # Another visitor has a separate allowance.
                self.assertTrue(app.demo_rate_allowed('visitor-b'))

            with patch('app.time.monotonic', return_value=161.0):
                self.assertTrue(app.demo_rate_allowed('visitor-a'))


if __name__ == '__main__':
    unittest.main()
