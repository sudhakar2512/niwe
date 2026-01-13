// detectPrivateMode.js

// Function to detect incognito/private mode
function checkPrivateMode() {
    // Ensure that detectIncognito() is available
    if (typeof detectIncognito !== 'function') {
        console.error("detectIncognito function is not loaded.");
        return;
    }

    detectIncognito()
        .then((result) => {

	    const isPrivateMode = result.isPrivate; 
            // If the browser is in private mode
            console.log('Private Mode:', isPrivateMode);
           
	    //if (isPrivateMode) {	
            document.cookie = "is_private_mode="+ isPrivateMode + "; path=/; Samesite=Strict;Secure;";
            // document.cookie = "is_private_mode="+ isPrivateMode + "; path=/; Samesite=Strict;";
	    //}
        })
        .catch((error) => {
            // If there is an error (likely that it's not supported or private mode is not detectable)
            console.error('Error detecting private mode:', error);
            document.cookie = 'is_private_mode=false; path=/; Samesite=Strict;Secure;';
        });
}

// Call the function when the script loads
checkPrivateMode();

