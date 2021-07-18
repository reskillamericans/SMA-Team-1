document.addEventListener("DOMContentLoaded", () => {
    const main = document.getElementById("main");
    const BtnOne = document.getElementById('mainBtn');
    const emailPopUp = document.getElementById("emailSent");

    if (main.style.display ="block") {
        BtnOne.addEventListener('click', function(e) {
            e.preventDefault();
        });
        BtnOne.addEventListener('click', showEmail);
    }

    function showEmail() {
        main.style.display = "none";
        emailPopUp.style.display = "block"; 
    };
});

