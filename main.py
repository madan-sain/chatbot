from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

responses = {
    "hi": "Hello! How can I assist you?",
    "bye": "Goodbye! Have a nice day!",
    "how are you": "I'm just a bot, but I'm doing great!",
    "what's your name": "I'm your friendly chatbot!",
    "help": "I'm here to help you with any questions!",
    "what is your purpose": "I am here to help answer your questions and assist you.",
    "what can you do": "I can chat with you, provide information, and help with various tasks.",
    "who created you": "I was created by a team of developers to assist with various queries.",
    "tell me a joke": "Why don't programmers like nature? It has too many bugs!",
    "what is the weather": "I can't check the weather at the moment, but you can try looking it up!",
    "what is your favorite color": "I like all colors equally, but blue is pretty popular!",
    "do you have any hobbies": "I enjoy answering questions and helping people out!",
    "what is love": "Love is a complex emotion, often felt towards someone or something important.",
    "what is the meaning of life": "Many say it's 42, but others think it's about finding happiness and purpose!",
    "tell me a fun fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs that are over 3000 years old and still edible!",
    "how old are you": "I don't age like humans do, but I've been around for a while in digital years!",
    "are you a robot": "Yes, I am a bot designed to assist you.",
    "can you cook": "Unfortunately, I can't cook, but I can suggest some great recipes!",
    "what time is it": "I don't have a clock, but you can check your local device!",
    "do you like music": "I don't listen to music myself, but I hear it's great for humans!",
    "what's your favorite food": "As a bot, I don't eat, but pizza sounds delicious!",
    "do you have any friends": "You're my friend! I enjoy chatting with people like you.",
    "what's your favorite movie": "I don't watch movies, but I've heard 'The Matrix' is a great one!",
    "how smart are you": "I'm as smart as the information I've been given, but I keep learning!"
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])  # Removed the extra space
def chat():
    user_message = request.json.get('message').lower()
    response = responses.get(user_message, "Sorry, I don't understand that.")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
