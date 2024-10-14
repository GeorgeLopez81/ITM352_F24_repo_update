QUESTIONS = {
    "History": {
        "What is the capital of Texas?": ["Austin", "San Antonio", "Dallas", "Houston"],
        "Who was the first President of the United States?": ["George Washington", "Thomas Jefferson", "John Adams", "Abraham Lincoln"]
    },
    "Art": {
        "The Last Supper was painted by which artist?": ["Da Vinci", "Rembrandt", "Picasso", "Michelangelo"],
        "Starry Night was painted by which artist?": ["Van Gogh", "Monet", "Dali", "Kandinsky"]
    },
    "NBA Trivia": {
        "Which player has the most NBA championships?": ["Bill Russell", "Michael Jordan", "Kobe Bryant", "LeBron James"],
        "Who is the all-time leading scorer in NBA history?": ["Kareem Abdul-Jabbar", "Karl Malone", "LeBron James", "Michael Jordan"]
    }
}


def ask_question(question, alternatives):
    correct_answer = alternatives[0]  # First item in the list is the correct answer
    sorted_alternatives = sorted(alternatives)  # Sort the alternatives alphabetically
    print(f"\n{question}")
    for label, alternative in enumerate(sorted_alternatives, start=1):
        print(f"  {label}. {alternative}")
    
    # Get the user's answer, ensuring they input a valid option
    while True:
        answer = input("Your answer (1-4): ").strip()
        if answer in ['1', '2', '3', '4']:
            break
        print("Invalid choice. Please enter a number between 1 and 4.")
    
    chosen_answer = sorted_alternatives[int(answer) - 1]  # Convert input to index
    
    if chosen_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Incorrect! The correct answer was {correct_answer}.")
        return False


def choose_category(questions):
    print("Choose a category:")
    categories = list(questions.keys())
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")
    
    while True:
        choice = input("Enter the number of your choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            return categories[int(choice) - 1]
        print("Invalid choice. Please try again.")

def run_quiz(questions):
    category = choose_category(questions)
    score = 0
    total_questions = len(questions[category])

    print(f"\nYou chose: {category}\n")
    for question, alternatives in questions[category].items():
        if ask_question(question, alternatives):
            score += 1
    
    print(f"\nQuiz finished! You got {score} out of {total_questions} correct.")
    return score, total_questions

def save_score_history(category, score, total_questions):
    with open("score_history.txt", "a") as file:
        file.write(f"Category: {category}, Score: {score}/{total_questions}\n")

def main():
    QUESTIONS = {
        "History": {
            "What is the capital of Texas?": ["Austin", "San Antonio", "Dallas", "Houston"],
            "Who was the first President of the United States?": ["George Washington", "Thomas Jefferson", "John Adams", "Abraham Lincoln"]
        },
        "Art": {
            "The Last Supper was painted by which artist?": ["Da Vinci", "Rembrandt", "Picasso", "Michelangelo"],
            "Starry Night was painted by which artist?": ["Van Gogh", "Monet", "Dali", "Kandinsky"]
        },
        "NBA Trivia": {
            "Which player has the most NBA championships?": ["Bill Russell", "Michael Jordan", "Kobe Bryant", "LeBron James"],
            "Who is the all-time leading scorer in NBA history?": ["Kareem Abdul-Jabbar", "Karl Malone", "LeBron James", "Michael Jordan"]
        }
    }

    print("Welcome to the Quiz Game!")
    score, total_questions = run_quiz(QUESTIONS)
    save_score_history("History", score, total_questions)

if __name__ == "__main__":
    main()

