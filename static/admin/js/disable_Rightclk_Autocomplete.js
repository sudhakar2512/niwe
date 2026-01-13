
// Code for disabling right click
if(window.location.pathname.startsWith('/admin/')){
    document.addEventListener("DOMContentLoaded",function()
    {
        document.addEventListener('contextmenu',function(event)
        {
            event.preventDefault();            
        });
    });
}

// Code for disabling autocomplete off

document.addEventListener("DOMContentLoaded", function () {
    const usernameField    = document.getElementById("id_username");
    const passwordField    = document.getElementById("id_password");
    const OneTimePSWField  = document.getElementById("id_otp_token");
    
    if (usernameField) {
        usernameField.setAttribute("autocomplete", "off");
    }

    if (passwordField) {
        passwordField.setAttribute("autocomplete", "off");
    }

    if (OneTimePSWField) {
        OneTimePSWField.setAttribute("autocomplete", "off");
    }


});
