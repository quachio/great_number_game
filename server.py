from flask import Flask, redirect, render_template, session, request
import random


app = Flask(__name__)
app.secret_key = 'ZKdRFjd6WpFCD+9NGETh4'

@app.route('/')
def index():
    if 'random_number' not in session:
        session['random_number'] = random.randint(0, 101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():

    session['guess'] = int(request.form['guess'])

    print(request.form['guess'], session['random_number'] )
    return redirect('/')

@app.route('/playagain', methods=['POST'])
def play_again():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
