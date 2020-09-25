import unittest
import datetime
from unittest.mock import patch
from clock_alarm import clock_alarm

class TestClockAlarm(unittest.TestCase):

    def setUp(self):
        self.tuesday = datetime.datetime(year=2020, month=1, day=1)
        self.saturday = datetime.datetime(year=2020, month=1, day=5)

    @patch('datetime.datetime')
    def test_is_weekday(self, mock_datetime):
        mock_datetime.today.return_value = self.tuesday
        self.assertTrue(clock_alarm.is_weekday())
        mock_datetime.today.return_value = self.saturday
        self.assertFalse(clock_alarm.is_weekday())

    

if __name__ == '__main__':
    unittest.main()
