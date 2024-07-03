# tests/test_screenshot_service.py

import unittest
from screenshot_service.ScreenshotService import ScreenshotService
from event_manager.EventManager import EventManager

class TestScreenshotService(unittest.TestCase):
    def setUp(self):
        self.event_manager = EventManager()
        self.screenshot_service = ScreenshotService(self.event_manager, interval=1)

    def test_take_screenshot(self):
        self.screenshot_service.take_screenshot()
        # Add assertions to check if screenshot is taken and saved

    def test_start_periodic_screenshots(self):
        # This test would need to run in a separate thread or mock time.sleep
        pass

if __name__ == "__main__":
    unittest.main()
