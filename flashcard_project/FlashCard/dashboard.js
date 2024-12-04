let flashcards = []; // Flashcard deck
let currentCardIndex = 0;
let showingQuestion = true; // Track whether the question or answer is displayed

const flashcardContent = document.getElementById("flashcard-content");

// Fetch flashcards from the server (flashcards.json) when the page loads
function fetchFlashcards() {
    fetch("http://127.0.0.1:5000/get-flashcards")
        .then((response) => response.json())
        .then((data) => {
            flashcards = data; // Load flashcards into the array
            currentCardIndex = 0; // Start at the first flashcard
            displayFlashcard(currentCardIndex); // Display the first flashcard
        })
        .catch((error) => {
            console.error("Error fetching flashcards:", error);
            flashcardContent.innerHTML = "No flashcards available!";
        });
}

// Display the current flashcard (question by default)
function displayFlashcard(index) {
    if (flashcards.length > 0) {
        const card = flashcards[index];
        if (showingQuestion) {
            flashcardContent.innerHTML = card.question; // Display question
        } else {
            flashcardContent.innerHTML = card.answer; // Display answer
        }
    } else {
        flashcardContent.innerHTML = "No flashcards available!";
    }
}

// Handle "Previous" and "Next" buttons
document.getElementById("previous-button").addEventListener("click", () => {
    if (currentCardIndex > 0) {
        currentCardIndex--;
        showingQuestion = true; // Reset to show question
        displayFlashcard(currentCardIndex);
    }
});

document.getElementById("next-button").addEventListener("click", () => {
    if (currentCardIndex < flashcards.length - 1) {
        currentCardIndex++;
        showingQuestion = true; // Reset to show question
        displayFlashcard(currentCardIndex);
    }
});

// Handle "Flip" button
document.getElementById("flip-button").addEventListener("click", () => {
    showingQuestion = !showingQuestion; // Toggle between question and answer
    displayFlashcard(currentCardIndex);
});

// Modal functionality
const modal = document.getElementById("modal");
const manualInsertButton = document.getElementById("manual-insert-button");
const closeModal = document.getElementById("close-modal");

manualInsertButton.addEventListener("click", () => {
    modal.style.display = "flex";
});

closeModal.addEventListener("click", () => {
    modal.style.display = "none";
});

// Handle manual insertion
document.getElementById("manual-insert-form").addEventListener("submit", (e) => {
    e.preventDefault(); // Prevent form submission

    const question = document.getElementById("question-input").value;
    const answer = document.getElementById("answer-input").value;

    fetch("http://127.0.0.1:5000/insert-flashcard", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question, answer }),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.message === "Flashcard added successfully!") {
                alert("Flashcard added!");

                // Reload flashcards to include the newly added flashcard
                fetchFlashcards();

                // Hide the modal
                modal.style.display = "none";
            } else {
                alert(data.message);
            }
        })
        .catch((error) => {
            console.error("Error adding flashcard:", error);
        });
});

document.getElementById("quiz-button").addEventListener("click", () => {
    window.location.href = "quiz.html"; // Redirect to quiz page
});

// Fetch and display flashcards on page load
fetchFlashcards();
