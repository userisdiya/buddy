# 🤖 Buddy v1.0

> A modular Python-based voice assistant that can control desktop applications, open browser resources, and use AI/LLM capabilities to handle natural-language requests.

## 🔗 Repository

**GitHub:** https://github.com/userisdiya/buddy

---

## 📌 Overview

**Buddy v1.0** is a Python-based desktop voice assistant designed to provide hands-free interaction with a computer.

The assistant listens to a user's voice command, converts speech into text, identifies the user's intent, and then performs the appropriate action.

Depending on the request, Buddy can:

* Open desktop applications
* Open browser resources
* Execute predefined commands
* Handle general conversational requests
* Send unsupported requests to an AI/LLM
* Respond using text-to-speech

The project follows a **modular architecture**, allowing new commands, applications, responses, and AI capabilities to be added without restructuring the entire application.

---

## ✨ Features

### 🎙️ Voice Interaction

* Speech-to-text command recognition
* Voice-based interaction
* Text-to-speech responses
* Continuous command processing

### 🖥️ Desktop Automation

Buddy can open commonly used desktop applications such as:

* Visual Studio Code
* Blender
* File Explorer
* Calculator

### 🌐 Browser Automation

Buddy can launch Chrome and open commonly used resources:

* Google
* YouTube
* Gmail
* Gemini
* GitHub

Chrome can also be configured to use a selected browser profile.

### 🧠 AI / LLM Integration

Buddy can use an AI/LLM when a request does not match one of the predefined commands.

This allows Buddy to handle:

* General questions
* Natural-language requests
* Conversational interactions
* Unrecognized queries
* Explanations and informational requests

The generated response can then be converted into speech.

### 🧩 Modular Command Processing

Commands are categorized before execution:

```text
DESKTOP
BROWSER
AI
STOP
OFFLINE
NONE
```

This separation makes the command system easier to maintain and extend.

---

## 🔄 How Buddy Works

```text
User speaks a command
        ↓
Speech Recognition
        ↓
Command Processing
        ↓
Intent Detection
        ↓
 ┌───────────────┬───────────────┬───────────────┐
 ↓               ↓               ↓
Desktop         Browser          AI / LLM
Command         Command          Request
 ↓               ↓               ↓
Execute         Open            Generate
Action          Resource        Response
        \          |             /
         \         |            /
          └──── Voice Response ┘
```

---

## 🏗️ Project Architecture

```text
BUDDY/
│
├── apps/
│   ├── __init__.py
│   ├── browser.py
│   └── desktop.py
│
├── assets/
│
├── data/
│   └── commands.json
│
├── history/
│
├── responses/
│   ├── __init__.py
│   ├── confirmations.py
│   ├── errors.py
│   ├── greetings.py
│   └── offline.py
│
├── .env
├── ai.py
├── commands.py
├── config.py
├── gui.py
├── listener.py
├── logger.py
├── main.py
├── speech.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Core Modules

| File                 | Purpose                                            |
| -------------------- | -------------------------------------------------- |
| `main.py`            | Application entry point and overall execution flow |
| `listener.py`        | Handles voice listening and input                  |
| `speech.py`          | Handles speech recognition and text-to-speech      |
| `commands.py`        | Processes and classifies user commands             |
| `ai.py`              | Handles AI/LLM requests                            |
| `config.py`          | Stores application configuration                   |
| `gui.py`             | Handles the graphical user interface               |
| `logger.py`          | Handles application logging                        |
| `apps/desktop.py`    | Handles desktop application commands               |
| `apps/browser.py`    | Handles browser-related commands                   |
| `data/commands.json` | Stores configurable command mappings               |
| `responses/`         | Contains predefined assistant responses            |

---

## 🛠️ Technology Stack

| Technology             | Purpose                               |
| ---------------------- | ------------------------------------- |
| **Python**             | Core programming language             |
| **PySide6**            | Graphical user interface              |
| **Speech Recognition** | Converts voice input into text        |
| **Text-to-Speech**     | Converts responses into spoken output |
| **AI / LLM API**       | Handles natural-language requests     |
| **JSON**               | Stores command configuration          |
| **Git**                | Version control                       |
| **GitHub**             | Source-code hosting                   |

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/userisdiya/buddy.git
cd buddy
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root and add the required API configuration.

Example:

```env
AI_API_KEY=your_api_key_here
```

> **Never commit API keys, passwords, or other sensitive information to GitHub.**

### 6. Run Buddy

```bash
python main.py
```

---

## 🎤 Example Commands

### Desktop Commands

```text
"Open VS Code"
"Open Blender"
"Open File Explorer"
"Open Calculator"
```

### Browser Commands

```text
"Open Chrome"
"Open Google"
"Open YouTube"
"Open Gmail"
"Open Gemini"
"Open GitHub"
```

### AI / Conversational Requests

```text
"Explain what an API is."
"What is the difference between Python and JavaScript?"
"Help me understand recursion."
"What is FastAPI?"
```

If a request does not match a predefined command, Buddy can route it to the configured AI/LLM.

---

## 🔐 Security

Buddy may require API credentials for AI functionality.

Sensitive information should be stored using environment variables rather than being written directly into source code.

The project's `.gitignore` prevents sensitive and unnecessary files from being committed.

Important ignored files and directories include:

```text
.env
.venv/
venv/
env/
__pycache__/
*.pyc
```

---

## 📦 Dependencies

Project dependencies are stored in:

```text
requirements.txt
```

The virtual environment itself is **not included in the repository**.

To recreate the development environment:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚧 Current Version

### Buddy v1.0

The current version focuses on:

* Voice interaction
* Speech recognition
* Text-to-speech
* Desktop application launching
* Browser resource launching
* Command classification
* AI/LLM fallback
* Voice responses
* Modular architecture
* Basic graphical interface
* Configurable command mappings

---

## 🔮 Future Improvements

Potential improvements for future versions include:

* More desktop automation commands
* More browser automation
* Improved natural-language command detection
* Better conversational memory
* More advanced AI integration
* Improved graphical interface
* System information commands
* File and folder operations
* Application control
* More configurable commands
* Improved error handling
* Personalized assistant settings

---

## 🎯 Project Goal

Buddy was created as a practical project to explore how multiple technologies can work together to create a functional desktop assistant.

The project combines:

```text
Voice Recognition
       +
Python Automation
       +
GUI Development
       +
Command Processing
       +
AI / LLM Integration
       +
Text-to-Speech
```

The long-term goal is to evolve Buddy from a basic command-based assistant into a more capable personal desktop AI assistant.

---

## 📚 What This Project Demonstrates

Buddy demonstrates practical experience with:

* Python application development
* Modular software architecture
* GUI development
* Voice-based interaction
* Desktop automation
* Browser automation
* API integration
* AI/LLM integration
* Command processing
* Environment configuration
* Error handling
* Git and GitHub workflow

---

## 👨‍💻 Author

**Drashti Shah**

### GitHub

https://github.com/userisdiya

---

## 📄 License

This project is currently intended for educational and personal development purposes.
