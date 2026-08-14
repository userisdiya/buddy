"""
==========================================
Buddy v1.0
File: listener.py

Purpose:
    Handles microphone input and converts
    speech into text.
==========================================
"""

import speech_recognition as sr


class Listener:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.recognizer.energy_threshold = 300

        self.recognizer.dynamic_energy_threshold = True

        self.recognizer.pause_threshold = 1.2

    def listen(self):

        with sr.Microphone() as source:

            print("Listening...")

            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

            try:

                audio = self.recognizer.listen(
                    source,
                    timeout=25,
                    phrase_time_limit=15
                )

                text = self.recognizer.recognize_google(audio)

                text = text.lower().strip()

                print(f"You: {text}")

                return text

            except sr.WaitTimeoutError:

                return None

            except sr.UnknownValueError:

                return None

            except sr.RequestError:

                return "OFFLINE"

            except Exception as e:

                print(e)

                return None


listener = Listener()