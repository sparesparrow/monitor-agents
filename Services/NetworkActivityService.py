# network_activity_service/NetworkActivityService.py

import subprocess
import time
from event_manager.EventManager import EventManager

class NetworkActivityService:
    def __init__(self, event_manager):
        self.event_manager = event_manager

    def monitor_network_activity(self):
        while True:
            activity = subprocess.check_output(['tcpdump', '-i', 'any', '-n', 'port', '80', 'or', 'port', '443', '-c', '10']).decode('utf-8')
            self.event_manager.add_event("network_activity_detected", activity)
            time.sleep(60)

if __name__ == "__main__":
    event_manager = EventManager()
    network_service = NetworkActivityService(event_manager)
    network_service.monitor_network_activity()
