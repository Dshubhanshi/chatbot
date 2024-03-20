def greetings():
    print("Hello! I'm chatbot. How can I help you?")

def respond(u_i):
    u_i = u_i.lower()

    if "hello" in u_i or "hi" in u_i:
        return "Hello there! How can I help you?"
    elif "how are you" in u_i:
        return "I'm just a computer program, but I'm doing well. Thanks for asking!"
    elif "what is your name?" in u_i or "who are you?" in u_i:
        return "Hello! I am ChatBot."
    elif "what do you do?" in u_i or "what is your job?" in u_i or "what is your work?" in u_i:
        return "For the CodeAlpha internship project, I have been built."
    elif "bye" in u_i or "goodbye" in u_i:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please ask me something else?"

if __name__ == "__main__":
    greetings()

    while True:
        u_i = input("You: ")
        
        if u_i.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day.")
            break

        response = respond(u_i)
        print("Chatbot:", response)
