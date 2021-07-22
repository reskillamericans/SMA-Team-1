document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("login-form");
    const email = document.getElementById("user_email");
    const pwd = document.getElementById("user_password");
    const login = document.getElementById("login");
    const loginBtn = document.getElementById("login-btn");
   
    
    form.addEventListener('input', function(e) {
        loginBtn.addEventListener('click', function(e) {
            e.preventDefault();
        });    
        if (email.validity.valid && pwd.validity.valid) {
            login.addEventListener('click', showSent);
        }
});
