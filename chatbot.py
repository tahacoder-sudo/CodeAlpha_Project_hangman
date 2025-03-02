import nltk  # For natural language processing tasks
import random

# Download required NLTK data (only needs to be done once)
try:
    nltk.data.find('tokenizers/punkt')  # Check if punkt tokenizer is already downloaded
except LookupError:
    nltk.download('punkt')  # Download punkt tokenizer if not found

def chatbot_response(user_input):
    """Generates a chatbot response based on user input."""

    # Tokenize user input (split into words)
    tokens = nltk.word_tokenize(user_input.lower())  # Convert to lowercase for consistency

    # Basic keyword-based responses (you can expand this)
    greetings = ["hello", "hi", "hey", "greetings"]
    weather_keywords = ["weather", "forecast", "temperature"]
    bye_keywords = ["bye", "goodbye", "farewell", "see you"]
    help_keywords = ["help", "assistance", "support", "commands"]

    for word in tokens:
      if word in greetings:
          return random.choice(["Hello there! How can I help you today?", "Hi! What can I do for you?", "Hey! Nice to see you!"])
      elif word in weather_keywords:
          return "I'm not a weather expert, but I can suggest checking a weather app or website."
      elif word in bye_keywords:
          return random.choice(["Goodbye! Have a great day.", "See you later!", "Farewell!"])
      elif word in help_keywords:
          return "I can answer simple questions and provide basic information. Try asking me about the weather or saying hello!"

    # Default response if no keywords are matched
    return "I'm still learning. Can you rephrase your question?"

def main():
    print("Welcome to the Enhanced Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "q"]:  # Allow user to exit
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()