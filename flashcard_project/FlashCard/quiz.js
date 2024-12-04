// Fetch flashcards from the server
let flashcards = []; // Store flashcards globally for access
fetch("http://127.0.0.1:5000/get-flashcards")
    .then((response) => response.json())
    .then((data) => {
        flashcards = data;
        displayQuiz(flashcards);
    })
    .catch((error) => {
        console.error("Error fetching flashcards:", error);
    });

// Generate multiple-choice answers
function generateChoices(correctAnswer, flashcards) {
    const choices = new Set();
    choices.add(correctAnswer); // Ensure the correct answer is included

    // Generate plausible incorrect answers from other flashcards
    while (choices.size < 4) {
        const randomAnswer = flashcards[Math.floor(Math.random() * flashcards.length)].answer;
        choices.add(randomAnswer);
    }

    return Array.from(choices).sort(() => Math.random() - 0.5); // Shuffle the choices
}

// Display the quiz
function displayQuiz(flashcards) {
    const quizContainer = document.getElementById("quiz-container");

    flashcards.forEach((card, index) => {
        const questionDiv = document.createElement("div");
        questionDiv.classList.add("quiz-question");

        const questionText = document.createElement("h3");
        questionText.textContent = `Q${index + 1}: ${card.question}`;
        questionDiv.appendChild(questionText);

        const choices = generateChoices(card.answer, flashcards);

        choices.forEach((choice) => {
            const label = document.createElement("label");
            label.textContent = choice;

            const radioButton = document.createElement("input");
            radioButton.type = "radio";
            radioButton.name = `question-${index}`;
            radioButton.value = choice;

            label.prepend(radioButton);
            questionDiv.appendChild(label);
            questionDiv.appendChild(document.createElement("br")); // Line break for formatting
        });

        quizContainer.appendChild(questionDiv);
    });
}

// Handle quiz submission
document.getElementById("submit-button").addEventListener("click", () => {
    let correctCount = 0;

    flashcards.forEach((card, index) => {
        const selectedOption = document.querySelector(`input[name="question-${index}"]:checked`);
        if (selectedOption && selectedOption.value === card.answer) {
            correctCount++;
        }
    });

    // Calculate the percentage
    const totalQuestions = flashcards.length;
    const percentage = Math.round((correctCount / totalQuestions) * 100);

    // Display results
    alert(`You got ${correctCount} out of ${totalQuestions} correct (${percentage}%).`);
});
