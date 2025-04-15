
# import pyttsx3, datetime, wikipedia, webbrowser, os, pyautogui


# context = {
#     "awaiting_dictation": False
# }

# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# def handle_command(query):
#     query = query.lower()
#     response = ""

#     if "wikipedia" in query:
#         topic = query.replace("wikipedia", "").strip()
#         result = wikipedia.summary(topic, sentences=2)
#         speak("According to Wikipedia")
#         speak(result)
#         response = result

#     elif "open" in query:
#         domain = query.replace("open", "").strip().replace(" ", "")
#         webbrowser.open(f"https://{domain}.com")
#         response = f"Opening {domain}.com"
#         speak(response)

#     elif "google" or "search" in query:

#         if query.find("search") == True:
#             search = query.replace("search", "").strip()
#         else:
#             search = query.replace("google", "").strip()
#         webbrowser.open(f"https://www.google.com/search?q={search}")
#         response = f"Searching Google for {search}"
#         speak(response)

#     elif "launch notepad" in query:
#         os.startfile("notepad.exe")
#         response = "Opening Notepad"
#         speak(response)

#     elif "launch calculator" in query:
#         os.startfile("calc.exe")
#         response = "Opening Calculator"
#         speak(response)

#     elif "launch vs code" in query:
#         os.startfile("C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
#         response = "Opening VS Code"
#         speak(response)

#     elif "play music" in query:
#         songs = os.listdir("C:\\Users\\USER\\Music")
#         if songs:
#             os.startfile(os.path.join("C:\\Users\\USER\\Music", songs[0]))
#             response = "Playing music"
#             speak(response)
#         else:
#             response = "No music files found"

#     elif "launch settings" in query:
#         pyautogui.hotkey('win', 'i')
#         response = "Opening Settings"

#     elif "launch explorer" in query:
#         pyautogui.hotkey('win', 'e')
#         response = "Opening Explorer"

#     elif "shutdown" in query:
#         os.system("shutdown /s /t 1")
#         response = "Shutting down system"

#     else:
#         response = "Sorry, I didn't understand that"
#         speak(response)

#     return response





















# import pyttsx3
# import datetime
# import wikipedia
# import webbrowser
# import os
# import pyautogui
# import json
# from google import genai
# # import google.generativeai as genai


# # ============== SPEECH OUTPUT ==============
# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()


# def get_intent_from_llm(query):
#     prompt = f"""
# You are an intelligent assistant. Interpret this user command and classify it into an intent with parameters.
# Respond ONLY in JSON format like this:

# {{
#   "intent": "launch_app",
#   "app_name": "calculator"
# }}

# Follow these below given formats correctly:

# if it is of opening applications other than web searching or websites, give like

# {{
#   "intent": "launch_app",
#   "app_name": "calculator"
# }}

# if it is of opening websites, give like:

# {{
#   "intent": "open_website",
#   "app_name": "websitename"
# }}

# Here is the user query: "{query}"
# """

#     try:
#         client = genai.Client(
#             api_key="AIzaSyDv4W67qdw1E7_WsCEHkq0qPuOKTpm08Jc"
#         )  
#         response = client.models.generate_content(
#             model="gemini-2.0-flash", contents=prompt
#         )
#         response_text = response.text.strip()
#         print(response_text)

#         # Handle markdown format if present
#         if response_text.startswith("```json"):
#             response_text = (
#                 response_text.replace("```json", "").replace("```", "").strip()
#             )

#         json_data = json.loads(response_text)
#         return json_data

#     except Exception as e:
#         print("Gemini Error:", e)
#         return {"intent": "unknown"}


# # ============== MAIN HANDLER ==============
# def handle_command(user_query):
#     user_query = user_query.lower()
#     response = ""

#     intent_data = get_intent_from_llm(user_query)
#     intent = intent_data.get("intent")

#     # Intent-based execution
#     if intent == "search_wikipedia":
#         topic = intent_data.get("topic", user_query.replace("wikipedia", "").strip())
#         result = wikipedia.summary(topic, sentences=2)
#         speak("According to Wikipedia")
#         speak(result)
#         response = result

