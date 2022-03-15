import pyttsx3  # for voice
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib # for Email

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello, I'm Jarvis sir.Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again Please....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com', 'your_email_password')
    server.sendmail('your_email@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    # speak("Vinay is a programmer")
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'about' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'code' in query:
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to vinay' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "your_email@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry bhai. I'm not able to send this email.")

        elif 'stop' in query:
            speak("Thank you sir. Now I'm leaving.")
            exit()

    
