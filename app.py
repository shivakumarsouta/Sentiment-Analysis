from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    polarity = None
    user_input = ''

    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        if user_input.strip():
            blob = TextBlob(user_input)
            polarity = blob.sentiment.polarity
            if polarity > 0:
                sentiment = "Positive 😊"
            elif polarity < 0:
                sentiment = "Negative 😠"
            else:
                sentiment = "Neutral 😐"

    return render_template('index.html', sentiment=sentiment, polarity=polarity, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
