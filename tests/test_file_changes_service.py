# tests/test_file_changes_service.py

import unittest
from file_changes_service.FileChangesService import FileChangesService
from event_manager.EventManager import EventManager

class TestFileChangesService(unittest.TestCase):
    def setUp(self):
        self.event_manager = EventManager()
        self.file_service = FileChangesService(self.event_manager, "/path/to/watch")

    def test_snapshot_directory(self):
        snapshot = self.file_service.snapshot_directory()
        # Add assertions to check if snapshot is created correctly

    def test_monitor_file_changes(self):
        # This test would need to mock os.walk, os.stat, and time.sleep
        pass

if __name__ == "__main__":
    unittest.main()
