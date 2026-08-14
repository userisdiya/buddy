from ai import buddy_ai

while True:

    question = input("\nYou : ")

    if question.lower() == "exit":
        break

    reply = buddy_ai.ask(question)

    print("\nBuddy :", reply)