def chatbot():
    print("Welcome to Basic Chatbot!")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hello! How are you?")

        elif user == "hi":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I am fine. Thank you!")

        elif user == "your name":
            print("Bot: I am CodeAlpha Chatbot.")

        elif user == "what can you do":
            print("Bot: I can answer simple questions.")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()