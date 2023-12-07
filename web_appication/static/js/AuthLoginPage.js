const loginDiv = document.querySelector('#login');
const registerDiv = document.querySelector('#register');

function showRegisterForm() {
    loginDiv.style.display = "none";
    registerDiv.style.display = "block";
}

function showLoginForm() {
    loginDiv.style.display = "block";
    registerDiv.style.display = "none";
}

// Канвас частиц
window.onload = function () {
    window.sp = new SuperParticles({
        maxFps: 24,
        container: {
            element: "#particles-js"
        }
    });
};