#     elif intent == "open_website":
#         site = intent_data.get(
#             "website", user_query.replace("open", "").strip().replace(" ", "")
#         )
#         webbrowser.open(f"https://{site}.com")
#         response = f"Opening {site}.com"
#         speak(response)

#     elif intent == "google_search":
#         search = intent_data.get("search", user_query)
#         webbrowser.open(f"https://www.google.com/search?q={search}")
#         response = f"Searching Google for {search}"
#         speak(response)

#     elif intent == "launch_app":
#         app = intent_data.get("app_name", "")
#         if app in ["notepad", "text editor"]:
#             os.startfile("notepad.exe")
#             response = "Opening Notepad"
#         elif app in ["calculator"]:
#             os.startfile("calc.exe")
#             response = "Opening Calculator"
#         elif app in ["vs code", "visual studio code"]:
#             os.startfile(
#                 "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#             )
#             response = "Opening Visual Studio Code"
#         elif app in ["settings"]:
#             pyautogui.hotkey("win", "i")
#             response = "Opening Settings"
#         elif app in ["explorer", "file explorer"]:
#             pyautogui.hotkey("win", "e")
#             response = "Opening File Explorer"
#         else:
#             response = f"App '{app}' not recognized"
#         speak(response)

#     elif intent == "play_music":
#         music_dir = "C:\\Users\\USER\\Music"
#         songs = os.listdir(music_dir)
#         if songs:
#             os.startfile(os.path.join(music_dir, songs[0]))
#             response = "Playing music"
#             speak(response)
#         else:
#             response = "No music files found"
#             speak(response)

#     elif intent == "shutdown":
#         speak("Shutting down system")
#         os.system("shutdown /s /t 1")
#         response = "System shutdown initiated"

#     elif intent == "greet":
#         hour = datetime.datetime.now().hour
#         if 0 <= hour < 12:
#             greet = "Good morning"
#         elif 12 <= hour < 16:
#             greet = "Good afternoon"
#         else:
#             greet = "Good evening"
#         response = f"{greet}, how can I assist you?"
#         speak(response)

#     else:
#         response = "Sorry, I didn't understand that command."
#         speak(response)

#     return response


























# import pyttsx3, datetime, wikipedia, webbrowser, os, pyautogui


# context = {
#     "awaiting_dictation": False
# }

# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# def handle_command(query):
#     query = query.lower()
#     response = ""

#     if "wikipedia" in query:
#         topic = query.replace("wikipedia", "").strip()
#         result = wikipedia.summary(topic, sentences=2)
#         speak("According to Wikipedia")
#         speak(result)
#         response = result

#     elif "open" in query:
#         domain = query.replace("open", "").strip().replace(" ", "")
#         webbrowser.open(f"https://{domain}.com")
#         response = f"Opening {domain}.com"
#         speak(response)

#     elif "google" or "search" in query:

#         if query.find("search") == True:
#             search = query.replace("search", "").strip()
#         else:
#             search = query.replace("google", "").strip()
#         webbrowser.open(f"https://www.google.com/search?q={search}")
#         response = f"Searching Google for {search}"
#         speak(response)

#     elif "launch notepad" in query:
#         os.startfile("notepad.exe")
#         response = "Opening Notepad"
#         speak(response)

#     elif "launch calculator" in query:
#         os.startfile("calc.exe")
#         response = "Opening Calculator"
#         speak(response)

#     elif "launch vs code" in query:
#         os.startfile("C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
#         response = "Opening VS Code"
#         speak(response)

#     elif "play music" in query:
#         songs = os.listdir("C:\\Users\\USER\\Music")
#         if songs:
#             os.startfile(os.path.join("C:\\Users\\USER\\Music", songs[0]))
#             response = "Playing music"
#             speak(response)
#         else:
#             response = "No music files found"

#     elif "launch settings" in query:
#         pyautogui.hotkey('win', 'i')
#         response = "Opening Settings"

#     elif "launch explorer" in query:
#         pyautogui.hotkey('win', 'e')
#         response = "Opening Explorer"

#     elif "shutdown" in query:
#         os.system("shutdown /s /t 1")
#         response = "Shutting down system"

