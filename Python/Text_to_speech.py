"""import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, world!")
engine.runAndWait()"""

from gtts import gTTS
import os

# Creating text to speech object
tts = gTTS(text="Hello ", lang='en')

# Save the audio file
tts.save('ttsout.mp3')

# Play the audio file
os.system('afplay ttsout.mp3')


