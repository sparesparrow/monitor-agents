# tests/test_data_aggregation_service.py

import unittest
from data_aggregation_service.DataAggregationService import DataAggregationService
from event_manager.EventManager import EventManager

class TestDataAggregationService(unittest.TestCase):
    def setUp(self):
        self.event_manager = EventManager()
        self.aggregation_service = DataAggregationService(self.event_manager)

    def test_aggregate_data(self):
        self.aggregation_service.aggregate_data({"test_key": "test_value"})
        self.assertIn("test_key", self.aggregation_service.collected_data)

    def test_create_assistant_prompt(self):
        self.aggregation_service.collected_data = {"test_key": "test_value"}
        self.aggregation_service.create_assistant_prompt()
        # Add assertions to check if prompt is created correctly

if __name__ == "__main__":
    unittest.main()
