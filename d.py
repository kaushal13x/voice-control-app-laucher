import streamlit as st
import speech_recognition as sr
import os
import webbrowser

st.text("""                       
        
                             --------------------
                             App Launcher    
                             --------------------
""")
query = st.text_input(" ", placeholder="Search...                                                                                                                              Speak...", )


if st.button("Start Listening"):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Listening... Speak your command.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        st.success(f"You said: {command}")

        command = command.lower()

        if "chrome" in command:
            st.write("Opening Chrome...")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif "instagram" in command:
            st.write("Opening Instagram...")
            webbrowser.open("https://www.instagram.com/")

        elif "excel" in command:
            st.write("Opening  excel...")
            os.system("start excel")

        elif "VLC" in command:
            st.write("Opening vlc media...")
            os.system("start vlc")

        elif "ms word" in command:
            st.write("opening ms word...")
            os.system("start winword")

        elif "youtube" in command:
            st.write("Opening YouTube...")
            webbrowser.open("https://www.youtube.com/")

        elif "notepad" in command:
            st.write("Opening Notepad...")
            os.system("start notepad")

        elif "calculator" in command:
            st.write("Opening Calculator...")
            os.system("start calc")

        elif "command Prompt" in command:
            st.write("Command Prompt...")
            os.system("start cmd")

        elif "control Pane" in command:
            st.write("Control Panel...")
            os.system("start control")

        elif "calender" in command:
            st.write("Opening Calender...")
            os.system("start outlookcal")
        else:
            st.warning("Command not recognized.")

    except sr.UnknownValueError:
        st.error("Sorry, could not understand your voice.")
    except Exception as e:
        st.error(f"Error: {e}")
