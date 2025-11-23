from flask import Flask, g
import sqlite3

app = Flask(__name__)

# Name of the SQLite database file
DATABASE = 'students.db'


def get_db():
    # Get the database connection for this request
    db = getattr(g, '_database', None)
    if db is None:
        # Create a new connection if one doesn't exist yet
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    # Close the database connection after the request ends
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    # Simple test route
    return "Flask SQLite App is running!"


@app.route('/init_db')
def init_db():
    # Create the database file and table if they don't exist
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        grade TEXT
                    )''')
    conn.commit()
    return "Database and 'students' table initialized!"


@app.route('/add_student/<name>/<grade>')
def add_student(name, grade):
    # Insert a new student into the database
    conn = get_db()
    conn.execute('INSERT INTO students (name, grade) VALUES (?, ?)', (name, grade))
    conn.commit()
    return f"Student {name} with grade {grade} added to the database!"


@app.route('/students')
def students():
    # Retrieve and show all students from the database
    conn = get_db()
    cursor = conn.execute('SELECT * FROM students')
    all_students = cursor.fetchall()
    return f"Students: {all_students}"


if __name__ == '__main__':
    # Run this app on port 5003
    app.run(debug=True, host='127.0.0.1', port=5003)
