# app.py

from flask import Flask, request, render_template
from summarizer import summarize_text  # Importing the summarizer function

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if 'text' not in request.form:
        return render_template('index.html', error="No text provided")
    
    text = request.form['text']
    if text.strip() == '':
        return render_template('index.html', error="Text is empty")
    
    # Get the number of sentences for the summary if provided
    num_sentences = request.form.get('num_sentences', 3)
    try:
        num_sentences = int(num_sentences)
    except ValueError:
        num_sentences = 3  # default to 3 if the conversion fails
    
    summary = summarize_text(text, num_sentences)
    return render_template('result.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
