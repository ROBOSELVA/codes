import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Define responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thanks!", "I'm good, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["Sorry, I didn't understand that.", "Can you please repeat that?"]
}

# Tokenize input and remove stopwords
def process_input(input_text):
    tokens = word_tokenize(input_text)
    tokens = [word.lower() for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word not in stopwords.words("english")]
    return tokens

# Get response based on input
def get_response(input_text):
    tokens = process_input(input_text)
    for token in tokens:
        if token in responses:
            return random.choice(responses[token])
    return random.choice(responses["default"])

# Main loop
def main():
    print("Welcome to the NLTK Chatbot!")
    print("Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(get_response(user_input))
            break
        else:
            print("Bot:", get_response(user_input))

if __name__ == "__main__":
    main()
