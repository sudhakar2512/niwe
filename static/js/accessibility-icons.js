document.addEventListener("DOMContentLoaded", function () {
    
    const triggerButton = document.querySelector(".accessibility-btn");
    const dropdownMenu = document.getElementById("accessibility-dropdown");
    const socialButton = document.querySelector(".social-btn");
    const socialDropdown = document.querySelector(".social-menu");

    // Font size controls
    const increaseFontBtn = document.getElementById("linkIncrease");
    const resetFontBtn = document.getElementById("linkReset");
    const decreaseFontBtn = document.getElementById("linkDecrease");

    // Accessibility settings
    const toggleContrastBtn = document.getElementById("toggleContrast");
    const toggleLineHeightBtn = document.getElementById("toggleLineHeight");
    const toggleTextSpacingBtn = document.getElementById("toggleTextSpacing");

    if(!triggerButton || !dropdownMenu || !socialButton || !socialDropdown){
        console.error("Elements not found");
        return;
    }


function getFirstFocusable(container) {
  if (!container) return null;
  return container.querySelector(
    'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
  );
}

// Initialize a pair (button toggle + menu/dropdown)
function initDropdownPair(button, menu, otherMenu) {
  if (!button || !menu) return;


  button.setAttribute('aria-haspopup', 'true');
  if (!button.hasAttribute('aria-expanded')) button.setAttribute('aria-expanded', 'false');


  button.addEventListener('click', function (e) {
    e.stopPropagation();
    const willShow = !menu.classList.contains('show');

    if (otherMenu && otherMenu.classList.contains('show')) {
      otherMenu.classList.remove('show');

      const otherBtn = otherMenu._toggleButton;
      if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
    }

    if (willShow) {
      menu.classList.add('show');
      button.setAttribute('aria-expanded', 'true');
      
    } else {
      menu.classList.remove('show');
      button.setAttribute('aria-expanded', 'false');
    }
  });

  menu._toggleButton = button;

  button.addEventListener('focus', function () {

    menu.classList.add('show');
    button.setAttribute('aria-expanded', 'true');

    if (otherMenu && otherMenu.classList.contains('show')) {
      otherMenu.classList.remove('show');
      const otherBtn = otherMenu._toggleButton;
      if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
    }
  });

  menu.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' || e.key === 'Esc') {
      menu.classList.remove('show');
      button.setAttribute('aria-expanded', 'false');
      button.focus();
    }
  });
  button.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' || e.key === 'Esc') {
      menu.classList.remove('show');
      button.setAttribute('aria-expanded', 'false');
      button.focus();
    }
  });
}

initDropdownPair(triggerButton, dropdownMenu, socialDropdown);
initDropdownPair(socialButton, socialDropdown, dropdownMenu);

// ---- Close dropdowns when clicking or focusing outside ----
document.addEventListener('click', function (event) {
  // close dropdownMenu if click outside toggle and outside menu
  if (triggerButton && dropdownMenu) {
    if (!triggerButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
      dropdownMenu.classList.remove('show');
      triggerButton.setAttribute('aria-expanded', 'false');
    }
  }
  if (socialButton && socialDropdown) {
    if (!socialButton.contains(event.target) && !socialDropdown.contains(event.target)) {
      socialDropdown.classList.remove('show');
      socialButton.setAttribute('aria-expanded', 'false');
    }
  }
});

// Use focusin which bubbles: close menus when focus moves outside them
document.addEventListener('focusin', function (event) {
  const active = document.activeElement;

  if (triggerButton && dropdownMenu) {
    if (!triggerButton.contains(active) && !dropdownMenu.contains(active)) {
      dropdownMenu.classList.remove('show');
      triggerButton.setAttribute('aria-expanded', 'false');
    }
  }
  if (socialButton && socialDropdown) {
    if (!socialButton.contains(active) && !socialDropdown.contains(active)) {
      socialDropdown.classList.remove('show');
      socialButton.setAttribute('aria-expanded', 'false');
    }
  }
});


    toggleDropdown(triggerButton, dropdownMenu);
    toggleDropdown(socialButton, socialDropdown);

    // ---- FONT SIZE HANDLING ----
    let fontSize = localStorage.getItem("fontSize") ? parseInt(localStorage.getItem("fontSize")) : 16;
    document.body.style.fontSize = fontSize + "px";

    function updateFontSize(size) {
        document.body.style.fontSize = size + "px";
        localStorage.setItem("fontSize", size);
    }

    increaseFontBtn.addEventListener("click", function () {
        if (fontSize < 22) {
            fontSize += 2;
            updateFontSize(fontSize);
        }
    });

    decreaseFontBtn.addEventListener("click", function () {
        if (fontSize > 12) {
            fontSize -= 2;
            updateFontSize(fontSize);
        }
    });

    resetFontBtn.addEventListener("click", function () {
        fontSize = 16;
        updateFontSize(fontSize);
    });

    // ---- HIGH CONTRAST MODE ----
    function applyHighContrast() {
        document.body.classList.add("high-contrast");
        localStorage.setItem("highContrast", "enabled");
        toggleCheckmark(toggleContrastBtn, true);
    }

    function removeHighContrast() {
        document.body.classList.remove("high-contrast");
        localStorage.setItem("highContrast", "disabled");
        toggleCheckmark(toggleContrastBtn, false);
    }

    toggleContrastBtn.addEventListener("click", function () {
        document.body.classList.toggle("high-contrast");
        let isActive = document.body.classList.contains("high-contrast");
        localStorage.setItem("highContrast", isActive ? "enabled" : "disabled");
        toggleCheckmark(toggleContrastBtn, isActive);
    });

    // ---- APPLY SETTINGS ON LOAD ----
    if (localStorage.getItem("highContrast") === "enabled") {
        applyHighContrast();
    }

    if (localStorage.getItem("fontSize")) {
        updateFontSize(parseInt(localStorage.getItem("fontSize")));
    }

    // ---- LINE HEIGHT TOGGLE ----
    toggleLineHeightBtn.addEventListener("click", function () {
        document.body.classList.toggle("accessible-line-height");
        let isActive = document.body.classList.contains("accessible-line-height");
        localStorage.setItem("lineHeight", isActive ? "true" : "false");
        toggleCheckmark(toggleLineHeightBtn, isActive);
    });

    if (localStorage.getItem("lineHeight") === "true") {
        document.body.classList.add("accessible-line-height");
        toggleCheckmark(toggleLineHeightBtn, true);
    }

    // ---- TEXT SPACING TOGGLE ----
    toggleTextSpacingBtn.addEventListener("click", function () {
        document.body.classList.toggle("accessible-text-spacing");
        let isActive = document.body.classList.contains("accessible-text-spacing");
        localStorage.setItem("textSpacing", isActive ? "true" : "false");
        toggleCheckmark(toggleTextSpacingBtn, isActive);
    });

    if (localStorage.getItem("textSpacing") === "true") {
        document.body.classList.add("accessible-text-spacing");
        toggleCheckmark(toggleTextSpacingBtn, true);
    }

    // ---- FUNCTION TO ADD/REMOVE ✅ TICK MARK ----
    function toggleCheckmark(button, isActive) {
        let text = button.innerText.replace("✅ ", "").trim();
        button.innerHTML = `<i class="fa ${getIcon(button.id)}"></i> ${isActive ? '✅ ' : ''}${text}`;
    }

    function getIcon(buttonId) {
        const icons = {
            "toggleLineHeight": "fa-text-height",
            "toggleTextSpacing": "fa-text-width",
            "toggleContrast": "fa-adjust"
        };
        return icons[buttonId] || "fa-circle";
    }

});