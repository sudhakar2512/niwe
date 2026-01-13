
// Bootstrap tooltips initialization (commented out block in the original code)
$(function () {
  $('[data-toggle="tooltip"]').tooltip();
});

// Panel visibility toggle
function toggleAnswer(panelId) {
  var panel = document.getElementById(panelId);
  var button = document.querySelector(`button[aria-controls="${panelId}"]`);

  if (panel.classList.contains("d-none")) {
    panel.classList.remove("d-none");
    button.setAttribute("aria-expanded", "true");
  } else {
    panel.classList.add("d-none");
    button.setAttribute("aria-expanded", "false");
  }
}



// Confirm external link redirection
function confirmExternalLink(event) {
  const userConfirmed = confirm(
    "You are being redirected to external website. Do you want to continue?"
  );
  if (!userConfirmed) {
    event.preventDefault(); // Stops navigation if the user cancels
    return false;
  }
  return true; // Allows navigation if the user confirms
}


 




