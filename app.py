from flask import Flask, render_template
from flask import request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_flashcards', methods=['POST'])
def generate_flashcards():
    data = request.get_json()
    input_text = data['text']

    # for now just return the input doubled
    return jsonify({'output': input_text * 2})

if __name__ == '__main__':
    app.run(debug=True)
