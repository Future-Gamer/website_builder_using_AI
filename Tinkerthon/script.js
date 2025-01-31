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
