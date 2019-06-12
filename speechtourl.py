#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
import webbrowser as wb



chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Record Audio
r = sr.Recognizer()


with sr.Microphone() as source:
    
    print("Say something!")
    audio = r.listen(source)             
    print("Done!")
   
    
try:
    text = r.recognize_google(audio)
    print("You said: " + text)
    
    url = 'http://'+text.replace(" ", "/")
    print(url)
    wb.get(chrome_path).open(url)
    
except Exception as e:
    print(e)
