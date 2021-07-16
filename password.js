document.addEventListener("DOMContentLoaded", () => {
    const main = document.getElementById("main");
    const BtnOne = document.getElementById('mainBtn');
    const emailPopUp = document.getElementById("emailSent");
    const BtnTwo = document.getElementById("emailBtnTwo");
    const reset = document.getElementById("reset");
    const BtnThree = document.getElementById("confirmBtnThree");
    const success = document.getElementById("successReset");
    



    if (main.style.display ="block") {
        BtnOne.addEventListener('click', function(e) {
            e.preventDefault();
        });
        BtnOne.addEventListener('click', showEmail);
    }
    if (emailPopUp.style.display ="none") {
        BtnTwo.addEventListener('click', function(e) {
            e.preventDefault();
        });
        BtnTwo.addEventListener('click', showReset);
    } 
    if (reset.style.display ="none") {
        BtnThree.addEventListener('click', function(e) {
            e.preventDefault();
        });
        BtnThree.addEventListener('click', showSuccess);
    };


    function showEmail() {
        main.style.display = "none";
        reset.style.display = "none";
        success.style.display = "none";
        emailPopUp.style.display = "block"; 
    };
    function showReset() {
        emailPopUp .style.display = "none";
        main.style.display = "none";
        success.style.display = "none";
        reset.style.display = "block";
    };
    function showSuccess() {
        emailPopUp .style.display = "none";
        main.style.display = "none";
        reset.style.display = "none";
        success.style.display = "block";
    };

});

