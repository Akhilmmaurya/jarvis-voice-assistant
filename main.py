import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary


recognizer = sr.Recognizer()
# engine = pyttsx3.init("sapi5")
# engine.setProperty('rate', 150)
# engine.setProperty('volume', 1.0)

def speak(text):
    print(text)
    engine = pyttsx3.init("sapi5")
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
            webbrowser.open("https://youtube.com")

    elif "open linkedin" in c.lower():
            webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
         song = c.lower().replace("play ", "").strip()
         if song in musiclibrary.music:
              webbrowser.open(musiclibrary.music[song])
         else:
              speak(f"Sorry, I don't have the song {song} in my library.")
        #  link = musiclibrary.music[song]
        #  webbrowser.open(link)

    elif "open gemini" in c.lower():
        webbrowser.open("https://gemini.google.com")

    else:
         speak(f"Sorry, I did not understand that command")
       

if __name__ == "__main__":
    speak("Initializing Jarvis........")




    while True:
        #Listen for the wake word jarvis
        #obtain audio from the microphone


        r = sr.Recognizer()
        print("Recognizing...")


        try:
            with sr.Microphone() as source:
                 print("Listening...")
                 audio = r.listen(source, timeout=3, phrase_time_limit=2)

            word = r.recognize_google(audio)
            if ("jarvis" in word.lower()):
                speak("Yes sir")
                #listen for the command

                with sr.Microphone() as source:
                    print("jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("error; {0}".format(e))    


