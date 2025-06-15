def respond(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! How can I help you today?"
    elif "weather" in user_input:
        return "Try our weather app! 😄"
    elif "bye" in user_input:
        return "Goodbye! Stay safe."
    else:
        return "Hmm... I didn’t quite get that."

print("🤖 Chatbot ready! (type 'bye' to quit)")
while True:
    msg = input("You: ")
    if "bye" in msg.lower():
        print("Bot: Goodbye! 👋")
        break
    print("Bot:", respond(msg))
