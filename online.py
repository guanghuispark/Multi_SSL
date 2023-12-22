import pyaudio
import wave
import time
import sounddevice as sd

frames = []
CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 20
WAVE_OUTPUT_FILENAME = "output.wav"
def callback(in_data, frame_count, time_info, status):
    frames.append(in_data)
    return (None, pyaudio.paContinue)

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))
# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK,
#                 stream_callback=callback)

# stream.start_stream()
# time.sleep(RECORD_SECONDS)
# stream.stop_stream()
# stream.close()
# p.terminate()

# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()
# print('\n\n\n')

# def is_palying_music():
#     devices = sd.query_devices()
#     for device in devices:
#         print(device)

# is_palying_music()