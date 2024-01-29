from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import random
from flask import session

# List of words for the hangman game
words = ['python', 'java', 'javascript', 'ruby', 'html', 'css', 'flask', 'django']

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    session['word'] = random.choice(words)
    session['guesses'] = []
    return redirect(url_for('game'))

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        letter = request.form['letter']
        if letter not in session['guesses']:
            session['guesses'].append(letter)
            session.modified = True
        if set(session['word']) <= set(session['guesses']):
            return redirect(url_for('win'))
        if len([guess for guess in session['guesses'] if guess not in session['word']]) > 5:
            return redirect(url_for('lose'))
    return render_template('game.html', word=session['word'], guesses=session['guesses'])

@app.route('/guess', methods=['POST'])
def guess():
    guess = request.form.get('guess')
    # Check if the guess is correct (replace this with your actual logic)
    correct = guess in session['word']
    return jsonify(correct=correct)

@app.route('/win')
def win():
    return render_template('win.html')

@app.route('/lose')
def lose():
    return render_template('lose.html')

if __name__ == '__main__':
    app.run(debug=True)