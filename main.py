# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 20:13:37 2020

@author: PRIYAHEMA PC
"""
import speech_recognition as sr

def audio_input() :
    r = sr.Recognizer()
    print("Make sure that the input audio file is included in the same file as that of the application or enter the path of the file\n")
    file = input("Enter the .wav audio file name ")
    sample = sr.AudioFile(file)
    with sample as source :
        r.adjust_for_ambient_noise(source)
        audio_file = r.record(source,duration=81,offset=23)        
    try :
        print("The audio file contains: " + r.recognize_google(audio_file))
        print()
    except sr.RequestError:
        print("API is unavailable\n")
    except sr.UnknownValueError:
        print("Google Sppech Recognition couldn't understand the audio, retry by giving clear audio input\n")
    return 

def mic_input() :
    r = sr.Recognizer() 
    choice = int(input("Press 1 if you are using default microphone(recommended) in the device or else press 2\n"))
    while(1) :
        if(choice==1) :
            print("You may speak now\n")
            mic = sr.Microphone()   #default system microphone
            with mic as source :
                r.adjust_for_ambient_noise(source,duration=0.5)
                audio = r.listen(source)
            try:
                print(r.recognize_google(audio))
            except sr.RequestError:
                print("API is unavailable\n")
            except sr.UnknownValueError:
                print("Google Sppech Recognition couldn't understand the audio, retry by giving clear audio input\n")
            break
        if choice==2 :
            print(sr.Microphone().list_microphone_names())
            input_no = int(input("Enter the number of the device from the list that you are using as microphone\n"))
            mic = sr.Microphone(device_index=input_no-1)   #default system microphone
            print("You may speak now\n")
            with mic as source :
                r.adjust_for_ambient_noise(source,duration=0.5)
                audio = r.listen(source)
            try:
                print(r.recognize_google(audio))
            except sr.RequestError:
                print("API is unavailable\n")
            except sr.UnknownValueError:
                print("Google Sppech Recognition couldn't understand the audio, retry by giving clear audio input\n")
            break
        return

choice = int(input("What do you want the speech recognition application to do?\n Select the follwing options:\n 1.Giving audio file input and getting the output in text form\n 2.Giving input via microphone\n 3. Quit\n"))

while 1 :
    if choice==1 :
        audio_input()
    if choice==2 :
        mic_input()
    if choice==3 :
        print("Thank you for using speech recognition application!")
        break
