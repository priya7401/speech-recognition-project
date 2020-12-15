# -*- coding: utf-8 -*-

import speech_recognition as sr

#creating a sample of the audio file; i.e., giving the audio file input
#The AudioFile class of SpeechRecognition provides a context manager interface for reading and working with the file's contents.
sample = sr.AudioFile('Ae Dil Hai Mushkil.wav')

#initialize the recognizer
#recognizer is a class of speechrecognition module used to convert speech to text
#REcognizer class contains almost everything required to work with basic speech recognition modules
#Its like a class containing various functions required to perform various tasks
r = sr.Recognizer()

#reads the audio file; to convert the audio FILE to an OBJECT
#we use record method from the recognizer class
#record() method records the data from the entire file into an AudioData instance
#AudioData is the waveform of the original audio input
#Vaguely speaking, the record() method converts the audio into a graph that contains the waveform output of the audio

with sample as source:
    audio_file = r.record(source,duration=58,offset=20)
    #offset->from time, duration->to time of the audio file,i.e., the audio between these seconds will be recorded.
    #print(type(audio_file)) will give output as: <class 'speech_recognition.AudioData'>

try:
    #recognize_google() method recognizes the speech in the audio
    print("The audio file contains: " + r.recognize_google(audio_file))

#There is a limit of 10 MB,i.e.,1min approx on all single requests sent to the API using local files.
except sr.RequestError:
    print("API is unavailable")

except sr.UnknownValueError:
    print("Google Sppech Recognition couldn't understand the audio, retry by giving clear audio input")
    

