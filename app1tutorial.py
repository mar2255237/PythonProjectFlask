from flask import Flask

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    # Run the Flask app on port 5002 with debug mode on
    app.run(debug=True, port=5002)
