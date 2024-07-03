# screenshot_service/ScreenshotService.py

import pyautogui
import time
import threading
from event_manager.EventManager import EventManager

class ScreenshotService:
    def __init__(self, event_manager, interval=60):
        self.event_manager = event_manager
        self.interval = interval

    def take_screenshot(self):
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        self.event_manager.add_event("screenshot_taken", "screenshot.png")

    def start_periodic_screenshots(self):
        while True:
            self.take_screenshot()
            time.sleep(self.interval)

if __name__ == "__main__":
    event_manager = EventManager()
    screenshot_service = ScreenshotService(event_manager)
    threading.Thread(target=screenshot_service.start_periodic_screenshots).start()
