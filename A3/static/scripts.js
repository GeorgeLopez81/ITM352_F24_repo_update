let currentQuestionIndex = 0;
let score = 0;
let questions = []; // Questions will be loaded dynamically

// Function to load questions from the backend
function loadQuestions() {
    fetch('/api/questions') // Fetch questions from the Flask API
        .then((response) => response.json())
        .then((data) => {
            questions = data;
            displayQuestion();
        })
        .catch((error) => {
            console.error("Failed to load questions:", error);
            alert("Failed to load questions. Please try again later.");
        });
}

// Function to display the current question
function displayQuestion() {
    if (currentQuestionIndex < questions.length) {
        const questionData = questions[currentQuestionIndex];

        // Set question text
        document.getElementById('question-text').innerText = questionData.question;

        // Generate answer options
        const optionsContainer = document.getElementById('options-container');
        optionsContainer.innerHTML = ''; // Clear previous options
        questionData.options.forEach((option) => {
            const optionElement = document.createElement('label');
            optionElement.innerHTML = `
                <input type="radio" name="answer" value="${option}" />
                ${option}
            `;
            optionsContainer.appendChild(optionElement);
        });

        // Clear feedback for the new question
        const feedback = document.getElementById('feedback');
        feedback.innerText = '';
        feedback.className = '';
    } else {
        showResults();
    }
}

// Function to handle answer submission
function submitAnswer() {
    const selectedOption = document.querySelector('input[name="answer"]:checked');
    if (!selectedOption) {
        alert("Please select an answer!");
        return;
    }

    const userAnswer = selectedOption.value;
    const correctAnswer = questions[currentQuestionIndex].correct;

    const feedback = document.getElementById('feedback');
    if (userAnswer === correctAnswer) {
        feedback.innerText = "Correct!";
        feedback.className = "correct";
        score++;
    } else {
        feedback.innerText = `Incorrect! The correct answer was: ${correctAnswer}`;
        feedback.className = "incorrect";
    }

    // Disable further input to avoid double submissions
    document.querySelectorAll('input[name="answer"]').forEach(input => input.disabled = true);

    // Wait 2 seconds, then move to the next question or show results
    setTimeout(() => {
        currentQuestionIndex++;
        if (currentQuestionIndex < questions.length) {
            displayQuestion();
        } else {
            showResults();
        }
    }, 2000); // 2-second delay for feedback
}

// Function to show final results
function showResults() {
    // Save the score to the backend
    fetch('/api/save_score', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ score: score })
    }).then(() => {
        // Redirect to the home page after saving the score
        window.location.href = '/';
    }).catch((error) => {
        console.error("Failed to save score:", error);
        alert("Failed to save your score. Please try again.");
    });
}

// Function to restart the quiz
function restartQuiz() {
    currentQuestionIndex = 0;
    score = 0;
    loadQuestions();
}

// Initialize the quiz
document.addEventListener('DOMContentLoaded', () => {
    loadQuestions();
});