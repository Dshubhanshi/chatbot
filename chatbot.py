def greet():
    print("Hello! I'm your chatbot. How can I help you today?")

def respond(response):
    response = response.lower()

    if "hello" in response or "hi" in response:
        return "Hi there! How can I assist you?"
    elif "how are you" in response:
        return "I'm just a computer program, but I'm doing well. Thanks for asking!"
    elif ("what is your name"  or "what is your name?") or ("who are you?" or "who are you") in response:
        return "hii i am somuuuunnnnn "
    elif "for what purpose you have build?" in response:
        return "for codealpha internship project i had build"
    elif "bye" in response or "goodbye" in response:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please ask me something else?"

if __name__ == "__main__":
    greet()

    while True:
        response = input("You: ")
        
        if response.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day.")
            break

        responsed = respond(response)
        print("Chatbot:", responsed)
