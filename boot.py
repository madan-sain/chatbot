from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

responses = {
    "hi": "Hello! How can I assist you?",
    "bye": "Goodbye! Have a nice day!",
    "how are you": "I'm just a bot, but I'm doing great!",
    "what's your name": "I'm your friendly chatbot!",
    "help": "I'm here to help you with any questions!"
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/git ', methods=['POST'])
def chat():
    user_message = request.json.get('message').lower()
    response = responses.get(user_message, "Sorry, I don't understand that.")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
