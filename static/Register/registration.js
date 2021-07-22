document.addEventListener("DOMContentLoaded", () => {
    const register = document.getElementById("register");
    const confirmAccount = document.getElementById("accountConfirmed");
    const form = document.getElementById("registration-form");
    const userName = document.getElementById("user_name");
    const email = document.getElementById("user_email");
    const pwd = document.getElementById("user_password");
    const optin = document.getElementById("optIn");
    const BtnOpt = document.getElementById('optBtn');
    const BtnClose = document.getElementById('closeOptin');
    const BtnSignup = document.getElementById("sign-up");


    confirmAccount.style.display ="none";

    
    BtnOpt.addEventListener('click', showOptin);
    function showOptin(){
        optin.style.display = "block";    
    };

    BtnClose.addEventListener('click', hideOptin);
    function hideOptin(){
        optin.style.display = "none"; 
    };

    function showConfirmed(){
        register.style.display = "none";
        confirmAccount.style.display = "block";
    };
    

    form.addEventListener('input', function(e) {
        BtnSignup.addEventListener('click', function(e) {
            e.preventDefault();
        }); 
        if(userName.value !== "" && email.validity.valid && pwd.validity.valid) {
            BtnSignup.addEventListener('click', showConfirmed);  
        };
    });

    
    
});    