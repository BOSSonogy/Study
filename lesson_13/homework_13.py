
import unittest
import logging


def log_event(username: str, status: str):

    log_message = f"Login event - Username: {username}, Status: {status}"

    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
        )

    logger = logging.getLogger("log_event")

    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)



class TestLogin(unittest.TestCase):
    def test_success(self):
        with self.assertLogs('log_event', level='INFO'):
            log_event('Bob', 'success')

    def test_expired(self):
        actual = log_event('Nick', 'expired')
        self.assertIsNone(actual)

    def test_error(self):
        with self.assertLogs('log_event', level='ERROR') as log:
            log_event('Mike', 'failed')
        self.assertTrue(log.output[0].startswith('ERROR'))