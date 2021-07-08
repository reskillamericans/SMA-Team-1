
//  Add email and password to an object when submitted

var objects = {};
var form = document.getElementById('form');
form.onsubmit = function(e){
    var item = document.getElementById('item').value, email =document.getElementById('email').value, password = document.getElementById('password').value;
    objects[item] = {'email':email, 'password':password}
    console.log(JSON.stringify(objects));
    e.preventDefault();
}

//Script for Forgot/Reset password - has error...run correctly only after clicking X in corner 
document.addEventListener("DOMContentLoaded", () => {
    const main = document.getElementById("main");
    const BtnOne = document.getElementById('mainBtn');
    const email = document.getElementById("emailSent");
    const BtnTwo = document.getElementById("emailBtnTwo");
    const reset = document.getElementById("reset");
    const BtnThree = document.getElementById("confirmBtnThree");
    const success = document.getElementById("successReset");
    const BtnFour = document.getElementById("successBtnFour");

    email.style.display = "none"; 
    reset.style.display = "none";
    success.style.display = "none";
    main.style.display = "block";
    
    BtnOne.addEventListener('click', showEmail);
    BtnTwo.addEventListener('click', showReset);
    BtnThree.addEventListener('click', showSuccess);
    BtnFour.addEventListener('click', showHome);
    
    function showEmail() {
        main.style.display = "none";
        reset.style.display = "none";
        success.style.display = "none";
        email.style.display = "block"; 
    };
    function showReset() {
        email.style.display = "none";
        main.style.display = "none";
        success.style.display = "none";
        reset.style.display = "block";
    };
    function showSuccess() {
        email.style.display = "none";
        main.style.display = "none";
        reset.style.display = "none";
        success.style.display = "block";
    };
    function showHome() {
        reset.style.display = "none";
        email.style.display = "none";
        success.style.display = "none";
        main.style.display = "block";
    };
});