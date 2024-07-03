# clipboard_history_service/ClipboardHistoryService.py

import pyperclip
import time
from event_manager.EventManager import EventManager

class ClipboardHistoryService:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.last_clipboard = ""

    def monitor_clipboard(self):
        while True:
            current_clipboard = pyperclip.paste()
            if current_clipboard != self.last_clipboard:
                self.event_manager.add_event("clipboard_updated", current_clipboard)
                self.last_clipboard = current_clipboard
            time.sleep(1)

if __name__ == "__main__":
    event_manager = EventManager()
    clipboard_service = ClipboardHistoryService(event_manager)
    clipboard_service.monitor_clipboard()
