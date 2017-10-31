from io import RawIOBase
import os, re, wave, pyaudio

chunk = 1024

filelocation = "C:\\Users\Dascham\Desktop\\paris2.wav"

file = wave.open(filelocation, mode="rb")

print(file.getframerate())

p = pyaudio.PyAudio()

stream = p.open(format=(p.get_format_from_width(file.getsampwidth())),
                channels = file.getnchannels(),
                rate = file.getframerate(),
                output = True)

data = file.readframes(chunk)
a = 0
while a < 50:
    stream.write(data)
    data = file.readframes(chunk)
    a = a + 1


stream.stop_stream()
stream.close()

p.terminate()

file.close()
