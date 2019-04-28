from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = 'JoeIsTheMan'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
 
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():

    print(request.form)
    

    if len(request.form["name"]) < 3:
        flash("Name must be at least 2 characters", "name")

    if len(request.form['email']) < 1:
        flash("Email required", "email")

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email", "email")

    if '_flashes' in session:
        print(session)
        return redirect('/')
    else:
        session['user_id'] = 1
        session['user_name'] = request.form['name']
        return redirect('/success')

@app.route('/success')
def success():

    if "user_id" not in session:
        session.clear()
        flash("You must have the key to enter the kingdom.", "security")
        print(session)
        return redirect('/')

    else:
        return render_template('success.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)