# data_aggregation_service/DataAggregationService.py

import json
from event_manager.EventManager import EventManager

class DataAggregationService:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.collected_data = {}

    def aggregate_data(self, event_data):
        self.collected_data.update(event_data)
        self.event_manager.add_event("data_aggregated", self.collected_data)

    def create_assistant_prompt(self):
        prompt = json.dumps(self.collected_data)
        self.event_manager.add_event("assistant_prompt_created", prompt)

if __name__ == "__main__":
    event_manager = EventManager()
    aggregation_service = DataAggregationService(event_manager)
    aggregation_service.aggregate_data({"initial": "data"})
    aggregation_service.create_assistant_prompt()
