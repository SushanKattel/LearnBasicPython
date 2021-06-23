import pyttsx3, datetime, speech_recognition as sr, wikipedia, webbrowser, os, smtplib, random, ctypes, platform
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]


def wifi():
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split(
            '\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}|  {:<}".format(i, ""))
    #print("I am wifi")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Creator Sushan! ")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon Creator Sushan!")
    else:
        speak("Good Evening Creator Sushan!")

    speak("Hi, I am your virtual assistance, BAKLOL. How can I help you sir ?")


def takeInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining.........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Rocognizing Voice........")
        query = r.recognize_google(audio, language="en-in")
        print("Sir you said : {query}\n")
    except Exception as e:
        print(e)
        print("Please Say that again Sir.....")
        return "None"
    return query


 #def sendEmail(to,content):
  # server = smtplib.SMTP("",)
   # server.ehlo()
    #server.starttls() #we can also use text file for password for security reason and use path instead of password
    #server.login("sushankattel@gmail.com","password")  # I dont give you pswd :p
    #server.sendmail("your sending mail identity i.e your email address",to,content)
    #server.close()


if __name__ == "__main__":
    speak(" Welcome To The System Master Sushan")
    speak("I am your virtual assistant BAKLOL! ")

    while True:
        query = takeInput().lower()

        if "wikipedia" in query:
            speak("Searching information on Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("Speaking........\n")
            speak("Sir, According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open twitter" in query:
            webbrowser.open("www.twitter.com")

        elif "open google" in query:
            webbrowser.open("www.google.com")

        elif "homepage" in query:
            webbrowser.open("www.facebook.com/sushan.kattel.1")

        elif "home page" in query:
            webbrowser.open("www.facebook.com/sushan.kattel.1")

        elif "watch movie" in query:
            webbrowser.open("www.watchonlinemovies.com.pk")

        elif "debug" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "online course" in query:
            webbrowser.open("www.udemy.com")

        elif "music" in query:
            music_dir = "F://personal files/music/Njk and new//"
            select = random.randint(1, 118)
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[select]))



        elif "song" in query:
            music_dir = "F://personal files/music/Njk and new/new1/"
            select = random.randint(0, 32)
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[select]))

        elif "music videos" in query:
            music_dir = "E://Music videos/"
            select = random.randint(2, 248)
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[select]))


        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, the time is {strTime}")

        elif "watch video" in query:
            webbrowser.open("www.watchonlinemovies.com.pk")

        elif "powerpoint" in query:
            path = "C://Program Files (x86)/Microsoft Office/root/Office16/POWERPNT.EXE"

            os.startfile(path)

        elif "power point" in query:
            path = "C://Program Files (x86)/Microsoft Office/root/Office16/POWERPNT.EXE"
            os.startfile(path)

        elif "presentation" in query:
            path = "C://Program Files (x86)/Microsoft Office/root/Office16/POWERPNT.EXE"
            os.startfile(path)

        elif "slides" in query:
            path = "C://Program Files (x86)/Microsoft Office/root/Office16/POWERPNT.EXE"
            os.startfile(path)

        elif "document" in query:
            path = "C://Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE"
            os.startfile(path)

        elif "excel" in query:
            path = "C://Program Files (x86)/Microsoft Office/root/Office16/EXCEL.EXE"
            os.startfile(path)

        elif "data entry" in query:
            path = "C://Program Files (x86)/Microsoft Office/root/Office16/EXCEL.EXE"
            os.startfile(path)

        elif "opera" in query:
            path = "C://Users/asus/AppData/Local/Programs/Opera/launcher.exe"
            os.startfile(path)

        elif "browser" in query:
            path = "C://Program Files (x86)/Google/Chrome/Application/chrome.exe"
            os.startfile(path)

        elif "internet" in query:
            path = "C://Program Files (x86)/Google/Chrome/Application/chrome.exe"
            os.startfile(path)





        elif "remix" in query:
            path = "D://Program Files (x86)/Audacity/audacity.exe"
            os.startfile(path)




        elif "python programming" in query:
            path = "D://Program Files/JetBrains/PyCharm Community Edition 2018.2.4/bin/pycharm64.exe"
            os.startfile(path)

        elif "notepad" in query:
            path = "%windir%//system32/notepad.exe"
            os.startfile(path)

        elif "notepad plus plus" in query:
            path = "D://Program Files/Notepad++/notepad++.exe"
            os.startfile(path)


        elif "notepad plus" in query:
            path = "D://Program Files/Notepad++/notepad++.exe"
            os.startfile(path)

        elif "text editor" in query:
            path = "D://Program Files/Sublime Text 3/sublime_text.exe"
            os.startfile(path)

        elif "jupyter" in query:
            path = "D://Users/asus/Anaconda3/python.exe D://Users/asus/Anaconda3/cwp.py D://Users/asus/Anaconda3 D://Users/asus/Anaconda3/python.exe D://Users/asus/Anaconda3/Scripts/jupyter-notebook-script.py %USERPROFILE%/"
            os.startfile(path)

        elif "jupiter" in query:
            path = "D://Users/asus/Anaconda3/python.exe D://Users/asus/Anaconda3/cwp.py D://Users/asus/Anaconda3 D://Users/asus/Anaconda3/python.exe D://Users/asus/Anaconda3/Scripts/jupyter-notebook-script.py %USERPROFILE%/"
            os.startfile(path)

        elif "notebook" in query:
            path = "D://Users/asus/Anaconda3/python.exe D://Users/asus/Anaconda3/cwp.py D://Users/asus/Anaconda3 D://Users/asus/Anaconda3/python.exe D://Users/asus/Anaconda3/Scripts/jupyter-notebook-script.py %USERPROFILE%/"
            os.startfile(path)

        elif "hello" in query:
            wishMe()

        elif "hi" in query:
            wishMe()

        elif "what's up" in query:
            wishMe()

        elif "hey" in query:
            wishMe()

        elif "How are you" in query:
            speak("I am fine! Thank you.")

        elif "who" in query:
            print("Searching.....")
            speak("Searching")
            webbrowser.open("https://www.google.com/search?client=opera&q={query}")

        elif "which" in query:
            print("Searching.....")
            speak("Searching")
            webbrowser.open("https://www.google.com/search?client=opera&q={query}")

        elif "what" in query:
            print("Searching.....")
            speak("Searching")
            webbrowser.open("https://www.google.com/search?client=opera&q={query}")

        elif "how" in query:
            print("Searching.....")
            speak("Searching")
            webbrowser.open("https://www.google.com/search?client=opera&q={query}")

        elif "why" in query:
            print("Searching.....")
            speak("Searching")
            webbrowser.open("https://www.google.com/search?client=opera&q={query}")

        elif "search" in query:
            print("Searching.....")
            speak("Searching")
            webbrowser.open("https://www.google.com/search?client=opera&q={query}")

        elif "exit" in query:
            print("Good bye sir, Have a good day!")
            speak("Good bye Sir, Have a good day!")
            exit()

        elif "bye" in query:
            print("Good bye sir, Have a good day!")
            speak("Good bye Sir, Have a good day!")
            exit()

        elif "goodbye" in query:
            print("Good bye sir, Have a good day!")
            speak("Good bye Sir, Have a good day!")
            exit()

        elif "have a break" in query:
            print("Good bye sir, Have a good day!")
            speak("Good bye Sir, Have a good day!")
            exit()

        elif "turnoff yourself" in query:
            print("Good bye sir, Have a good day!")
            speak("Good bye Sir, Have a good day!")
            exit()

        elif "shutdown yourself" in query:
            print("Good bye sir, Have a good day!")
            speak("Good bye Sir, Have a good day!")
            exit()

        elif "do a greeting" in query:
            print("Hello Sir !")
            speak("Hello Sir !")

        elif "type" in query:
            print("Sure Sir, as your Wish!")
            speak("Sure Sir, as your Wish!")
            print(query)

        elif "thank you" in query:
            print("You're extremly Welcome Sir. Good to hear this.")
            speak("You're extremly Welcome Sir. Good to hear this.")

        elif "okey" in query:
            print("Got it Sir !")
            speak("Got it Sir !")

        elif "okay" in query:
            print("Got it Sir !")
            speak("Got it Sir !")

        elif "ok" in query:
            print("Got it Sir !")
            speak("Got it Sir !")

        elif "logout system" in query:
            speak("Are you Sure Sir, Do you want to Log Out the System ?")
            choice = takeInput().lower()

            if "yes" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
            elif "s" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
            elif "yeah" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
            elif "yup" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
            else:
                print("Oops! Sorry Sir, continuing the system....")
                speak("Oops! Sorry Sir, continuing the system....")
                continue

        elif "log out system" in query:
            speak("Are you Sure Sir, Do you want to Log Out the System ?")
            choice = takeInput().lower()

            if "yes" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
            elif "s" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
            elif "yeah" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
            elif "yup" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
            else:
                print("Oops! Sorry Sir, continuing the system....")
                speak("Oops! Sorry Sir, continuing the system....")
                continue

        elif "logout from the system" in query:
            speak("Are you Sure Sir, Do you want to Log Out the System ?")
            choice = takeInput().lower()

            if "yes" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
            elif "s" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
            elif "yeah" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
            elif "yup" in choice:
                print("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                speak("As your Wish Sir !. Logging Out the System, Pausing all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                ctypes.windll.user32.LockWorkStation()
                exit()
            else:
                print("Oops! Sorry Sir, continuing the system....")
                speak("Oops! Sorry Sir, continuing the system....")
                continue

        elif "introduce" in query:
            print("Hello! I am BAKLOL , Virtual Assistance of Sushan Kattel.")
            speak("Hello! I am BAKLOL , Virtual Assistance of Sushan Kattel.")
            print(f"OS Type {platform.system()}")
            speak(f"OS Type {platform.system()}")
            print(f"Platform {platform.platform()}")
            speak(f"Platform {platform.platform()}")
            print(f"OS Version {platform.version()}")
            speak(f"OS Version {platform.version()}")
            print(f"Processor {platform.processor()}")
            speak(f"Processor {platform.processor()}")
            print(f"Processor Architecture {platform.architecture()}")
            speak(f"Processor Architecture {platform.architecture()}")
            print("RAM 8 Giga bytes")
            speak("RAM 8 Giga bytes")
            print("Hard Disk 1 Tera Bytes and solid state drive 120 Giga Bytes")
            speak("Hard Disk 1 Tera Bytes and solid state drive 120 Giga Bytes")
            print(f"Machine Type {platform.machine()}")
            speak(f"Machine Type {platform.machine()}")
            #print(f"Desktop Name {platform.uname()}")
            #speak(f"Desktop Name {platform.uname()}")
            print("That's it Sir !")
            speak("That's it Sir !")

        elif "introduction" in query:
            print("Hello! I am BAKLOL , Virtual Assistance of Sushan kattel.")
            speak("Hello! I am BAKLOL , Virtual Assistance of Sushan kattel.")
            print(f"OS Type {platform.system()}")
            speak(f"OS Type {platform.system()}")
            print(f"Platform {platform.platform()}")
            speak(f"Platform {platform.platform()}")
            print(f"OS Version {platform.version()}")
            speak(f"OS Version {platform.version()}")
            print(f"Processor {platform.processor()}")
            speak(f"Processor {platform.processor()}")
            print(f"Processor Architecture {platform.architecture()}")
            speak(f"Processor Architecture {platform.architecture()}")
            print("RAM 8 Giga bytes")
            speak("RAM 8 Giga bytes")
            print("Hard Disk 1 Tera Bytes and solid state drive 120 Giga Bytes")
            speak("Hard Disk 1 Tera Bytes and solid state drive 120 Giga Bytes")
            print(f"Machine Type {platform.machine()}")
            speak(f"Machine Type {platform.machine()}")
            # print(f"Desktop Name {platform.uname()}")
            # speak(f"Desktop Name {platform.uname()}")
            print("That's it Sir !")
            speak("That's it Sir !")


        elif "shutdown computer" in query:
            speak("Are you Sure Sir, Do you want to Shut Down the System ?")
            choice = takeInput().lower()

            if "yes" in choice:
                print("As your Wish Sir !. Shutting down the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Shutting down System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /s /t 1")
                exit()
            elif "s" in choice:
                print("As your Wish Sir !. Shutting down the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Shutting down System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /s /t 1")
                exit()
            elif "yeah" in choice:
                print("As your Wish Sir !. Shutting down the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Shutting down System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /s /t 1")
                exit()
            elif "yup" in choice:
                print("As your Wish Sir !. Shutting down the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Shutting down System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /s /t 1")
                exit()
            else:
                print("Oops! Sorry Sir, continuing the system....")
                speak("Oops! Sorry Sir, continuing the system....")
                continue

        elif "shutdown system" in query:
            speak("Are you Sure Sir, Do you want to Shut Down the System ?")
            choice = takeInput().lower()

            if "yes" in choice:
                print("As your Wish Sir !. Shutting down the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Shutting down System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /s /t 1")
                exit()
            elif "s" in choice:
                print("As your Wish Sir !. Shutting down the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Shutting down System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /s /t 1")
                exit()
            elif "yeah" in choice:
                print("As your Wish Sir !. Shutting down the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Shutting down System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /s /t 1")
                exit()
            elif "yup" in choice:
                print("As your Wish Sir !. Shutting down the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Shutting down System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /s /t 1")
                exit()
            else:
                print("Oops! Sorry Sir, continuing the system....")
                speak("Oops! Sorry Sir, continuing the system....")
                continue

        elif "restart system" in query:
            speak("Are you Sure Sir, Do you want to Restart the System ?")
            choice = takeInput().lower()

            if "yes" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
            elif "s" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
            elif "yeah" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
            elif "yup" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
            else:
                print("Oops! Sorry Sir, continuing the system....")
                speak("Oops! Sorry Sir, continuing the system....")
                continue


        elif "restart computer" in query:
            speak("Are you Sure Sir, Do you want to Restart the System ?")
            choice = takeInput().lower()

            if "yes" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
            elif "s" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
            elif "yeah" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
            elif "yup" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
            else:
                print("Oops! Sorry Sir, continuing the system....")
                speak("Oops! Sorry Sir, continuing the system....")
                continue

        elif "reboot system" in query:
            speak("Are you Sure Sir, Do you want to Restart the System ?")
            choice = takeInput().lower()

            if "yes" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
            elif "s" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
            elif "yeah" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
            elif "yup" in choice:
                print("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                speak("As your Wish Sir !. Restarting the System, Stopping all the processing actions !")
                print("Good bye sir, Have a good day!")
                speak("Good bye Sir, Have a good day!")
                os.system("shutdown /r /t 1")
                exit()
            else:
                print("Oops! Sorry Sir, continuing the system....")
                speak("Oops! Sorry Sir, continuing the system....")
                continue

        elif "say" in query:
            speak(query)

        elif "wi-fi password" in query:
            speak(wifi())


        elif "email" in query:
            print("Sorry Sir, Due to Security Reason I am Unable to send this email at the Moment !")
            speak("Sorry Sir, Due to Security Reason I am Unable to send this email at the Moment !")
#         try:
#             speak("What should i say sir ?")
#             content = takeInput()
#             to = "destination email address"
#             sendEmail(to,content)
#             speak(f"Sir, Email has been sent! to {to}")
#         except Exception as e:
#             print(e)
#             speak("Sorry Sir, I am Unable to send this email at the moment!")


#     End Line of The Project