import random

def greeting():
    responses = ["Hi there! How can I help you today?", "Hello! What can I assist you with?", "Hey! How can I assist you?"]
    return random.choice(responses)

def farewell():
    responses = ["Goodbye!", "Farewell!", "See you later!"]
    return random.choice(responses)

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return greeting()
    elif "bye" in user_input or "goodbye" in user_input:
        return farewell()
    else:
        return "I'm just a simple chatbot. I don't understand that."

# Main loop
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
