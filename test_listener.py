from listener import Listener

listener = Listener()

print("===== Buddy Listener Test =====")
print("Speak after the beep...\n")

text = listener.listen()

print("\nYou said:")
print(text)

input("\nPress Enter to Exit...")