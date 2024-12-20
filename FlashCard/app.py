from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS
import json

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

# Initialize SQLite database for users
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Route: User registration
@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"message": "Username and password are required."}), 400

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return jsonify({"message": "Registration successful!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"message": "Username already exists."}), 400
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500
    finally:
        if conn:
            conn.close()

# Route: User login
@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        if user:
            return jsonify({"message": "Login successful!"})
        return jsonify({"message": "Invalid credentials."}), 401
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500
    finally:
        if conn:
            conn.close()

# Route: Insert flashcard into JSON file
@app.route("/insert-flashcard", methods=["POST"])
def insert_flashcard():
    try:
        data = request.json
        question = data.get("question")
        answer = data.get("answer")

        if not question or not answer:
            return jsonify({"message": "Both question and answer are required!"}), 400

        # Load or initialize flashcards JSON file
        flashcards_file = "flashcards.json"
        try:
            with open(flashcards_file, "r") as file:
                flashcards = json.load(file)
        except FileNotFoundError:
            flashcards = []

        # Add new flashcard to the deck
        flashcards.append({"question": question, "answer": answer})

        # Save updated flashcards to JSON file
        with open(flashcards_file, "w") as file:
            json.dump(flashcards, file)

        return jsonify({"message": "Flashcard added successfully!"}), 201
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

# Run the application
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
