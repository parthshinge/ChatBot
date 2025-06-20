import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

from similarity import get_intent
from intents import intents

def get_response(user_input):
    intent, response = get_intent(user_input)
    return response

def chat():
    print("Chatbot: Hello! Type 'exit' to stop.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
