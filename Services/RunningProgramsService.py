# running_programs_service/RunningProgramsService.py

import psutil
import time
from event_manager.EventManager import EventManager

class RunningProgramsService:
    def __init__(self, event_manager):
        self.event_manager = event_manager

    def monitor_running_programs(self):
        while True:
            running_programs = [p.info for p in psutil.process_iter(['pid', 'name'])]
            self.event_manager.add_event("running_programs_updated", running_programs)
            time.sleep(60)

if __name__ == "__main__":
    event_manager = EventManager()
    programs_service = RunningProgramsService(event_manager)
    programs_service.monitor_running_programs()
