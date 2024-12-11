from flask import Flask, request, jsonify, send_file
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import io
import os
from flask_cors import CORS
import json
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend


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

# Route: Retrieve all flashcards from JSON file
@app.route("/get-flashcards", methods=["GET"])
def get_flashcards():
    try:
        flashcards_file = "flashcards.json"

        # Load flashcards from the JSON file
        with open(flashcards_file, "r") as file:
            flashcards = json.load(file)

        return jsonify(flashcards), 200
    except (FileNotFoundError, json.JSONDecodeError):
        return jsonify([]), 200  # Return an empty list if the file doesn't exist or is invalid
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

# Route: Edit a specific flashcard
@app.route("/edit-flashcard", methods=["PUT"])
def edit_flashcard():
    try:
        data = request.json
        index = data.get("index")
        updated_question = data.get("question")
        updated_answer = data.get("answer")

        if index is None or not isinstance(index, int):
            return jsonify({"message": "Valid flashcard index is required!"}), 400
        if not updated_question or not updated_answer:
            return jsonify({"message": "Both question and answer are required!"}), 400

        flashcards_file = "flashcards.json"

        # Load existing flashcards
        with open(flashcards_file, "r") as file:
            flashcards = json.load(file)

        # Ensure index is within range
        if index < 0 or index >= len(flashcards):
            return jsonify({"message": "Flashcard index out of range!"}), 400

        # Update the flashcard
        flashcards[index]["question"] = updated_question
        flashcards[index]["answer"] = updated_answer

        # Save the updated flashcards back to the file
        with open(flashcards_file, "w") as file:
            json.dump(flashcards, file, indent=4)

        return jsonify({"message": "Flashcard updated successfully!"}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500
    # Route to save quiz results
@app.route("/save-quiz-results", methods=["POST"])
def save_quiz_results():
    try:
        data = request.json
        username = data.get("username")
        percentage = data.get("percentage")
        date = data.get("date")

        # Save results to a CSV file
        results_file = "quiz_results.csv"
        new_entry = pd.DataFrame([[username, percentage, date]], columns=["Username", "Percentage", "Date"])

        # Append to the CSV file or create a new one if it doesn't exist
        if os.path.exists(results_file):
            new_entry.to_csv(results_file, mode="a", header=False, index=False)
        else:
            new_entry.to_csv(results_file, mode="w", header=True, index=False)

        return jsonify({"message": "Results saved successfully!"}), 201

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500
    
@app.route("/generate-scatter-plot", methods=["GET"])
def generate_scatter_plot():
    try:
        username = request.args.get("username")
        results_file = "quiz_results.csv"

        print(f"Received username: {username}")
        print(f"Checking if results file exists: {os.path.exists(results_file)}")

        if not os.path.exists(results_file):
            print("Results file not found.")
            return jsonify({"message": "No results found!"}), 404

        df = pd.read_csv(results_file)
        print(f"DataFrame loaded successfully. Data:\n{df}")

        user_results = df[df["Username"] == username]
        print(f"Filtered results for user '{username}':\n{user_results}")

        if user_results.empty:
            print("No results found for this user.")
            return jsonify({"message": "No results found for this user!"}), 404

        # Generate the scatter plot
        plt.figure(figsize=(10, 5))
        plt.scatter(user_results["Date"], user_results["Percentage"], color='blue', s=50)

        plt.xlabel("Date")
        plt.ylabel("Score (%)")
        plt.title(f"Quiz Scores for {username}")
        plt.xticks(rotation=45)
        plt.grid(True)

        img = io.BytesIO()
        plt.tight_layout()
        plt.savefig(img, format="png")
        img.seek(0)

        return send_file(img, mimetype="image/png")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500





# Run the application
if __name__ == "__main__":
    init_db()
    app.run(debug=True)