from pyttsx3 import init
from speech_recognition import Recognizer,Microphone
from webbrowser import open
import wikipedia
from datetime import date,datetime

# pip install pyttsx3 speech_recognition,wikipedia

''' speaking methord'''
def speak(output):
    engine =init()
    engine.setProperty('rate',120)
    engine.say(output)
    engine.runAndWait()


''' listing methord'''
def listen():
    while True:
        r = Recognizer()
        r.energy_threshold =300
        with Microphone() as source:
            r.adjust_for_ambient_noise(source, duration = 1)
            audio =r.listen(source)
            speak("sir plaese say ")  
            try:
                input =r.recognize_google(audio)
                check(input)
               
            except:
                speak("sir plaese repeat")          
            


''' Check methord'''
def check(input):
    input =input.lower()
    if 'date' in input:
        today = date.today()
        speak("Today's date:", today)
        return
    if 'time' in input:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak("Current Time =", current_time) 
        return
    if 'open google' in input:
        speak("open google")
        open("www.google.com")
        return
    if 'wikipedia' in input:
        speak("Serching sir...")
        input =input.replace("wikipedia","")
        result =wikipedia.summary(input,sentences =2)
        speak(result)
        return    

    if 'open facebook' in input:
        speak("open facebook")
        open("www.facebook.com")
        return
     
        
    if 'open youtube' in input:
        speak("What you  want on youtube")
        open(f"www.youtube.com")
        return
        
    if 'open stackoverflow' in input:
        speak("open stackoverflow")
        open("www.stackoverflow.com")
        return
        
    if 'open instagram' in input:
        speak("open instagram")
        open("www.instagram.com")
        return
        
    if 'open gmail' in input:
        speak("open gmail")
        open("www.gmail.com")
        return
          
    else:
        speak("Sorry sir i don't do this")  

if __name__ == "__main__":
    listen()

  


