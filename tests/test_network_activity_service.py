# tests/test_network_activity_service.py

import unittest
from network_activity_service.NetworkActivityService import NetworkActivityService
from event_manager.EventManager import EventManager

class TestNetworkActivityService(unittest.TestCase):
    def setUp(self):
        self.event_manager = EventManager()
        self.network_service = NetworkActivityService(self.event_manager)

    def test_monitor_network_activity(self):
        # This test would need to mock subprocess.check_output and time.sleep
        pass

if __name__ == "__main__":
    unittest.main()
