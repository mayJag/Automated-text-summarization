from flask import Flask, request, render_template
from transformers import BartTokenizer, BartForConditionalGeneration, pipeline

app = Flask(__name__)

model_name = 'facebook/bart-large-cnn'
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

def summarize_text(text, max_length=130, min_length=30):
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    summary = summarizer(text, max_length=max_length, min_length=min_length, truncation=True)
    return summary[0]['summary_text']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    summary = summarize_text(text)
    return render_template('result.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
