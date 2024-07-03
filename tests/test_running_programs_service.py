# tests/test_running_programs_service.py

import unittest
from running_programs_service.RunningProgramsService import RunningProgramsService
from event_manager.EventManager import EventManager

class TestRunningProgramsService(unittest.TestCase):
    def setUp(self):
        self.event_manager = EventManager()
        self.programs_service = RunningProgramsService(self.event_manager)

    def test_monitor_running_programs(self):
        # This test would need to mock psutil.process_iter and time.sleep
        pass

if __name__ == "__main__":
    unittest.main()
