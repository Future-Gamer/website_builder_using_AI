// --------------------------------------------- Login Page JS ------------------------------------------------------

document.addEventListener("DOMContentLoaded", function () {
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const emailLoginBtn = document.getElementById("email-login");

    // Validate email function
    function validateEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }

    // Handle email login
    emailLoginBtn.addEventListener("click", function () {
        if (!validateEmail(emailInput.value)) {
            alert("Please enter a valid email.");
            return;
        }

        if (passwordInput.value === "") {
            alert("Please enter your password.");
            return;
        }

        alert("Login successful!");
        // You can send this data to a backend API here
    });

    // Social Login Buttons
    document.querySelector(".google").addEventListener("click", function () {
        window.location.href = "https://accounts.google.com/signin";
    });

    document.querySelector(".facebook").addEventListener("click", function () {
        window.location.href = "https://www.facebook.com/login/";
    });

    document.querySelector(".apple").addEventListener("click", function () {
        window.location.href = "https://appleid.apple.com/auth/authorize";
    });
});

// --------------------------------------------------------- ------------------------------

// JavaScript to handle expanding the message box and maintaining its state

const messageBox = document.getElementById('messageBox');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');

// Expand the message box when clicked
messageInput.addEventListener('focus', function () {
    messageBox.classList.add('expanded');
});

// Keep the message box expanded after sending the message
sendButton.addEventListener('click', function (event) {
    event.preventDefault(); // Prevent the default form submission behavior

    if (messageInput.value.trim() !== "") {
        // Simulate sending the message (this can be replaced with actual send logic)
        console.log("Message sent: " + messageInput.value);

        // Clear the textarea, but keep the message box expanded
        messageInput.value = "";
        messageBox.classList.add('expanded');
    }
