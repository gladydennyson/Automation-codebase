import speech_recognition as sr

import pyaudio
import os
import webbrowser

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
    
 
try:
    
    print('You said:\n' + r.recognize_google(audio))

    if(r.find("Sum")!=-1):
       os.system("start C:\\Users\\admin\\Desktop\\Voice-Act\\test-calculating-sum-2.py")
               
        
except:
    pass
