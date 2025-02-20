import sqlite3
from flask import Flask, request, jsonify, g

app = Flask(__name__)
DATABASE = 'users.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# def init_db():
#     with app.app_context():
#         db = get_db()
#         with app.open_resource('schema.sql', mode='r') as f:
#             db.cursor().executescript(f.read())
#         db.commit()
def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)
        db.commit()

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (data['name'], data['email']))
    db.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()
    return jsonify([{'id': user[0], 'name': user[1], 'email': user[2]} for user in users])

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (id,))
    user = cursor.fetchone()
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'id': user[0], 'name': user[1], 'email': user[2]})

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (data['name'], data['email'], id))
    db.commit()
    if cursor.rowcount == 0:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'message': 'User updated successfully'})

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    db.commit()
    if cursor.rowcount == 0:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
