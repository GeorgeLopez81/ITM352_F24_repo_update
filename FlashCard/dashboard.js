const flashcards = []; // Flashcard deck
let currentCardIndex = 0;

const flashcardQuestion = document.getElementById("flashcard-question");
const flashcardList = document.querySelector(".flashcard ul");

// Display flashcard
function displayFlashcard(index) {
    if (flashcards.length > 0) {
        const card = flashcards[index];
        flashcardQuestion.innerHTML = card.question;
        flashcardList.innerHTML = `<li>${card.answer}</li>`;
    } else {
        flashcardQuestion.innerHTML = "No flashcards available!";
        flashcardList.innerHTML = "";
    }
}

// Handle Previous and Next buttons
document.getElementById("previous-button").addEventListener("click", () => {
    if (currentCardIndex > 0) {
        currentCardIndex--;
        displayFlashcard(currentCardIndex);
    }
});

document.getElementById("next-button").addEventListener("click", () => {
    if (currentCardIndex < flashcards.length - 1) {
        currentCardIndex++;
        displayFlashcard(currentCardIndex);
    }
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
    e.preventDefault();
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
                flashcards.push({ question, answer });
                alert("Flashcard added!");
                modal.style.display = "none";
                displayFlashcard(currentCardIndex);
            }
        })
        .catch((error) => {
            console.error("Error adding flashcard:", error);
        });
});

// Initial display
displayFlashcard(currentCardIndex);
