from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
openai.api_key = os.getenv("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")



app = Flask(__name__)
CORS(app)

# OpenAI API Key/Create this by loggin into your Chat GPT account
openai.api_key = "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"

@app.route("/generate_flashcards", methods=["POST"])
def generate_flashcards():
    subject_text = request.form.get("subject", "")
    if not subject_text.strip():
        return jsonify({"flashcards": []})
    
    # Split input text into paragraphs
    paragraphs = [p.strip() for p in subject_text.split("\n") if p.strip()]
    
    flashcards = []
    try:
        for paragraph in paragraphs:
            # Generate two questions and answers per paragraph
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Generate 2 questions and answers based on this paragraph:\n\n{paragraph}\n\nFormat: Question: <question> Answer: <answer>",
                max_tokens=300,
                n=1,
                temperature=0.7
            )
            # Extract questions and answers
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
