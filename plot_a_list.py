##ffmpeg -i resto.mp3 -vn -acodec pcm_s16le -ac 1 -ar 44100 -f wav resto.wav                                                                                                     
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt

samplerate, data = scipy.io.wavfile.read("test.wav")

## Esempio cerco pezzi con 3 secondi di silenzio.                                                                                                                                
sec = 3
sec_= int(sec*samplerate)
silence = np.zeros(sec_)
#test = [0, 0, 1, 1, 2, 0, 0, 0, 0, 1, 2, 3]                                                                                                                                     
print(data)

fig, ax = plt.subplots()
plt.plot(data)
fig.savefig("test.png")
