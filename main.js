var gfg = document.getElementById("fname");
        gfg.onchange = function (e) {
            if (gfg.value != '') {
                e.target.style.border
                        = "4px dotted red";
            }
        };