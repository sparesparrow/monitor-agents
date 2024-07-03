# socket_monitoring_service/SocketMonitoringService.py

import subprocess
import time
from event_manager.EventManager import EventManager

class SocketMonitoringService:
    def __init__(self, event_manager):
        self.event_manager = event_manager

    def monitor_sockets(self):
        while True:
            sockets = subprocess.check_output(['netstat', '-tunlp']).decode('utf-8')
            self.event_manager.add_event("socket_activity_detected", sockets)
            time.sleep(60)

if __name__ == "__main__":
    event_manager = EventManager()
    socket_service = SocketMonitoringService(event_manager)
    socket_service.monitor_sockets()
