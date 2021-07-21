document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("form");
    const email = document.getElementById("email");
    const main = document.getElementById("main");
    const BtnOne = document.getElementById('mainBtn');
    const emailPopUp = document.getElementById("emailSent");
    const BtnTwo = document.getElementById("emailBtnTwo");
    const reset = document.getElementById("reset");
    const BtnThree = document.getElementById("confirmBtnThree");
    const success = document.getElementById("successReset");
    const BtnFour = document.getElementById("successBtnFour");

    function isValidEmail(email) {
        const re =
          /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
      }


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
function isValidEmail(email) {
    const re =
      /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

// form.addEventListener('click', function (e) {
//     e.preventDefault();

    
// form.addEventListener('submit', function (e) {
//         e.preventDefault();

    
//     showEmail();

// });

// function showEmail() {
//     emailPopUp .style.display = "block"; 
//     main.style.display = "none";
//     // reset.style.display = "none";
//     // success.style.display = "none";
// };

// BtnOne.addEventListener('click', showEmail);
  
// form.addEventListener('submit', function (e) {
//     e.preventDefault();

