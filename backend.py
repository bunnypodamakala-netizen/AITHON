from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)  # Enable CORS to allow frontend JavaScript to communicate with backend

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    
    # Placeholder for processing user input and generating response
    # Here just echoing back with a prefix for demo
    response_text = f"Assistant: You said '{user_input}'"
    
    return jsonify({'response': response_text})

if _name_ == '_main_':
    app.run(debug=True)
