# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 00:30:03 2020

@author: PRIYAHEMA PC
"""

import speech_recognition as sr

noise = sr.AudioFile("jackhammer.wav")
r = sr.Recognizer()
with noise as source:
    #in-bult function to help reduce noise effect
    #this method reads the 1st second of the file stream and calibrates the recognizer to the noise level of the 
    r.adjust_for_ambient_noise(source,duration=0.5)
    #You can adjust the time-frame that the method uses for analysis with the duration keyword argument. 
    #This argument takes a numerical value in seconds and is set to 1 by default. 
    audio = r.record(source)
print(r.recognize_google(audio))
#prints something random and your original speech is lost due to noise
print(r.recognize_google(audio, show_all=True))

'''
Most APIs return a JSON string containing many possible transcriptions. 
The recognize_google() method will always return the most likely transcription unless 
you force it to give you the full response.
You can do this by setting the show_all keyword argument of the recognize_google() 
method to True.
'''