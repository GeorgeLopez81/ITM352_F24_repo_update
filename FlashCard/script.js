// Select the form, flashcards container, and buttons
const form = document.getElementById("inputForm");
const flashcardsDiv = document.getElementById("flashcards");
const prevButton = document.getElementById("prev");
const nextButton = document.getElementById("next");

let flashcards = []; // Store all generated flashcards
let currentIndex = 0; // Track the current flashcard index

// Add an event listener for form submission
form.addEventListener("submit", async (e) => {
    e.preventDefault(); // Prevent default form submission behavior

    // Get input text
    const textInput = document.getElementById("subject").value;

    // Prepare form data to send to the backend
    const formData = new FormData();
    formData.append("subject", textInput);

    // Make the POST request to the Flask backend
    try {
        const response = await fetch("http://127.0.0.1:5000/generate_flashcards", {
            method: "POST",
            body: formData,
        });

        // Parse the JSON response
        const data = await response.json();

        // Load flashcards and display the first one
        if (data.flashcards && data.flashcards.length > 0) {
            flashcards = data.flashcards;
            currentIndex = 0;
            displayFlashcard(currentIndex);
        } else {
            flashcardsDiv.textContent = "No flashcards generated.";
        }
    } catch (error) {
        console.error("Error generating flashcards:", error);
        flashcardsDiv.textContent = "An error occurred while generating flashcards.";
    }
});

// Function to display a flashcard
function displayFlashcard(index) {
    flashcardsDiv.innerHTML = ""; // Clear previous content
    if (flashcards[index]) {
        const card = document.createElement("div");
        card.className = "flashcard";
        card.innerHTML = `
            <div class="flashcard-inner">
                <div class="flashcard-front">${flashcards[index].question}</div>
                <div class="flashcard-back">${flashcards[index].answer}</div>
            </div>
        `;
        flashcardsDiv.appendChild(card);
        addFlipEvent(card);
    } else {
        flashcardsDiv.textContent = "No flashcards to display.";
    }
}

// Add flip event to the flashcard
function addFlipEvent(card) {
    card.addEventListener("click", () => {
        card.classList.toggle("flipped");
    });
}

// Navigate between flashcards
prevButton.addEventListener("click", () => {
    if (currentIndex > 0) {
        currentIndex--;
        displayFlashcard(currentIndex);
    }
});

nextButton.addEventListener("click", () => {
    if (currentIndex < flashcards.length - 1) {
        currentIndex++;
        displayFlashcard(currentIndex);
    }
});
