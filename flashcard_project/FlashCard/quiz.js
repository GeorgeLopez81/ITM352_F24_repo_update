// Fetch flashcards from the server
let flashcards = []; // Store flashcards globally for access
const quizContainer = document.getElementById("quiz-container");

// Get the username from localStorage and set the hidden field
const username = localStorage.getItem("currentUsername") || "Guest";
document.getElementById("username").value = username;

// Fetch the flashcards and display the quiz
fetch("http://127.0.0.1:5000/get-flashcards")
    .then((response) => {
        if (!response.ok) {
            throw new Error("Failed to fetch flashcards");
        }
        return response.json();
    })
    .then((data) => {
        flashcards = data;
        displayQuiz(flashcards);
    })
    .catch((error) => {
        console.error("Error fetching flashcards:", error);
        quizContainer.innerHTML = "<p>Unable to load quiz questions. Please try again later.</p>";
    });

// Function to generate multiple-choice answers
function generateChoices(correctAnswer, flashcards) {
    const choices = new Set();
    choices.add(correctAnswer); // Ensure the correct answer is included

    while (choices.size < 4) {
        const randomAnswer = flashcards[Math.floor(Math.random() * flashcards.length)].answer;
        choices.add(randomAnswer);
    }

    return Array.from(choices).sort(() => Math.random() - 0.5); // Shuffle the choices
}

// Function to display the quiz
function displayQuiz(flashcards) {
    quizContainer.innerHTML = ""; // Clear any existing content

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

    const totalQuestions = flashcards.length;
    const percentage = Math.round((correctCount / totalQuestions) * 100);
    const username = document.getElementById("username").value;

    // Save results with username
    fetch("http://127.0.0.1:5000/save-quiz-results", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, percentage, date: new Date().toISOString() }),
    })
    .then((response) => response.json())
    .then((data) => {
        alert(`You scored ${percentage}%!`);
    })
    .catch((error) => {
        console.error("Error saving quiz results:", error);
    });
});
