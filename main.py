import speech_recognition as sr
import webbrowser
import pyttsx3 
import musicLibrary
from client import ask_gemini
import sys

recognizer =sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open anime" in c.lower():
        webbrowser.open("https://hianime.sx/home")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "stop" in c.lower():
        speak("Shutting down. Goodbye!")
        sys.exit()    
    else:
         response = ask_gemini(c)
         print("Gemini:", response)
        #  speak(response)


if __name__=="__main__":
    speak("intializing friday......")   
    while True:
        mode = input("👉 Type 'voice' for voice mode or type your command directly: ").strip().lower()
        r= sr.Recognizer()
        if mode == "voice":   
            try:
                with sr.Microphone() as source :
                    print("listening....")
                    recognizer.energy_threshold = 300  # Adjust based on mic quality
                    recognizer.pause_threshold = 0.7
                    audio = r.listen(source, timeout=3,phrase_time_limit=3)
                    word = r.recognize_google(audio)
                    # print(command) 
                    if (word.lower()== "friday"):
                        speak("yes sir im listening")
                        with sr.Microphone() as source :
                            print("friday Active....")
                            audio = r.listen(source)
                            command = r.recognize_google(audio)

                            processCommand(command)
                
            except Exception as e:
                print(e)
           