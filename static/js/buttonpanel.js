
// Function to toggle the visibility of FAQ panels
function toggleAnswer(panelId) {
  const panel = document.getElementById(panelId);
  const button = document.getElementById("panel-button-" + panelId.replace('panel', ''));

  // Toggle visibility of the panel
  if (panel.classList.contains("d-none")) {
    panel.classList.remove("d-none");
    // Update the aria-expanded attribute for accessibility
    button.setAttribute("aria-expanded", "true");
  } else {
    panel.classList.add("d-none");
    // Update the aria-expanded attribute for accessibility
    button.setAttribute("aria-expanded", "false");
  }
}

// Add event listeners to the buttons
// document.addEventListener('DOMContentLoaded', function () {
//   // Add event listeners for each FAQ button
//   const buttons = document.querySelectorAll('.faq__question');
//   buttons.forEach(function(button) {
//     button.addEventListener('click', function() {
//       const panelId = this.getAttribute('aria-controls');
//       toggleAnswer(panelId);
//     });
//   });

//   // Add event listeners for all external links
//   const externalLinks = document.querySelectorAll('.external-link');
//   externalLinks.forEach(function(link) {
//     link.addEventListener('click', function(event) {
//       confirmExternalLink(event);  // Handle confirmation before navigating
//     });
//   });
// });


document.addEventListener('DOMContentLoaded', function () {
  // Add event listeners for each FAQ button
  const buttons = document.querySelectorAll('.faq__question');
  buttons.forEach(function(button) {
    button.addEventListener('click', function() {
      const panelId = this.getAttribute('aria-controls');
      toggleAnswer(panelId);
    });
  });

  // Add event listeners for all external links
  // const externalLinks = document.querySelectorAll('.external-link');
  // externalLinks.forEach(function(link) {
  //   link.addEventListener('click', function(event) {
  //     confirmExternalLink(event);  // Handle confirmation before navigating
  //   });
  // });

  // Add confirmation for external links within TinyMCE content
  // document.body.addEventListener('click', function(event) {
  //   const target = event.target.closest('a');

  //   if (target && target.href) {
  //     const currentHost = window.location.hostname;
  //     const linkHost = new URL(target.href).hostname;

  //     // Show confirmation for external links
  //     if (linkHost !== currentHost) {
  //       event.preventDefault();
  //       const userConfirmed = confirm("You are being redirected to external website. Do you want to continue?");
        
  //       if (userConfirmed) {
  //         window.open(target.href, '_blank');
  //       }
  //     }
  //   }
  // });

  document.body.addEventListener('click', function(event) {
    const target = event.target.closest('a');

    if (!target || !target.href) return;

    const currentHost = window.location.hostname;
    const linkUrl = new URL(target.href, window.location.href);
    const linkHost = linkUrl.hostname;

    const isGoogleSearchInternal = (
        linkHost.includes('google') && linkUrl.href.includes(currentHost)
    );

    const isExternal = (linkHost !== currentHost) && !isGoogleSearchInternal;

    if (isExternal) {
        event.preventDefault();
        const userConfirmed = confirm("You are being redirected to an external website. Do you want to continue?");
        if (userConfirmed) {
            window.open(linkUrl.href, '_blank');
        }
    }
});


  // For Search Button click option

  const searchIcon = document.getElementById('search-trigger');
const searchInput = document.getElementById('search-input');
const searchContainer = document.getElementById('search-container');
const searchForm = document.getElementById('search-form');

// Existing click handler — unchanged
let searchOpenedOnce = false;

searchIcon.addEventListener('click', function(event) {
    event.stopPropagation();

    if (searchInput.classList.contains('hidden')) {
        searchInput.classList.remove('hidden');
        searchInput.style.display = 'block';
        searchInput.focus();
        searchOpenedOnce = true; // Mark that input is now open
    } else {
        // Only trigger submit if user has typed something or input was already opened
        if (searchOpenedOnce) {
            if (searchInput.value.trim() !== "") {
                searchForm.submit(); // Submit the form if there's text
            } else {
                alert("Please fill out the search field.");
            }
        }
    }
});

// 🟢 NEW: Open when focused using Tab key
searchIcon.addEventListener('focus', function() {
    if (searchInput.classList.contains('hidden')) {
        searchInput.classList.remove('hidden');
        searchInput.style.display = 'block';
    }
});

// 🟢 NEW: Also allow Enter or Space key to trigger click behavior
searchIcon.addEventListener('keydown', function(event) {
    if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        searchIcon.click(); // trigger same behavior as click
    }
});

// 🟢 NEW: Close when clicking outside or focus leaves search area
document.addEventListener('click', function(event) {
    if (!searchContainer.contains(event.target)) {
        searchInput.classList.add('hidden');
        searchInput.style.display = 'none';
    }
});

// 🟢 NEW: Close when focus moves away (using Tab key)
searchInput.addEventListener('blur', function() {
    setTimeout(() => {
        if (!searchContainer.contains(document.activeElement)) {
            searchInput.classList.add('hidden');
            searchInput.style.display = 'none';
        }
    }, 150);
});

});










