document.addEventListener("DOMContentLoaded", () => {
    const forgot = document.getElementById("forgot");
    const closeForgotbtn =document.getElementById("forgotClose");
    const backgroundImg = document.getElementById("img-bg");
    const email = document.getElementById("user_email");
    const emailSentbtn = document.getElementById("btn-send");
    const emailPopup = document.getElementById("emailSent");

    
    email.addEventListener('input', function(e) {
        emailSentbtn.addEventListener('click', function(e) {
            e.preventDefault();
        });    
        if (email.validity.valid) {
            emailSentbtn.addEventListener('click', showSent);
        };
    });
    
    function showSent() {
        forgot.style.display = "none";
        emailPopup.style.display = "block";
    }

});
