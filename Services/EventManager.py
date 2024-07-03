# event_manager/EventManager.py

import threading
import queue

class EventManager:
    def __init__(self):
        self.event_queue = queue.Queue()
        self.subscribers = {}

    def publish_event(self, event_type, event_data):
        if event_type in self.subscribers:
            for subscriber in self.subscribers[event_type]:
                subscriber(event_data)

    def subscribe_to_event(self, event_type, callback):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    def run(self):
        while True:
            event_type, event_data = self.event_queue.get()
            self.publish_event(event_type, event_data)

    def add_event(self, event_type, event_data):
        self.event_queue.put((event_type, event_data))

if __name__ == "__main__":
    event_manager = EventManager()
    threading.Thread(target=event_manager.run).start()