#     else:
#         response = "Sorry, I didn't understand that"
#         speak(response)

#     return response





















import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pyautogui
import json
from google import genai
# import google.generativeai as genai


# ============== SPEECH OUTPUT ==============
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_intent_from_llm(query):
    prompt = f"""
You are an intelligent assistant. Interpret this user command and classify it into an intent with parameters.
Respond ONLY in JSON format like this:

{{
  "intent": "launch_app",
  "app_name": "calculator"
}}

Follow these below given formats correctly:

if intent is of searching in wikipedia or opening in wikipedia , give like:

{{
  "intent": "search_wikipedia",
  "topic": "sometopic"
}}

if intent is of opening websites, give like:

{{
  "intent": "open_website",
  "website": "websitename"
}}


if intent is of opening applications other than web searching or websites, give like

{{
  "intent": "launch_app",
  "app_name": "calculator"
}}


if intent is of google search, or even search give like:

{{
  "intent": "google_search",
  "search": "searchcontent"
}}

if intent is of playing music, give like:

{{
  "intent": "play_music"
}}


if intent is of shutting down the laptop or pc or computer, give like:

{{
  "intent": "shutdown"
}}

if the intent is of casual conversation and user is just trying to interact or greet you then 

{{
    "intent" : "greet"
}}




Here is the user query: "{query}"
"""

    try:
        client = genai.Client(
            api_key="AIzaSyDv4W67qdw1E7_WsCEHkq0qPuOKTpm08Jc"
        )  
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        response_text = response.text.strip()
        print(response_text)

        # Handle markdown format if present
        if response_text.startswith("```json"):
            response_text = (
                response_text.replace("```json", "").replace("```", "").strip()
            )

        json_data = json.loads(response_text)
        return json_data

    except Exception as e:
        print("Gemini Error:", e)
        return {"intent": "unknown"}


# ============== MAIN HANDLER ==============
def handle_command(user_query):
    user_query = user_query.lower()
    response = ""

    intent_data = get_intent_from_llm(user_query)
    intent = intent_data.get("intent")

    # Intent-based execution
    if intent == "search_wikipedia":
        topic = intent_data.get("topic", user_query.replace("wikipedia", "").strip())
        result = wikipedia.summary(topic, sentences=2)
        speak("According to Wikipedia")
        speak(result)
        response = result

    elif intent == "open_website":
        site = intent_data.get(
            "website", user_query.replace("open", "").strip().replace(" ", "")
        )
        webbrowser.open(f"https://{site}.com")
        response = f"Opening {site}.com"
        speak(response)

    elif intent == "google_search":
        search = intent_data.get("search", user_query)
        webbrowser.open(f"https://www.google.com/search?q={search}")
        response = f"Searching Google for {search}"
        speak(response)

    elif intent == "launch_app":
        app = intent_data.get("app_name", "")
        if app in ["notepad", "text editor"]:
            os.startfile("notepad.exe")
            response = "Opening Notepad"
        elif app in ["calculator"]:
            os.startfile("calc.exe")
            response = "Opening Calculator"
        elif app in ["vs code", "visual studio code"]:
            os.startfile(
                "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            )
            response = "Opening Visual Studio Code"
        elif app in ["settings"]:
            pyautogui.hotkey("win", "i")
            response = "Opening Settings"
        elif app in ["explorer", "file explorer"]:
            pyautogui.hotkey("win", "e")
            response = "Opening File Explorer"
        else:
            response = f"App '{app}' not recognized"
        speak(response)

    elif intent == "play_music":
        music_dir = "D:\Sync_Seagate\Mirror\Music\Songs"
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
            response = "Playing music"
            speak(response)
        else:
            response = "No music files found"
            speak(response)

    elif intent == "shutdown":
        speak("Shutting down system")
        os.system("shutdown /s /t 1")
        response = "System shutdown initiated"

    elif intent == "greet":
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            greet = "Good morning"
        elif 12 <= hour < 16:
            greet = "Good afternoon"
        else:
            greet = "Good evening"
        response = f"{greet}, how can I assist you?"
        speak(response)

    else:
        response = "Sorry, I didn't understand that command."
        speak(response)

    return response

