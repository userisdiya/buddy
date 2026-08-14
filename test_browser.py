from apps.browser import browser

print("===== Buddy Browser Test =====")

choice = input("""
1. Chrome
2. Google
3. YouTube
4. Gmail
5. GitHub
6. Gemini

Choose: """)

commands = {
    "1": "open chrome",
    "2": "open google",
    "3": "open youtube",
    "4": "open gmail",
    "5": "open github",
    "6": "open gemini"
}

result = browser.execute(commands.get(choice, ""))

print(f"\nSuccess: {result}")

input("\nPress Enter to Exit...")
