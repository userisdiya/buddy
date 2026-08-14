"""
==========================================
Buddy v1.0
File: main.py

Purpose:
    Entry point of Buddy Desktop Assistant.
==========================================
"""

import sys
import threading

from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import QApplication

from gui import BuddyWindow
from listener import Listener
from speech import speech
from responses.greetings import get_greeting
from commands import command_handler


class BuddyWorker(QObject):

    status_signal = Signal(str)
    user_signal = Signal(str)
    buddy_signal = Signal(str)
    speak_signal = Signal(str)

    def __init__(self):
        super().__init__()

        self.listener = Listener()
        self.running = True

    def run(self):

        while self.running:

            self.status_signal.emit("🎤 Listening...")

            text = self.listener.listen()

            if not text:
                continue

            self.user_signal.emit(text)

            self.status_signal.emit("🧠 Thinking...")

            reply = command_handler.execute(text)

            if reply == "__EXIT__":

                self.buddy_signal.emit("Alright honey.")

                speech.speak("Alright honey.")

                self.running = False

                QApplication.quit()

                return

            if reply:

                self.buddy_signal.emit(reply)

                self.speak_signal.emit(reply)

            self.status_signal.emit("Ready")

    def stop(self):

        self.running = False


def main():

    app = QApplication(sys.argv)

    window = BuddyWindow()
    window.show()

    greeting = get_greeting()

    window.add_message("Buddy", greeting)

    # Speak greeting without blocking GUI
    threading.Thread(
        target=speech.speak,
        args=(greeting,),
        daemon=True
    ).start()

    worker = BuddyWorker()

    thread = QThread()

    worker.moveToThread(thread)

    thread.started.connect(worker.run)

    worker.status_signal.connect(window.set_status)

    worker.user_signal.connect(
        lambda text: window.add_message("You", text)
    )

    worker.buddy_signal.connect(
        lambda text: window.add_message("Buddy", text)
    )

    worker.speak_signal.connect(speech.speak)

    thread.start()

    def cleanup():

        worker.stop()

        thread.quit()

        thread.wait()

    app.aboutToQuit.connect(cleanup)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()