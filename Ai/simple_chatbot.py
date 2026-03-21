#Build a bot which provides all the information related to text in search box


def simple_chatbot():
    print("ChatBot: Hello! I'm a simple chatbot. Type 'bye' to exit.")    
    while True:
        user_input = input("You: ").lower()
        if user_input == "hello" or user_input == "hi":
            print("ChatBot: Hi there!")
        elif user_input == "how are you":
            print("ChatBot: I'm just a bunch of code, but thanks for asking!")
        elif user_input == "what is your name":
            print("ChatBot: I'm SimpleBot.")
        elif user_input == "bye":
            print("ChatBot: Goodbye! Have a nice day :)")
            break
        else:
            print("ChatBot: I'm not sure how to respond to that.")
simple_chatbot()
