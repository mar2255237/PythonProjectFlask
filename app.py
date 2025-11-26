# Import core Flask features: handling requests, rendering HTML, and redirecting URLs.
from flask import Flask, request, render_template_string, redirect, url_for

# Import Bcrypt to securely hash passwords instead of storing them in plain text.
from flask_bcrypt import Bcrypt

app = Flask(__name__)
# Attach Bcrypt for hashing.
bcrypt = Bcrypt(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    output = ""
    username = ""

    if request.method == 'POST':
        # Retrieve user input from the form
        username = request.form['username']
        password = request.form['password']

        # Input Validation Rules for Username and Password
        if not username.isalnum():
            output = "Username must only contain letters and numbers."
        elif len(password) < 8:
            output = "Password must be at least 8 characters."
        elif not any(c.isdigit() for c in password):
            output = "Password must have at least 1 number."
        elif not any(not c.isalnum() for c in password):
            output = "Password must contain at least 1 special character."
        else:
            # Hash the user password
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            # Redirect to the result page, passing username and hashed password in the URL.
            return redirect(url_for('result', username=username, password=hashed_password))

    # Create HTML form
    form_html = f'''
    <form method="POST" action="/login">
        <label>Username:</label>
        <input type="text" name="username" value="{username}">

        <label>Password:</label>
        <input type="password" name="password">

        <input type="submit" value="Login">
    </form>

    <p>{output}</p>
    '''

    return render_template_string(form_html)


# URL Results page
@app.route('/result')
def result():
    # Retrieve values passed through the URL
    username = request.args.get("username")
    password = request.args.get("password")

    return f"Username: {username} Hashed Password: {password}"


if __name__ == '__main__':
    app.run(debug=True, port=5001)
