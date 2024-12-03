// Register functionality
document.getElementById("register-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const username = document.getElementById("register-username").value;
    const password = document.getElementById("register-password").value;

    fetch("http://127.0.0.1:5000/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.message === "Registration successful!") {
                alert("Thank you for registering! Use your new username and password to begin.");
            } else {
                alert(data.message);
            }
        })
        .catch((error) => {
            console.error("Error during registration:", error);
            alert("An error occurred. Please try again.");
        });
});

// Login functionality
document.getElementById("login-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;

    fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.message === "Login successful!") {
                alert("Login successful! Redirecting...");
                window.location.href = "dashboard.html"; // Redirect to the dashboard
            } else {
                alert(data.message);
            }
        })
        .catch((error) => {
            console.error("Error during login:", error);
            alert("An error occurred. Please try again.");
        });
});
