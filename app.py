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

import os
from flask import Flask, jsonify, request
from transformers import pipeline

app = Flask(__name__)

model_path = "./model"

@app.route('/')
def classify_review():
    review = request.args.get('review')
    api_key = request.args.get('api_key')
    if review is None or api_key != "MyCustomerApiKey":
        return jsonify(code=403, message="bad request")
    classify = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
    return classify("that was great")[0]


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google Cloud
    # Run, a webserver process such as Gunicorn will serve the app.
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
