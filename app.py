from flask import Flask , render_template
import torch
from transformers import pipeline

app = Flask(__name__)

classifier = pipeline("sentiment-analysis")
value = classifier(
    [
        "I've been waiting for a HuggingFace course my whole life.",
        "I hate this so much!",
    ]
)



@app.route('/')
def index():
  value = classifier(
    [
        "you are beautiful",
        "I hate this so much!",
    ]
)
  return render_template('index.html', script_value=value)

if __name__ == '__main__':
  app.run(debug=True)



