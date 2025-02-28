import random

def greet():
    greetings = ["Hello", "Hi", "Hey", "Greetings"]
    return random.choice(greetings)

def respond_to_user_input(user_input):
    user_input = user_input.lower()

    # Check for common questions and provide answers
    if "how are you" in user_input:
        return "I'm doing great, thank you for asking!"
    elif "hello" in user_input or "hi" in user_input:
        return greet()
    elif "your name" in user_input:
        return "I am a simple chatbot created in Python."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "what is your purpose" in user_input:
        return "My purpose is to help you with simple conversations and tasks!"
    elif "help" in user_input:
        return "I can help with basic tasks like chatting, answering simple questions, or telling jokes!"
    else:
        return "I'm sorry, I didn't understand that. Can you ask something else?"

def main():
    print("Chatbot: Hi! How can I help you today?")

    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print(f"Chatbot: {respond_to_user_input(user_input)}")
            break
        print("Chatbot: ", respond_to_user_input(user_input))

if __name__ == "__main__":
    main()