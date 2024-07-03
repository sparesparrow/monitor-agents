# tests/test_terminal_commands_service.py

import unittest
from terminal_commands_service.TerminalCommandsService import TerminalCommandsService
from event_manager.EventManager import EventManager

class TestTerminalCommandsService(unittest.TestCase):
    def setUp(self):
        self.event_manager = EventManager()
        self.terminal_service = TerminalCommandsService(self.event_manager)

    def test_monitor_terminal_commands(self):
        # This test would need to mock os.popen and time.sleep
        pass

if __name__ == "__main__":
    unittest.main()
