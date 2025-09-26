import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open gmail" in c.lower():
        webbrowser.open("https://gmail.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = (musicLibrary.music[song])
        webbrowser.open(link)

    else:
        pass

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('luna.mp3')
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the music
    pygame.mixer.music.load('luna.mp3')

    # Play the music
    pygame.mixer.music.play()

    # Keep program running so music can play
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.unload()
    os.remove("luna.mp3")

if __name__ == "__main__":
    speak("Initializing Luna....")
    while True:
        # Listen for the wake word "Luna"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if(word.lower() == "luna"):
                speak("Hai")
                #listen for luna
                with sr.Microphone() as source:
                  print("Listening...")
                  audio = r.listen(source, timeout=5, phrase_time_limit=5)
                  command = r.recognize_google(audio)
                  processcommand(command)
        
        except sr.UnknownValueError:
            print("Didn't catch that.")
        except sr.RequestError as e:
            print(f"API unavailable; {e}")
        except Exception as e:
            print(f"Error: {e}")
            