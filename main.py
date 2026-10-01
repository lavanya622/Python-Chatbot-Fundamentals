from responses import get_response

def chatbot():
    print("👋 Hello! I’m your Coding Assistant. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("👋 Bye! Happy coding.")
            break
        response = get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chatbot()
