from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():

    # Do we need any logic here?

    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():

    # Name must be at least 3 characters

    # Email must not be blank

    # Email must be in valid email format

    # If any checks fail - go back to the login page and display flash messages

    # Otherwise log them in and go to the success page


    # What should it return?
    return redirect('/success')

@app.route('/success')
def success():
    
    # Should we do any logic here?
    
    return render_template('success.html')



if __name__ == "__main__":
    app.run(debug=True)