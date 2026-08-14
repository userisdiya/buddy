"""
==========================================
Buddy v1.0
File: config.py
Purpose:
    Stores all global configuration values
    used throughout the Buddy application.
==========================================
"""

# ==========================================
# Application Information
# ==========================================

APP_NAME = "Buddy"
APP_VERSION = "v1.0"

WINDOW_TITLE = f"{APP_NAME} {APP_VERSION}"

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 650


# ==========================================
# Theme
# ==========================================

PRIMARY_COLOR = "#1E1E2F"
SECONDARY_COLOR = "#2A2A40"
ACCENT_COLOR = "#4CAF50"

TEXT_COLOR = "#FFFFFF"
SUBTEXT_COLOR = "#CFCFCF"

BUTTON_COLOR = "#3A3A55"
BUTTON_HOVER = "#50507A"


# ==========================================
# Status Messages
# ==========================================

STATUS_READY = "🟢 Ready"
STATUS_LISTENING = "🎤 Listening..."
STATUS_PROCESSING = "🟡 Thinking..."
STATUS_SPEAKING = "🟣 Speaking..."
STATUS_OFFLINE = "🔴 Offline"


# ==========================================
# Wake Words
# ==========================================

WAKE_WORDS = [
    "buddy",
    "hey buddy",
    "okay buddy",
    "my love"
]


# ==========================================
# Application Paths
# ==========================================

HISTORY_FOLDER = "history"
DATA_FOLDER = "data"
ASSETS_FOLDER = "assets"
BLENDER_PATH = r"C:\Program Files\Blender Foundation\Blender 5.2\blender-launcher.exe"

VSCODE_PATH = r"C:\Users\Drashti Shah\AppData\Local\Programs\Microsoft VS Code\Code.exe"

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

CHROME_PROFILE = "Default"

# ==========================================
# AI Configuration
# ==========================================

MODEL_NAME = "gemini-2.5-flash"


# ==========================================
# Miscellaneous
# ==========================================

DEFAULT_FONT = "Segoe UI"

DEFAULT_FONT_SIZE = 11

CHAT_FONT_SIZE = 12

# ==========================================
# Speech Configuration
# ==========================================

SPEECH_RATE = 180
SPEECH_VOLUME = 1.0
VOICE_NAME = "en-US-AvaMultilingualNeural"