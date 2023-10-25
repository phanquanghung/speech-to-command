import pyaudio
import wave

def rec(file_path):
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024, input_device_index=4)

    frames = []

    # record for 5 seconds
    print("Recording...")

    for i in range(0, int(44100 / 1024 * 3)):
        data = stream.read(1024)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Finished recording.")

    sound_file = wave.open(file_path,"wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()

    print("Saved audio to", file_path)