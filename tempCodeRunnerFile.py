from flask import Flask, request, jsonify, render_template
from similarity import get_intent
from intents import intents

app = Flask(__name__)

def get_response(user_input):
    intent = get_intent(user_input)
    if intent == "default":
        return "Sorry, I didn't understand that. Can you please rephrase?"
    return intents[intent]["response"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def chatbot_response():
    user_input = request.args.get('msg')
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
