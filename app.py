'''import os
from flask import Flask,render_template, request
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

# Configure FLASK_DEBUG from environment variable
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

@app.route('/', methods=['GET', 'POST'])
def index():
    input_text = ''
    if request.method == 'POST':
        input_text = request.form['text_input']
    return render_template('index.html', input_text=input_text)

if __name__ == '__main__':
    app.run()'''

'''# import objects from the Flask model
from flask import Flask, jsonify, request
# declare flask  
app = Flask(__name__)  # define app using Flask
@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works!'})'''

from transformers import pipeline

# Allocate a pipeline for sentiment-analysis
classifier = pipeline('sentiment-analysis')
classifier('We are very happy to include pipeline into the transformers repository.')
[{'label': 'POSITIVE', 'score': 0.9978193640708923}]
