import random
import requests
from config import APIkey

def greet():
    greetings = ["Hello", "Hi", "Hey", "Greetings"]
    return random.choice(greetings)

def tell_joke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I asked my dog what's two minus two. He said nothing.",
        "Why don’t oysters share their pearls? Because they’re shellfish!"
    ]
    return random.choice(jokes)

def get_weather(city):
    api_key = APIkey
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]

        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]

        # Return formatted weather info
        return (f"Weather in {city}:\n"
                f"Temperature: {temperature}°C\n"
                f"Pressure: {pressure} hPa\n"
                f"Humidity: {humidity}%\n"
                f"Description: {description.capitalize()}")
    else:
        return f"Sorry, I couldn't find the weather for {city}. Please check the city name."

context = {}

def respond_to_user_input(user_input):
    user_input = user_input.lower()

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
        return "I can help with basic tasks like chatting, answering simple questions, or telling jokes and weather!"
    elif "joke" in user_input:
        return tell_joke()
    elif "weather" in user_input:
        city = input("Please enter the city name: ")
        return get_weather(city)
    elif "how's it going" in user_input or "what's up" in user_input:
        return random.choice([
            "Not much, just here to chat with you!",
            "I'm just living the chatbot life. How about you?",
            "Same old, same old. What’s going on with you?"
        ])
    elif "my name is" in user_input:
        name = user_input.split("my name is ")[1]
        context["name"] = name
        return f"Nice to meet you, {name}!"

    elif "what's my name" in user_input and "name" in context:
        return f"Your name is {context['name']}."
    else:
        return random.choice([
            "I'm sorry, I didn't understand that. Can you ask something else?",
            "Hmm, that’s a bit unclear. Can you rephrase?",
            "I didn't quite get that. Let's talk about something else!"
        ])

def main():
    print("Chatbot: Hi! How can I help you today?")

    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print(f"Chatbot: {respond_to_user_input(user_input)}")
            break
        print(f"Chatbot: {respond_to_user_input(user_input)}")

if __name__ == "__main__":
    main()