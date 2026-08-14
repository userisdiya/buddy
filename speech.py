"""
==========================================
Buddy v1.0
File: speech.py

Purpose:
    Handles Text-to-Speech using Edge TTS.
==========================================
"""

import asyncio
import os
import tempfile
import time

import edge_tts
import pygame

from config import VOICE_NAME


class SpeechEngine:

    def __init__(self):

        pygame.mixer.init()

        self.is_speaking = False

    async def _generate(self, text, filename):

        communicate = edge_tts.Communicate(
            text=text,
            voice=VOICE_NAME,
        )

        await communicate.save(filename)

    def speak(self, text):

        if not text:
            return

        if self.is_speaking:
            return

        self.is_speaking = True

        try:

            temp_file = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".mp3",
            )

            temp_path = temp_file.name
            temp_file.close()

            asyncio.run(
                self._generate(text, temp_path)
            )

            pygame.mixer.music.load(temp_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():

                time.sleep(0.1)

            pygame.mixer.music.unload()

            if os.path.exists(temp_path):

                os.remove(temp_path)

        except Exception as e:

            print(f"Speech Error: {e}")

        finally:

            self.is_speaking = False

    def stop(self):

        try:

            pygame.mixer.music.stop()

        except Exception:

            pass

        self.is_speaking = False


speech = SpeechEngine()