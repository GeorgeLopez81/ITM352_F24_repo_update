// Placeholder for Flashcard Interaction
let currentCardIndex = 0;
const flashcards = [
    { question: "Did my dog eat my homework?", options: ["Yes", "No", "Your cat ate it", "Your mom ate it"] },
    { question: "What is 2 + 2?", options: ["3", "4", "5", "6"] },
];

const flashcardQuestion = document.getElementById("flashcard-question");

// Update flashcard display
function displayFlashcard(index) {
    const card = flashcards[index];
    flashcardQuestion.innerHTML = card.question;
    const options = card.options
        .map((opt, i) => `<li>${String.fromCharCode(65 + i)}) ${opt}</li>`)
        .join("");
    document.querySelector(".flashcard ul").innerHTML = options;
}

// Event listeners for buttons
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

document.getElementById("generate-button").addEventListener("click", () => {
    alert("Generate flashcards functionality will be implemented!");
});

// Initial flashcard display
displayFlashcard(currentCardIndex);
