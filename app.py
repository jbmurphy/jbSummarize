# app.py
from flask import Flask, request, jsonify
import re
import nltk
nltk.download('punkt')
import unicodedata
import numpy as np
from gensim.summarization import summarize
import json

app = Flask(__name__)

def clean_and_parse_document(document):
    document = re.sub('\n', ' ', document)
    document = document.strip()
    sentences = nltk.sent_tokenize(document)
    sentences = [sentence.strip() for sentence in sentences]
    return sentences

def summarize_text(text, summary_ratio=None, word_count=30):
    sentences = clean_and_parse_document(text)
    cleaned_text = ' '.join(sentences)
    summary = summarize(cleaned_text, split=True, ratio=summary_ratio, word_count=word_count)
    return summary 

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        content = request.json
        text = content['txt']
        print(text)
        summary = summarize_text(text)
        print(summary)
        return json.dumps(summary)
    else:
        return 'Hello Microsoft from docker'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


