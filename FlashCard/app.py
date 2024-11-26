from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import json
from PyPDF2 import PdfReader
from docx import Document
import csv

def save_questions_to_csv(questions, file_name="questions.csv"):
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Question", "Type"])
        for question in questions:
            writer.writerow([question, "multiple_choice"])


def extract_text_from_docx(file_path):
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def generate_batch_questions(paragraphs):
    joined_paragraphs = "\n\n".join(paragraphs)
    prompt = f"""
    Based on the following text, generate a set of multiple-choice questions and answers:
    {joined_paragraphs}

    Format:
    Question: <question>
    Options: <option1>, <option2>, <option3>, <option4>
    Correct Answer: <correct_option>
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]



# Initialize Flask app
app = Flask(__name__)
CORS(app)

# OpenAI API Key
openai.api_key = "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"

import openai


def generate_questions(text, question_type="multiple_choice"):
    prompt = f"""
    Based on the following text, generate 5 {question_type} questions. 
    Text: {text}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# In-memory progress data (for simplicity)
progress_data = {"quizzes": []}

@app.route("/save_progress", methods=["POST"])
def save_progress():
    user_progress = request.json
    progress_data["quizzes"].append(user_progress)
    with open("progress.json", "w") as f:
        json.dump(progress_data, f)
    return jsonify({"message": "Progress saved successfully!"})

@app.route("/get_progress", methods=["GET"])
def get_progress():
    with open("progress.json", "r") as f:
        return jsonify(json.load(f))

@app.route("/generate_quiz", methods=["POST"])
def generate_quiz():
    subject_text = request.form.get("subject", "")
    if not subject_text.strip():
        return jsonify({"quiz": []})

    paragraphs = [p.strip() for p in subject_text.split("\n") if p.strip()]

    questions = []
    try:
        for paragraph in paragraphs:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Generate one detailed multiple-choice question based on this paragraph:\n\n{paragraph}\n\nFormat:\nQuestion: <question>\nOptions: <option1>, <option2>, <option3>, <option4>\nCorrect Answer: <correct_option>",
                max_tokens=300,
                n=1,
                temperature=0.7
            )
            qa_pair = response.choices[0].text.strip().split("\n")
            question = {}
            for line in qa_pair:
                if line.startswith("Question:"):
                    question["question"] = line.split("Question:")[1].strip()
                elif line.startswith("Options:"):
                    question["options"] = line.split("Options:")[1].strip().split(", ")
                elif line.startswith("Correct Answer:"):
                    question["correct_answer"] = line.split("Correct Answer:")[1].strip()
            questions.append(question)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"quiz": questions})

@app.route("/generate_flashcards", methods=["POST"])
def generate_flashcards():
    subject_text = request.form.get("subject", "")
    if not subject_text.strip():
        return jsonify({"flashcards": []})
    
    paragraphs = [p.strip() for p in subject_text.split("\n") if p.strip()]
    
    flashcards = []
    try:
        for paragraph in paragraphs:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Generate 2 questions and answers based on this paragraph:\n\n{paragraph}\n\nFormat: Question: <question> Answer: <answer>",
                max_tokens=300,
                n=1,
                temperature=0.7
            )
            qa_pairs = response.choices[0].text.strip().split("\n")
            for qa in qa_pairs:
                if "Question:" in qa and "Answer:" in qa:
                    question = qa.split("Question:")[1].split("Answer:")[0].strip()
                    answer = qa.split("Answer:")[1].strip()
                    flashcards.append({"question": question, "answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"flashcards": flashcards})

if __name__ == "__main__":
    app.run(debug=True)
