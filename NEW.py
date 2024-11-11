import pyautogui
import time
import speech_recognition as sr
import pyttsx3
import webbrowser


# It converts " Text to Speech" :--
def speak(text):
  engine = pyttsx3.init()
  engine.setProperty('rate', 128)    
  engine.setProperty('volume', 0.9)   
  engine.say(text)
  engine.runAndWait()

# It converts "My Speech to text.lower()":--
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You : {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

#It executes different conmands based on different logics:--
def execute_command():
    while True :
        a=listen_command()
        pyautogui.click(1778,17)
        # For opening CHATGPT:--
        if a=="open chat":
            # We can use this on personal desktop :--
            #pyautogui.doubleClick(229,794) # click on chatgpt
            #time.sleep(1)
            #pyautogui.click(1379,46)
            
            webbrowser.open("https://chatgpt.com")
            time.sleep(1.5)
            pyautogui.click(150,130) 
            pyautogui.click(1098,968)# click on new chat
            query=""
            while (query!="exit"):
                speak("What's next, sir?")
                query=listen_command()
                pyautogui.write(query, interval=0)
                pyautogui.press('enter')
                time.sleep(6) 
            pyautogui.click(1905,11)    # TO CLICK EXIT ( X button )

        # For opening YOUTUBE:--
        if a=="open youtube":
            pyautogui.doubleClick(234,690) # click on youtube
            time.sleep(1)
            pyautogui.click(613,74) # click on "search"
            query=""

            while (query!="exit"):
                speak("What's next, sir?")
                query=listen_command()
                pyautogui.write(query, interval=0)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(500,730)
                time.sleep(200) 
            pyautogui.click(1905,11)    # TO CLICK EXIT ( X button )


        # For opening EDGE BROWSER:--
        if a=="open edge":
            pyautogui.doubleClick(233,905) # click on edge
            time.sleep(1)
            query=""
            while (query!="exit"):
                speak("What's next, sir?")
                query=listen_command()
                pyautogui.write(query, interval=0)
                pyautogui.press('enter') 
            pyautogui.click(1905,11)    # TO CLICK EXIT ( X button )

        # For opening MUSIC:--
        if a=="open music":
            url="https://www.youtube.com/watch?v=fmI_Ndrxy14&list=PLWC7BA9nvcDLMFBXf6wrrJOY85AYhcmyb&pp=gAQBiAQB"
            webbrowser.open(url)
            time.sleep(2.5)
            pyautogui.click(14430,515)
            wait()
        elif a=="exit" :
            print("GOODAY SIR")
            speak("GOODAY SIR")
            break

# It "wakes" upon hearing "NEXUS" and  "sleep" upon hearing  "go to sleep" respectively :--
def main():
    wake_word = "nexus"
    sleep_word = "go to sleep"
    assistant_awake = True
    
    while True:
        if assistant_awake:
            print("Listening ...")
            speak("INITIALIZING NEXUS...")
            command = listen_command()
            if command:  
                if sleep_word in command:
                    assistant_awake = False
                    speak("Entering sleeping mode. Say 'nexus' to wake me up again.")
                else:
                    speak(" What can I do for u Sir")
                    execute_command()
                    
        else:
            print("Sleeping...")
            command = listen_command()
            if command and wake_word in command: 
                assistant_awake = True
                speak("INITIALIZING NEXUS. What can I do for u Sir")





main()
