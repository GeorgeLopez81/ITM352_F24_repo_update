let flashcards = []; // Flashcard deck
let currentCardIndex = 0;
let showingQuestion = true; // Track whether the question or answer is displayed

// Load progress from localStorage or set to 0
let progress = JSON.parse(localStorage.getItem("progress")) || { reviewed: 0 };

// Update the progress display
document.getElementById("progress-report").innerText = `Cards Reviewed: ${progress.reviewed}`;

const flashcardContent = document.getElementById("flashcard-content");
const flashcardAnswer = document.getElementById("flashcard-answer");
const flashcard = document.querySelector(".flashcard");

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

// Display the current flashcard
function displayFlashcard(index) {
    if (flashcards.length > 0) {
        const card = flashcards[index];
        flashcardContent.innerHTML = card.question; // Display question
        flashcardAnswer.innerHTML = card.answer;    // Display answer
        flashcard.classList.remove("flipped");      // Ensure the card shows the question by default
    } else {
        flashcardContent.innerHTML = "No flashcards available!";
    }
}

// Handle "Previous" and "Next" buttons
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
        updateProgress();
    }
});

// Handle "Flip" button for the flip animation
document.getElementById("flip-button").addEventListener("click", () => {
    flashcard.classList.toggle("flipped");
});

// Modal elements
const manualInsertModal = document.getElementById("manual-insert-modal");
const manualInsertButton = document.getElementById("manual-insert-button");
const closeManualModal = document.getElementById("close-manual-modal");

// Show the manual insert modal
manualInsertButton.addEventListener("click", () => {
    manualInsertModal.style.display = "flex";
});

// Close the manual insert modal
closeManualModal.addEventListener("click", () => {
    manualInsertModal.style.display = "none";
});

document.getElementById("quiz-button").addEventListener("click", () => {
    window.location.href = "quiz.html";
});


// Handle manual insertion form submission
document.getElementById("manual-insert-form").addEventListener("submit", (e) => {
    e.preventDefault();

    const question = document.getElementById("manual-question").value.trim();
    const answer = document.getElementById("manual-answer").value.trim();

    if (question && answer) {
        fetch("http://127.0.0.1:5000/insert-flashcard", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question, answer, subject: "Manual" }),
        })
            .then((response) => response.json())
            .then((data) => {
                alert(data.message);
                fetchFlashcards(); // Refresh the flashcards
                manualInsertModal.style.display = "none";
                document.getElementById("manual-insert-form").reset();
            })
            .catch((error) => {
                console.error("Error adding flashcard:", error);
            });
    }
});

// Update progress function
function updateProgress() {
    progress.reviewed += 1;
    localStorage.setItem("progress", JSON.stringify(progress));
    document.getElementById("progress-report").innerText = `Cards Reviewed: ${progress.reviewed}`;
}

// Reset progress function
function resetProgress() {
    progress.reviewed = 0;
    localStorage.setItem("progress", JSON.stringify(progress));
    document.getElementById("progress-report").innerText = `Cards Reviewed: ${progress.reviewed}`;
}

// Fetch and display flashcards on page load
fetchFlashcards();
document.getElementById("quiz-history-button").addEventListener("click", () => {
    const username = localStorage.getItem("currentUsername") || "Guest";

    fetch(`http://127.0.0.1:5000/generate-scatter-plot?username=${username}`)
        .then((response) => {
            if (!response.ok) {
                throw new Error("Failed to generate scatter plot");
            }
            return response.blob(); // Get the image as a blob
        })
        .then((blob) => {
            const imgUrl = URL.createObjectURL(blob);
            const scatterPlot = document.getElementById("scatter-plot");
            scatterPlot.src = imgUrl;

            const scatterPlotContainer = document.getElementById("scatter-plot-container");
            scatterPlotContainer.style.display = "block";
        })
        .catch((error) => {
            console.error("Error fetching scatter plot:", error);
            alert("Unable to generate scatter plot. Please try again later.");
        });
});



// Handle closing the scatter plot
document.getElementById("close-plot-button").addEventListener("click", () => {
    const scatterPlotContainer = document.getElementById("scatter-plot-container");
    scatterPlotContainer.style.display = "none"; // Hide the scatter plot container
});

