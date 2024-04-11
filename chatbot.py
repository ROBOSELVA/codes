from flask import Flask, request, jsonify
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import numpy as np
import random
import string

app = Flask(__name__)

# Preprocessing
lemmatizer = WordNetLemmatizer()

def tokenize(text):
    return word_tokenize(text.lower())

def lemmatize(tokens):
    return [lemmatizer.lemmatize(token) for token in tokens]

def remove_punctuation(text):
    return ''.join([char for char in text if char not in string.punctuation])

# Define responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I assist you?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "default": ["I'm not sure I understand.", "Could you please rephrase that?", "Sorry, I didn't catch that."]
}

# Define intent classification rules
intents = {
    "greeting": ["hello", "hi", "hey", "howdy"],
    "goodbye": ["goodbye", "bye", "see you", "take care"],
    "thanks": ["thanks", "thank you"],
}

# Define responses to specific intents
def get_response(intent):
    if intent == "greeting":
        return random.choice(responses["greeting"])
    elif intent == "goodbye":
        return random.choice(responses["goodbye"])
    elif intent == "thanks":
        return random.choice(responses["thanks"])
    else:
        return random.choice(responses["default"])

# Define function to classify user input
def classify_intent(text):
    tokens = tokenize(text)
    lemmas = lemmatize(tokens)
    for intent, keywords in intents.items():
        for word in lemmas:
            if word in keywords:
                return intent
    return "default"

# Define route for chatbot API
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    intent = classify_intent(user_message)
    bot_response = get_response(intent)
    return jsonify({"message": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
