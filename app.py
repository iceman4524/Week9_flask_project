from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key

# Simulated user database
users = {
    "testuser": generate_password_hash("password123")  # Storing hashed passwords
}

@app.route('/')
def home():
    if 'username' in session:
        return f"Hello, {session['username']}! <a href='/logout'>Logout</a>"
    return "Welcome! <a href='/login'>Login</a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            return redirect(url_for('home'))
        return "Invalid credentials! <a href='/login'>Try again</a>"

    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
