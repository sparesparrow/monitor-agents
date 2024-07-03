# terminal_commands_service/TerminalCommandsService.py

import os
import time
from event_manager.EventManager import EventManager

class TerminalCommandsService:
    def __init__(self, event_manager):
        self.event_manager = event_manager

    def monitor_terminal_commands(self):
        last_line = ""
        while True:
            with os.popen('history') as f:
                lines = f.readlines()
                if lines and lines[-1] != last_line:
                    self.event_manager.add_event("terminal_command_executed", lines[-1])
                    last_line = lines[-1]
            time.sleep(1)

if __name__ == "__main__":
    event_manager = EventManager()
    terminal_service = TerminalCommandsService(event_manager)
    terminal_service.monitor_terminal_commands()
