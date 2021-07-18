document.addEventListener("DOMContentLoaded", () => {
    const reset = document.getElementById("reset");
    const BtnThree = document.getElementById("confirmBtnThree");
    const success = document.getElementById("successReset");
    
    if (reset.style.display ="block") {
        BtnThree.addEventListener('click', function(e) {
            e.preventDefault();
        });
        BtnThree.addEventListener('click', showSuccess);
    };

    function showSuccess() {
        reset.style.display = "none";
        success.style.display = "block";
    };

});

