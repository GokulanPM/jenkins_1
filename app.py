from flask import Flask, request, jsonify, render_template_string
import mysql.connector

app = Flask(__name__)

# MySQL connection
def get_db_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="flaskdb"
    )

@app.route('/')
def index():
    return '''
        <h2>Flask + MySQL running in Docker 🚀</h2>
        <form action="/add_form" method="post">
            <input type="text" name="name" placeholder="Enter Name" required>
            <button type="submit">Add User</button>
        </form>
        <br>
        <a href="/users">View All Users</a>
    '''

@app.route('/add_form', methods=['POST'])
def add_form():
    name = request.form['name']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()
    return f"User {name} added! <br><a href='/'>Go Back</a>"

@app.route('/users')
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
