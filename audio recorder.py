import sounddevice
import wavio


print("Welcome to the audio recorder!")
sample_rate = 192000
duration = int(input("Enter duration of audio in seconds: ")) 
if duration < 1:
    print("Duration must be at least 1 second")
    exit()

print("Recording...")
recording = sounddevice.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1)
sounddevice.wait()

file_name = input("Enter file name to save the audio:")
wav_file = file_name +".wav"
wavio.write(wav_file, recording, sample_rate, sampwidth=4)

print(f"Recording saved to {wav_file}")