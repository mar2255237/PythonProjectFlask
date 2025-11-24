from flask import Flask, request, render_template_string, redirect, url_for
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    output = ""
    username = ""

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

