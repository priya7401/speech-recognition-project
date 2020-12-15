# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:00:48 2020

@author: PRIYAHEMA PC
"""

import speech_recognition as sr
 
r = sr.Recognizer()
#using the system's default microphone as the source instead of an audio file
#Microphone() is a class in speech_recognition module that helps process audio from microphone
#mic = sr.Microphone() -> default system microphone
#inorder to use someother source connected to the system as microphone, 
#call sr.Microphone().list_microphone_names() to get a list of microphone names and use them
#note down the index of the device being used and pass the value in the Microphone() function

mic = sr.Microphone(device_index=1)

#Just like the AudioFile class, Microphone is a context manager. 
#You can capture input from the microphone using the listen() method of the 
#Recognizer class inside of the with block. This method takes an audio source 
#as its first argument and records input from the source until silence is detected.

with mic as source:
    r.adjust_for_ambient_noise(source,duration=0.5)
    audio = r.listen(source)

#Calling the recognizer of google as usual to get the text output
try:
    print(r.recognize_google(audio))

except sr.RequestError:
    print("API is unavailable")

except sr.UnknownValueError:
    print("Google Sppech Recognition couldn't understand the audio, retry by giving clear audio input")