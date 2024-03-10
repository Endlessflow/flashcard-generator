from flask import Flask, render_template
from flask import request, jsonify
from flask_cors import CORS

from OpenAIChat import OpenAIChat

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_flashcards', methods=['POST'])
def generate_flashcards():
    data = request.get_json()
    input_text = data['text']

    chat = OpenAIChat(model="gpt-4-turbo-preview")

    # Load templates from files
    chat.load_template_from_file("prompts/simple_flashcard.txt", 0.4)

    # Get a response from the API by filling the template
    response = chat.get_response("simple_flashcard", verbose=False, content=input_text)

    return jsonify({'output': response})

if __name__ == '__main__':
    app.run(debug=True)
