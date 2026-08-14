import random

STARTUP_GREETINGS = [
    "Good to see you again, sweetheart.",
    "Good to see you again, sweetheart. I'm ready whenever you are.",
    "Hey honey. What are we building today?",
    "Buddy online, sweetheart.",
    "Morning, honey. Let's make something awesome."
]

def get_greeting():
    return random.choice(STARTUP_GREETINGS)