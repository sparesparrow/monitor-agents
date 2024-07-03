# audio_recording_service/AudioRecordingService.py

import pyaudio
import wave
import time
import openai
from event_manager.EventManager import EventManager

class AudioRecordingService:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.chunk = 1024
        self.sample_format = pyaudio.paInt16
        self.channels = 2
        self.rate = 44100
        self.record_seconds = 10
        self.audio = pyaudio.PyAudio()

    def record_audio(self):
        stream = self.audio.open(format=self.sample_format,
                                 channels=self.channels,
                                 rate=self.rate,
                                 frames_per_buffer=self.chunk,
                                 input=True)
        frames = []
        for _ in range(0, int(self.rate / self.chunk * self.record_seconds)):
            data = stream.read(self.chunk)
            frames.append(data)
        stream.stop_stream()
        stream.close()
        wf = wave.open("audio.wav", 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio.get_sample_size(self.sample_format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        self.event_manager.add_event("audio_recorded", "audio.wav")

    def transcribe_audio(self, audio_file):
        with open(audio_file, "rb") as f:
            transcription = openai.Audio.transcribe("whisper-1", f)
        self.event_manager.add_event("audio_transcribed", transcription)

    def start_periodic_recording(self):
        while True:
            self.record_audio()
            self.transcribe_audio("audio.wav")
            time.sleep(60)

if __name__ == "__main__":
    event_manager = EventManager()
    audio_service = AudioRecordingService(event_manager)
    threading.Thread(target=audio_service.start_periodic_recording).start()
