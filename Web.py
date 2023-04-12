import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the text from the form
        text = request.form['text']
        
        # Send the text to the OpenAI API
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer YOUR_API_KEY_HERE'
        }
        data = {
            'prompt': text,
            'max_tokens': 10,
            'temperature': 0.5,
            'n': 1
        }
        response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=data)
        
        # Display the API response on the page
        completions = response.json()['choices']
        return render_template('index.html', completions=completions)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
