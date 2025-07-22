import datetime
import random

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def respond(user_input):
    user_input = user_input.lower()
    # You can add more keywords and responses here
    if "hello" in user_input or "hi" in user_input:
        return random.choice(["Hello! How can I help you?", "Hi there!"])
    elif "date" in user_input:
        return f"Today's date is {get_date()}"
    elif "time" in user_input:
        return f"Current time is {get_time()}"
    elif "joke" in user_input:
        return "Why did the Python developer go broke? Because he used up all his cache!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that. You can teach me new things!"

print("Chatbot Start! (Type 'bye' to exit)")

while True:
    inp = input("You: ")
    reply = respond(inp)
    print("Bot:", reply)
    if "bye" in inp.lower():
        break
