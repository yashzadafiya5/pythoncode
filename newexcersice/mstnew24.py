# 24. Voice Recorder using Python 

# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
  
# Sampling frequency
freq = 44100
  
# Recording duration
duration = 12

recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

sd.wait()

write("recording0.wav", freq, recording)
  

wv.write("recording1.wav", recording, freq, sampwidth=2)
