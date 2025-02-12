import speech_recognition as sr
import datetime
import webbrowser
import os
class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
    def listen(self):
        with self.microphone as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(
                    audio, language="en-US")
                print("You said:", text)
                self.process_command(text)
            except sr.UnknownValueError:
                print("Sorry, I didn't understand that.")
            except sr.RequestError as e:
                print("Error:", e)
    def process_command(self, text):
        if "hello" in text.lower():
            self.respond("Hello! How can I assist you today?")
        elif "what time" in text.lower():
            self.respond("The current time is " +
                         datetime.datetime.now().strftime("%I:%M %p"))
        elif "what date" in text.lower():
            self.respond("Today's date is " +
                         datetime.date.today().strftime("%B %d, %Y"))
        elif "search" in text.lower():
            query = text.split("search", 1)[1].strip()
            self.respond("Searching for " + query + "...")
            webbrowser.open("https://www.google.com/search?q=" + query)
        else:
            self.respond("Sorry, I didn't understand that command.")
    def respond(self, text):
        print("Assistant:", text)
assistant = VoiceAssistant()
while True:
    assistant.listen()
