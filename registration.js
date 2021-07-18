document.addEventListener("DOMContentLoaded", () => {
    const register = document.getElementById("register");
    const regSuccess = document.getElementById("accountConfirmed");

    const optin = document.getElementById("optIn");
    const BtnOpt = document.getElementById('optBtn');
    const BtnClose = document.getElementById('closeOptin');
    const BtnSignup = document.getElementById("sign-up");

    regSuccess.style.display ="none";

    BtnOpt.addEventListener('click', showOptin);
    BtnClose.addEventListener('click', hideOptin);
    BtnSignup.addEventListener('click', showConfirmed);

    if (regSuccess.style.display ="none") {
        BtnSignup.addEventListener('click', function(e) {
        e.preventDefault();
    });
        BtnSignup.addEventListener('click', showConfirmed);
    };

    function showOptin(){
        optin.style.display = "block";    
    };
    function hideOptin(){
        optin.style.display = "none"; 
    };
    function showConfirmed(){
        register.style.display = "none";
        regSuccess.style.display = "block";
    };
});
