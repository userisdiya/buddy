"""
==========================================
Buddy v1.0
File: ai.py

Purpose:
    Handles AI conversations using
    Google Gemini.
==========================================
"""

import google.generativeai as genai
from dotenv import load_dotenv
import os


class BuddyAI:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise Exception("Gemini API Key not found in .env")

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel("gemini-flash-latest")
        self.system_prompt = """
You are Buddy.

Personality:
- Funny.
- Be factually accurate.
- If you mention dates, years, names, or historical facts,prefer accuracy over making a joke.
- Slightly sarcastic.
- Friendly.
- Never rude.
- Talk like a best friend.
- Address the user naturally using words like
  'sweetheart' or 'honey' occasionally.
- Keep responses conversational.
- Don't sound like a robot.
- Keep answers concise unless the user asks for details.
"""

    def ask(self, question):

        try:

            prompt = f"""
{self.system_prompt}

User:
{question}
"""

            response = self.model.generate_content(prompt)

            if response and response.text:

                return response.text.strip()

            return "Honey... Gemini decided to stay quiet."

        except Exception as e:

            print(f"Gemini Error: {e}")

            return (
                "Sweetheart, I couldn't reach my brain right now. "
                "Can you try again in a moment?"
            )


buddy_ai = BuddyAI()