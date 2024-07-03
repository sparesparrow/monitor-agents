# system_logs_service/SystemLogsService.py

import subprocess
import time
from event_manager.EventManager import EventManager

class SystemLogsService:
    def __init__(self, event_manager):
        self.event_manager = event_manager

    def monitor_system_logs(self):
        last_logs = ""
        while True:
            logs = subprocess.check_output(['dmesg']).decode('utf-8')
            if logs != last_logs:
                self.event_manager.add_event("system_logs_updated", logs)
                last_logs = logs
            time.sleep(60)

if __name__ == "__main__":
    event_manager = EventManager()
    logs_service = SystemLogsService(event_manager)
    logs_service.monitor_system_logs()
