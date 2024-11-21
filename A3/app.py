from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import json
import random

# Initialize the Flask app
app = Flask(__name__)

# Set a secret key for the application
# This is required for session handling to work securely.
app.secret_key = 'your_secret_key'

# ---------------------------------------------
# Route: Home ('/')
# Purpose: Check if the user is already identified.
# If they have visited before, display their score history.
# If not, prompt them to provide their name.
# ---------------------------------------------
@app.route('/')
def index():
    # Retrieve the username from the session
    username = session.get('username', None)

    # If username exists, the user is returning, show their history
    if username:
        history = session.get('history', [])  # Fetch quiz history from the session
        return render_template('welcome_back.html', username=username, history=history)
    else:
        # If no username is found, assume it's a new user
        return render_template('new_user.html')

# ---------------------------------------------
# Route: Set Username ('/set_username')
# Purpose: Save the user's name in the session on their first visit
# and initialize an empty history to track quiz scores.
# ---------------------------------------------
@app.route('/set_username', methods=['POST'])
def set_username():
    # Retrieve the username from the submitted form
    username = request.form.get('username', None)
    
    # Validate the username and store it in the session
    if username:
        session['username'] = username  # Save username for later use
        session['history'] = []  # Initialize a blank score history for the user
        return redirect(url_for('index'))  # Redirect to the home route
    
    # If the form is submitted without a username, return an error
    return "Please enter a valid username", 400

# ---------------------------------------------
# Route: Quiz Game ('/game')
# Purpose: Serve the quiz interface to the user.
# This route simply renders the quiz game page.
# ---------------------------------------------
@app.route('/game')
def game():
    # Render the quiz page (quiz.html)
    return render_template('quiz.html')

# ---------------------------------------------
# Route: Results ('/results')
# Purpose: Display the user's latest quiz results, total score,
# and their quiz history.
# ---------------------------------------------
@app.route('/results')
def results():
    # Fetch the user's latest score and quiz history from the session
    score = session.get('score', 0)  # Default to 0 if no score exists
    total_questions = session.get('total_questions', 0)  # Default to 0 if no questions were recorded
    history = session.get('history', [])  # Retrieve the user's quiz history
    return render_template('results.html', score=score, total_questions=total_questions, history=history)

# ---------------------------------------------
# Function: Load Questions
# Purpose: Load quiz questions from a JSON file.
# This function is called when the quiz game begins.
# ---------------------------------------------
def load_questions():
    # Open the JSON file containing quiz questions
    with open('questions.json', 'r') as file:
        return json.load(file)  # Return the parsed JSON as a Python dictionary

# ---------------------------------------------
# Route: API to Get Questions ('/api/questions')
# Purpose: Provide a randomized set of quiz questions to the frontend.
# Shuffles the questions and their answer options before sending.
# ---------------------------------------------
@app.route('/api/questions', methods=['GET'])
def get_questions():
    # Load the quiz questions from the JSON file
    questions = load_questions()
    
    # Shuffle the order of questions for variety
    random.shuffle(questions)
    
    # Shuffle the options for each question to randomize answers
    for question in questions:
        random.shuffle(question['options'])
    
    # Store the total number of questions in the session for later use
    session['total_questions'] = len(questions)
    
    # Send the shuffled questions back to the client as JSON
    return jsonify(questions)

# ---------------------------------------------
# Route: API to Save Quiz Score ('/api/save_score')
# Purpose: Save the user's latest quiz score in the session.
# Append it to the score history for persistent tracking.
# ---------------------------------------------
@app.route('/api/save_score', methods=['POST'])
def save_score():
    # Parse the JSON payload sent from the client
    data = request.json
    
    # Extract the score from the payload
    score = data.get('score', 0)
    
    # Save the latest score in the session
    session['score'] = score

    # Append the new score to the user's history
    history = session.get('history', [])  # Retrieve current history
    history.append(score)  # Add the new score
    session['history'] = history  # Save updated history back to session

    # Return a success message to the client
    return jsonify({'message': 'Score saved successfully!'})

# ---------------------------------------------
# Main Entry Point
# Purpose: Start the Flask development server.
# Debug mode is enabled for easier debugging during development.
# ---------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)

