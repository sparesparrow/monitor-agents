# file_changes_service/FileChangesService.py

import os
import time
from event_manager.EventManager import EventManager

class FileChangesService:
    def __init__(self, event_manager, directory_to_watch):
        self.event_manager = event_manager
        self.directory_to_watch = directory_to_watch
        self.files_snapshot = self.snapshot_directory()

    def snapshot_directory(self):
        snapshot = {}
        for root, dirs, files in os.walk(self.directory_to_watch):
            for file in files:
                path = os.path.join(root, file)
                snapshot[path] = os.stat(path).st_mtime
        return snapshot

    def monitor_file_changes(self):
        while True:
            new_snapshot = self.snapshot_directory()
            changes = {path: mtime for path, mtime in new_snapshot.items() if path not in self.files_snapshot or self.files_snapshot[path] != mtime}
            if changes:
                self.event_manager.add_event("file_changes_detected", changes)
                self.files_snapshot = new_snapshot
            time.sleep(60)

if __name__ == "__main__":
    event_manager = EventManager()
    file_service = FileChangesService(event_manager, "/path/to/watch")
    file_service.monitor_file_changes()
