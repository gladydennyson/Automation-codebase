import speech_recognition as sr

import pyaudio

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
    
 
try:
    
    print('You said:\n' + r.recognize_google(audio))
        
except:
    pass
