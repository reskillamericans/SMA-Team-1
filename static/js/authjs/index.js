// Landing Page JS
document.addEventListener("DOMContentLoaded", () => {

    // bg elements
    const bg = document.getElementById("bg");
    const popBg = document.getElementById("pop-up-bg");
    const BtnArrow = document.querySelector(".mobile-arrow");
    const LinkHome = document.getElementById("home");
    const LinkLoginPg = document.getElementById("login-pg");
    const LinkRegPg = document.getElementById("registration-pg");
    
    // landing page elements
    const landing = document.getElementById("landing-page");
    const lpSignup = document.getElementById("lp-signup-btn");
    const lpLogin = document.getElementById("lp-login-btn");
    const footer = document.getElementById("lp-footer");

    const BtnClose = document.querySelectorAll(".button-close");

    // registration page elements
    const register = document.getElementById("register");
    const regForm = document.getElementById("registration-form");
    const userName = document.getElementById("user_name");
    const email = document.getElementById("user_email");
    const pwd = document.getElementById("user_password");
    const optin = document.getElementById("optIn");
    const BtnOpt = document.getElementById('optBtn');
    const BtnCloseopt = document.getElementById('closeOptin');
    const BtnSignup = document.getElementById("sign-up");
    const BtnRegLogin = document.getElementById("already-btn");

    // Account Confirm elements
    const confirmAccount = document.getElementById("accountConfirmed");
    const BtnOK = document.getElementById("btn-ok");
    
    // Almost There Elements
    const almost = document.getElementById("almostThere");
    const almostForm = document.getElementById("almost-form");
    const BtnComplete = document.getElementById("acct-complete");
    const jobTitle = document.getElementById("job-title");
    const interests = document.getElementById("interests");


    // login page elements
    const login = document.getElementById("login");
    const logForm = document.getElementById("login-form");
    const currentPwd = document.getElementById("password");
    const currentEmail = document.getElementById("email");
    const BtnForgot = document.getElementById("log-forgot");
    const BtnLogin = document.getElementById("login-btn");
    const BtnRegister = document.getElementById("log-reg");
    const BtnRegisterDK = document.getElementById("log-reg-dk");
    

    //forgot password page elements
    const forgot = document.getElementById("forgot");
    const forgotForm = document.getElementById("forgot-form");
    const forgotEmail = document.getElementById("forgot_user_email");
    const BtnSend = document.getElementById("btn-send");

    //email sent popup elements
    const emailSent = document.getElementById("emailSent");
    const BtnEmailOK = document.getElementById("email-btn");

    // reset password page elements 
    const reset = document.getElementById("reset");
    const resetForm = document.getElementById("reset-form");
    const newPwd = document.getElementById("new_password");
    const confirmPwd = document.getElementById("conf_password");
    const BtnConfirmReset = document.getElementById("confirmBtn");

    // reset success popup elements
    const resetSuccess = document.getElementById("successReset");
    const BtnSuccessOK = document.getElementById("successOK");


    popBg.style.display = "none"; 
    register.style.display = "none";
    optin.style.display = "none";    
    BtnArrow.style.display = "none";
    confirmAccount.style.display = "none";
    almost.style.display = "none";
    login.style.display = "none";  
    BtnArrow.style.display = "none";
    forgot.style.display = "none"; 
    emailSent.style.display = "none";
    reset.style.display = "none"; 
    resetSuccess.style.display = "none";




    //Remove bg when screen is less than 500px
    function atWidth() {
        if (matchMedia('only screen and (max-width: 500px)').matches) { 
          popBg.style.display= "none";
        } else {
            popBg.style.display = "block";
        };
    };
      
    var screen = window.matchMedia("(max-width:500px)")
    // Call listener function at run time
    atWidth(screen) 
    // Attach listener function on state changes
    screen.addListener(atWidth) 
    

    function showRegister(){
        landing.style.display = "none";
        footer.style.display = "none"; 
        login.style.display = "none";  
        register.style.display = "block";
        optin.style.display = "none";   
        BtnArrow.style.display = "block";
        bg.style.display = "none";  
        popBg.style.display = "block";  
        popBg.style.opacity = ".2";
        confirmAccount.style.display = "none";
        almost.style.display = "none";
        emailSent.style.display = "none";
        forgot.style.display = "none";
        reset.style.display = "none"; 
        resetSuccess.style.display = "none"; 
        regForm.reset();
        atWidth();
    };
    
    // BACK TO LANDING PAGE
    function showLanding(){
        landing.style.display = "block";
        footer.style.display = "block"; 
        bg.style.display = "block";    
        register.style.display = "none";
        optin.style.display = "none";   
        almost.style.display = "none";
        BtnArrow.style.display = "none";  
        popBg.style.display = "none";
        confirmAccount.style.display = "none";
        emailSent.style.display = "none";
        login.style.display = "none";
        forgot.style.display = "none";
        reset.style.display = "none"; 
        resetSuccess.style.display = "none"; 
        atWidth(); 
        // resetForms();  
    };
    
    function showLogin(){
        landing.style.display = "none";
        footer.style.display = "none";  
        login.style.display = "block";
        register.style.display = "none";
        optin.style.display = "none";   
        reset.style.display = "none";  
        BtnArrow.style.display = "block";
        bg.style.display = "none";  
        popBg.style.display = "block";  
        popBg.style.opacity = ".2";
        almost.style.display = "none";
        confirmAccount.style.display = "none";
        emailSent.style.display = "none";
        resetSuccess.style.display = "none"; 
        forgot.style.display = "none";
        reset.style.display = "none";
        BtnLogin.style.backgroundColor = "#53B6E0";
        logForm.reset();
        atWidth(); 
    };
    
    // HEADER LINKS - SOME WILL CLEAR FORM
    // Link to landing page
    LinkHome.addEventListener('click', function(e) {
        e.preventDefault();
    }); 
    LinkHome.addEventListener('click', showLanding);
    

    // Link to login page will clear the login form
    LinkLoginPg.addEventListener('click', function(e) {
        e.preventDefault();
        BtnLogin.style.backgroundColor = "#53B6E0"
       
    }); 
    LinkLoginPg.addEventListener('click', showLogin);
    

    // Link to register page will clear the reg form 
    LinkRegPg.addEventListener('click', function(e) {
        e.preventDefault();
    }); 
    LinkRegPg.addEventListener('click', showRegister);
    
    


    // Landing Page to Registration when "Sign up is Selected"
    lpSignup.addEventListener('click', function(e) {
        e.preventDefault();
    }); 
    lpSignup.addEventListener('click', showRegister);


    lpLogin.addEventListener('click', function(e) {
        e.preventDefault();
       
    }); 
    lpLogin.addEventListener('click', showLogin);


    // Returning to Landing Page from any mobile screen
    BtnArrow.addEventListener('click', showLanding);
    
    // Close Popups and Return to Landing Page
    Array.from(BtnClose).forEach(function(BtnClose) {
        BtnClose.addEventListener('click', showLanding);
    }); 
   

    // REGISTRATION OPT-IN
    // BtnOpt.addEventListener('click', showOptin);
    // function showOptin(){
    //     optin.style.display = "block"; 
    //     atWidth();     
    // };

    // BtnCloseopt.addEventListener('click', hideOptin);
    // function hideOptin(){
    //     optin.style.display = "none"; 
    //     atWidth();  
    // };
    
    // Link on reg form will clear login form of data
    BtnRegLogin.addEventListener('click', function(e) {
        e.preventDefault();
        BtnLogin.style.backgroundColor = "#53B6E0";
    });
    BtnRegLogin.addEventListener('click', showLogin);


    // ACCOUNT SUCCESS ON SUBMISSION OF REGISTRATION FORM
    // regForm.addEventListener('input', function(e) {
    //     BtnSignup.addEventListener('click', function(e) {
    //         e.preventDefault();
    //     });
    //     BtnSignup.addEventListener('click', Registration); 
    // });
    
    function Registration() {
        if(register.style.display = "block") {
            checkRegistration();
        };
    };
    function checkRegistration() {
        if(userName.value !== '' && email.validity.valid && pwd.validity.valid ) {
            showConfirmed();
        };
    };
    
    BtnSignup.addEventListener('click', showConfirmed);


    // Account confirm popup
    function showConfirmed(){
        register.style.display = "none";
        footer.style.display = "none"; 
        bg.style.display = "none";  
        confirmAccount.style.display = "block";
        atWidth();  
    };

    // ALMOST THERE POPUP ON BTN CLICK
    function showAlmost(){
        confirmAccount.style.display = "none"; 
        almost.style.display = "block"
        bg.style.display = "none"; 
        atWidth();  
    };

    BtnOK.addEventListener('click', function(e) {
        e.preventDefault();
        if(almost.style.display = "block") {
            almostForm.reset();
            BtnComplete.style.backgroundColor = "#53B6E0";
        }; 
    });
    BtnOK.addEventListener('click', showAlmost);
    

    // GO TO LOGIN ON SUBMISSION OF ALMOST THERE FORM
    almostForm.addEventListener('input', function(e) {
        BtnComplete.addEventListener('click', function(e) {
            e.preventDefault();
            
        }); 
        BtnComplete.addEventListener('click', AlmostThere)
    });

    function AlmostThere() {
        if(almost.style.display = "block") {
            checkAlmost();
        };
    };
    function checkAlmost() {
        if(jobTitle.value !== "" && interests.value !== "") {
            BtnComplete.style.backgroundColor = "#74C080";
        };
    };


    // Change color of button on completion of login form
    // logForm.addEventListener('input', function(e) {
    //     BtnLogin.addEventListener('click', function(e) {
    //         e.preventDefault();
    //     }); 
    //     BtnLogin.addEventListener('click', LoginNow); 
    // });

    function LoginNow() {
        if(login.style.display = "block") {
            checkLogin();
        };
    };
    
    function checkLogin() {
        if( currentPwd.value !== "" && currentEmail.value !== "") {
            changeBtn();
        } else {
            BtnLogin.style.backgroundColor = "#53B6E0";
        };
    };
    function changeBtn() {
        BtnLogin.style.backgroundColor =" #74C080";
    }

    // LINKS TO REGISTER ON REG FORM OF PREVIOUS DATA
    // On login page, user selects "Register" on Desktop
    BtnRegisterDK.addEventListener('click', function(e) {
            e.preventDefault();
            
    }); 
    BtnRegisterDK.addEventListener('click', showRegister);
  

    // On login page, user selects "Register" on Mobile
    BtnRegister.addEventListener('click', function(e) {
        e.preventDefault();
    }); 
    BtnRegister.addEventListener('click', showRegister);
    
    
    // On login page, user selects "Forgot" password
    function showForgot(){
        login.style.display = "none";
        forgot.style.display = "block"; 
        bg.style.display = "none";
        atWidth();  
    };

    BtnForgot.addEventListener('click', function(e) {
        e.preventDefault();
        if(forgot.style.display = "block") {
            forgotForm.reset();
        };
    }); 
    BtnForgot.addEventListener('click', showForgot);

    // GO TO EMAIL SENT  ON SUBMISSION OF EMAIL
    forgotForm.addEventListener('input', function(e) {
        BtnSend.addEventListener('click', function(e) {
            e.preventDefault();
        });
        BtnSend.addEventListener('click', ForgotPass); 
    });   
    function ForgotPass() {
        if(forgot.style.display ="block") {
            checkForgotEmail();
        };
    };
    function checkForgotEmail() {
        if (forgotEmail.validity.valid && forgotEmail.value !== '') {
            showSent();
        };
    }; 
    // After user supplies email, confirmation of email being sent
    function showSent() {
        forgot.style.display = "none";
        emailSent.style.display = "block";
        bg.style.display = "none"; 
        atWidth();  
    };


    // After selecting OK, user goes to password reset * JUST A TEST SCENARIO *
    // to include Reset Page, otherwise it should populate once the user responds to the email
   
    function showReset() {
        resetForm.reset();
        emailSent.style.display = "none";
        reset.style.display = "block";
        bg.style.display = "none"; 
        atWidth();  
    }
    BtnEmailOK.addEventListener('click', function(e) {
        e.preventDefault();
    }); 
    
    BtnEmailOK.addEventListener('click', showReset);


    // Reset form checks that passwords match, if so success if confirmed
    resetForm.addEventListener('input', function(e) {
        BtnConfirmReset.addEventListener('click', function(e) {
            e.preventDefault();
        }); 
        BtnConfirmReset.addEventListener('click', ResetPass);
        
    });
    function ResetPass() {
        if(reset.style.display = "block") {
            checkResetPass();
        };
    };
    function checkResetPass() {
        if (confirmPwd.value == newPwd.value && confirmPwd.value !== '' && newPwd.value !== '') {
            showSuccess();
        };
    };

    function showSuccess() {
        reset.style.display = "none";
        resetSuccess.style.display = "block";
        bg.style.display = "none";
        atWidth();   
    };
    BtnSuccessOK.addEventListener('click', function(e) {
        e.preventDefault();
    });
    BtnSuccessOK.addEventListener('click', showLogin);
});