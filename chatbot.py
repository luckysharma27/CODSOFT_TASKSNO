# CODSOFT - Artificial Intelligence Internship
# Task 1: Chatbot with Rule-Based Responses

def get_response(user_input):
    text = user_input.lower().strip()

    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! How can I help you?"
    elif "how are you" in text:
        return "I'm doing great! Thanks for asking."
    elif "your name" in text or "who are you" in text:
        return "I'm a simple rule-based chatbot created for the CodSoft AI internship."
    elif "help" in text:
        return "Sure! You can ask me about my name, internship, or say goodbye."
    elif "internship" in text:
        return "This chatbot is Task 1 of the CodSoft Artificial Intelligence internship."
    elif "thank" in text:
        return "You're welcome!"
    elif "bye" in text or "goodbye" in text:
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I don't understand that yet. Please try another question."


def main():
    print("=" * 55)
    print("        CODSOFT AI - RULE-BASED CHATBOT")
    print("=" * 55)
    print("Type 'bye' or 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Bot: Goodbye! Have a great day.")
            break

        response = get_response(user_input)
        print("Bot:", response)

        if "goodbye" in response.lower():
            break


if __name__ == "__main__":
    main()
