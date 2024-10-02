#Interactive quiz game wher each question has four possible answers
#USING A DICTIONARY

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr": ["12", "11", "8", "14"],
    "What is the capital of Texas": ["Austin", "San Antonio", "Dallas", "Houston"],
    "The Last Supper was painted by which artist": ["Da Vinci", "Rembrandt", "Picasso", "Michelangelo"]
}

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]  # First item is the correct answer
    print(f"{question}?")
    for alternative in sorted(alternatives):
        print(f" - {alternative}")
    
    answer = input("Your answer: ")

    if answer == correct_answer:
        print("Correct!\n")
    else:
        print(f"The correct answer is {correct_answer!r}, not {answer!r}\n")

