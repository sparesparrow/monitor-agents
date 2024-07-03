# tests/test_audio_recording_service.py

import unittest
from audio_recording_service.AudioRecordingService import AudioRecordingService
from event_manager.EventManager import EventManager

class TestAudioRecordingService(unittest.TestCase):
    def setUp(self):
        self.event_manager = EventManager()
        self.audio_service = AudioRecordingService(self.event_manager)

    def test_record_audio(self):
        self.audio_service.record_audio()
        # Add assertions to check if audio is recorded and saved

    def test_transcribe_audio(self):
        # This test would need to mock openai.Audio.transcribe
        pass

if __name__ == "__main__":
    unittest.main()
