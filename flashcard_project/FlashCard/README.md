# Flashcard Generator Application

This is a web-based Flashcard Generator designed to help users create, manage, and study flashcards interactively. The application supports user registration, login, flashcard creation, editing, quiz-taking, and progress tracking.

---

## 📋 **Features**

### 1. **User Authentication**
   - **Register:** Create a new account with a username and password.
   - **Login:** Access the dashboard by logging in with your credentials.
   - **Logout:** Log out to return to the login page.

### 2. **Flashcard Management**
   - **Create Flashcards:** Upload a file to automatically generate flashcards or manually insert flashcards.
   - **Edit Flashcards:** Modify the question and answer of existing flashcards.
   - **Shuffle Flashcards:** Randomize the order of the flashcards.
   - **Flip Flashcards:** Interactive flip animation to reveal the answer.
   - **Navigation:** Move between flashcards using the "Next" and "Previous" buttons.

### 3. **Quiz Feature**
   - Take a quiz based on your flashcards.
   - Multiple-choice questions are generated automatically.
   - View your quiz score after submission.

### 4. **Progress Tracking**
   - **Track Reviewed Cards:** See how many cards you have reviewed.
   - **Reset Progress:** Restart your flashcard review session.
   - **Quiz History:** View a scatter plot of your quiz scores over time.

### 5. **Scatter Plot Visualization**
   - Visualize quiz performance with a scatter plot.
   - Track scores over time for each user.

---

## 🛠️ **Technologies Used**

- **Frontend:**
  - HTML, CSS, JavaScript
- **Backend:**
  - Python (Flask)
  - SQLite (Database)
- **Libraries:**
  - `pandas` - For handling quiz results data.
  - `matplotlib` - For generating scatter plots.
  - `openai` - For generating Q&A pairs from uploaded files.
  - `Flask-CORS` - To handle cross-origin requests.

---

## 🚀 **Installation and Setup**

### **Prerequisites**

1. **Python** (version 3.7 or higher)
2. **Node.js** (optional for frontend development)
3. **Dependencies** listed in `requirements.txt`

### **Clone the Repository**

```bash
git clone https://github.com/yourusername/flashcard-generator.git
cd flashcard-generator
