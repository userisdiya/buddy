"""
==========================================
Buddy v1.0
File: commands.py
==========================================
"""

from config import WAKE_WORDS

from apps.desktop import desktop
from apps.browser import browser
from ai import buddy_ai


class CommandHandler:

    def __init__(self):

        self.desktop_commands = {
            "open blender": "Opening Blender for you, sweetheart.",
            "open vscode": "Opening VS Code for you, honey.",
            "open vs code": "Opening VS Code for you, honey.",
            "open visual studio code": "Opening VS Code for you, honey.",
            "open v s code": "Opening VS Code for you, honey.",
            "open code": "Opening VS Code for you, honey.",
            "open file explorer": "Opening File Explorer for you, sweetheart.",
            "open calculator": "Opening Calculator for you, honey.",
        }

        self.stop_words = [
            "stop",
            "stop it",
            "buddy stop",
            "buddy stop it",
            "stop listening",
            "stop listening buddy",
        ]

    def remove_wake_word(self, text):

        text = text.lower().strip()

        for wake_word in WAKE_WORDS:

            if text.startswith(wake_word):

                return text.replace(wake_word, "", 1).strip()

        return text

    def execute(self, text):

        if not text:
            return None

        if text == "OFFLINE":
            return "I'm offline right now, sweetheart."

        command = self.remove_wake_word(text)

        if command == "":
            return "Yes, sweetheart?"

        # ==========================
        # Stop Buddy
        # ==========================

        if any(word in command for word in self.stop_words):
            return "__EXIT__"

        # ==========================
        # Desktop Commands
        # ==========================

        if command in self.desktop_commands:

            if desktop.execute(command):
                return self.desktop_commands[command]

            return "Sorry sweetheart, I couldn't open that application."

        # ==========================
        # Browser Commands
        # ==========================

        words = command.split()

        if words:

            first_word = words[0]

            # --------------------------
            # Open
            # --------------------------

            if first_word == "open":

                if browser.open(command):
                    return "Opening it for you, sweetheart."

                return "Sorry sweetheart, I couldn't open that."

            # --------------------------
            # Search
            # --------------------------

            if first_word == "search":

                if browser.search(command):
                    return "Searching Google for you, honey."

                return "Sorry sweetheart, I couldn't search that."

            # --------------------------
            # Play
            # --------------------------

            if first_word == "play":

                if browser.play(command):
                    return "Playing it for you, sweetheart."

                return "Sorry honey, I couldn't play that."

        # ==========================
        # Gemini AI
        # ==========================

        return buddy_ai.ask(command)


command_handler = CommandHandler()