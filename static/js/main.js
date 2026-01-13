let questions = document.querySelectorAll(".faq__question");
questions.forEach((question) => {
    question.addEventListener("click", function () {
        question.classList.toggle("faq__question_active");
        const nextElement = question.nextElementSibling;
        nextElement.classList.toggle("faq__panel_active");
    });
});

document.addEventListener("DOMContentLoaded", function () {
    var sidebarLinks = document.querySelectorAll("#sidebar a li");

    sidebarLinks.forEach(function (link) {
        link.addEventListener("click", function () {
            var activeLink = document.querySelector("#sidebar a li.active");
            if (activeLink) {
                activeLink.classList.remove("active");
            }
            this.classList.add("active");
        });
    });
    // ----------------------

    // $(".main-content .owl-carousel").owlCarousel({
    //     autoplay: true,
    //     autoplayTimeout: 4000,
    //     stagePadding: 30,
    //     loop: true,
    //     margin: 10,
    //     nav: true,
    //     navText: [
    //         '<i class="fa fa-angle-left" aria-hidden="true"></i>',
    //         '<i class="fa fa-angle-right" aria-hidden="true"></i>',
    //     ],
    //     navContainer: ".main-content .custom-nav",
    //     responsive: {
    //         0: {
    //             items: 1,
    //         },
    //         410: {
    //             items: 2,
    //         },
    //         600: {
    //             items: 2,
    //         },
    //         991: {
    //             items: 3,
    //         },
    //         1200: {
    //             items: 4,
    //         },
    //         1400: {
    //             items: 6,
    //         },
    //     },
    // });

    $(".index-gallery").owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        navText: [
            "<i class='fa fa-caret-left'></i>",
            "<i class='fa fa-caret-right'></i>",
        ],
        autoplay: true,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1,
            },
            600: {
                items: 1,
            },
            1000: {
                items: 1,
            },
        },
    });

    $(document).ready(function () {
        $("#search-icn").click(function () {
            $(".dearch-div").slideToggle("slow");
            // Alternative animation for example
            // slideToggle("fast");
        });
    });
});

// document file size and formate read script

document.addEventListener("DOMContentLoaded", async function () {
    const docLinks = document.querySelectorAll("a[data-doc]");

    docLinks.forEach(async (link) => {
        try {
            // Fetch file
            const response = await fetch(link.href);
            const blob = await response.blob();
            // Get file size in MB
            const sizeMB = (blob.size / (1024 * 1024)).toFixed(2);
            // Get file extension
            const fileType = link.href.split(".").pop().toUpperCase();
            // Create a styled span to show format and size
            const infoSpan = document.createElement("span");
            infoSpan.classList.add("doc-file-info", fileType.toLowerCase()); // e.g., pdf, docx
            infoSpan.textContent = `[ ${fileType}, ${sizeMB} MB ]`;
            // Append after link text with a space
            link.appendChild(document.createTextNode(" "));
            link.appendChild(infoSpan);
        } catch (err) {
            console.error("Error fetching file:", err);
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    var myCarouselEl = document.getElementById("carouselExampleControls");
    var pauseBtn = document.getElementById("carouselPauseBtn");
    var btnIcon = document.getElementById("carouselBtnIcon");

    if (!myCarouselEl || !pauseBtn || !btnIcon) {
        console.warn("Carousel elements not found, skipping carousel JS.");
        return; // stop this script, prevent errors
    }

    var carousel = new bootstrap.Carousel(myCarouselEl, {
        interval: 2000,
        ride: "carousel",
        pause: false,
    });

    var isPaused = false;
    var manuallyPaused = false;

    // Hover control
    myCarouselEl.addEventListener("mouseenter", function () {
        if (!manuallyPaused) carousel.pause();
    });
    myCarouselEl.addEventListener("mouseleave", function () {
        if (!manuallyPaused) carousel.cycle();
    });

    // Manual Play/Pause button
    pauseBtn.addEventListener("click", function () {
        if (isPaused) {
            manuallyPaused = false;
            carousel.cycle();
            btnIcon.classList.replace("fa-play", "fa-pause");
            pauseBtn.setAttribute("aria-label", "Pause carousel");
        } else {
            manuallyPaused = true;
            carousel.pause();
            btnIcon.classList.replace("fa-pause", "fa-play");
            pauseBtn.setAttribute("aria-label", "Play carousel");
        }
        isPaused = !isPaused;
    });
});

//  script for detect the img and anchor and add alt and aria-label
document.addEventListener("DOMContentLoaded", () => {
   

    // ✅ Fix missing alt attributes for images
    const imgs = document.querySelectorAll("img");
    imgs.forEach((img, i) => {
        const alt = img.getAttribute("alt");
        if (!alt || alt.trim() === "") {
            const src = img.getAttribute("src") || "";
            const filename = src
                .split("/")
                .pop()
                .split(".")[0]
                .replace(/[-_]/g, " ")
                .trim();
            const altText = filename ? filename + " image" : "decorative image";
            img.setAttribute("alt", altText);
        }
    });

    // ✅ Fix missing aria-labels for anchor tags
    const anchors = document.querySelectorAll("a");
    anchors.forEach((a, j) => {
        const ariaLabel = a.getAttribute("aria-label");
        if (!ariaLabel || ariaLabel.trim() === "") {
            let label = a.textContent.trim();
            if (!label) {
                const href = a.getAttribute("href") || "";
                if (href && href !== "#" && !href.startsWith("javascript")) {
                    const filename = href
                        .split("/")
                        .pop()
                        .split(".")[0]
                        .replace(/[-_]/g, " ");
                    label = filename
                        ? "Open " + filename + " link"
                        : "Visit link";
                } else {
                    label = "Clickable element";
                }
            }
            a.setAttribute("aria-label", label);
          
        }
    });

});

// script that control the facebook widget not fecthing message 
document.addEventListener("DOMContentLoaded", function () {
    // Hide fallback messages initially
    document.getElementById("facebook-fallback").style.display = "none";

    // Check if Facebook widget loaded successfully
    setTimeout(function () {
        const facebookWidget = document.querySelector(".fb-page");
        if (facebookWidget && facebookWidget.offsetHeight < 100) {
            document.getElementById("facebook-fallback").style.display =
                "block";
        }
    }, 3000);
});




document.addEventListener("DOMContentLoaded", function () {
  // Create a test element to check if Owl CSS is loaded
  const testEl = document.createElement("div");
  testEl.className = "owl-carousel owl-theme";
  testEl.style.display = "none";
  document.body.appendChild(testEl);

  // Get a computed style property that should exist only when Owl CSS is loaded
  const owlCssLoaded =
    window.getComputedStyle(testEl).getPropertyValue("display") !== "none" ||
    window.getComputedStyle(testEl).getPropertyValue("position") === "relative";

  document.body.removeChild(testEl);

  // ✅ Only load or initialize Owl if CSS is actually loaded
  if (owlCssLoaded) {
    // Your Owl Carousel init code
    $(".main-content .owl-carousel").owlCarousel({
      autoplay: true,
      autoplayTimeout: 4000,
      stagePadding: 30,
      loop: true,
      margin: 10,
      nav: true,
      navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>',
      ],
      navContainer: ".main-content .custom-nav",
      responsive: {
        0: { items: 1 },
        410: { items: 2 },
        600: { items: 2 },
        991: { items: 3 },
        1200: { items: 4 },
        1400: { items: 6 },
      },
    });
  } else {
    console.warn("⚠️ Owl Carousel CSS not detected — JS initialization skipped.");
  }
});

// search page role="status" add js 
document.addEventListener('DOMContentLoaded', function() {

    // Function to apply role and aria-live to all .gs-snippet elements
    function applyAccessibilityAttributes() {
        document.querySelectorAll('.gs-snippet').forEach(function(element) {
            element.setAttribute('role', 'status');
            element.setAttribute('aria-live', 'polite');
            element.setAttribute('tabindex', '0');
        });
    }

    // Apply to existing elements (if any)
    applyAccessibilityAttributes();

    // Watch for dynamically added elements
    const observer = new MutationObserver(() => {
        applyAccessibilityAttributes();
    });

    observer.observe(document.body, { childList: true, subtree: true });
});

document.addEventListener("DOMContentLoaded", function() {

  const tables = document.querySelectorAll("table");

  tables.forEach(function(table) {

    const classesToAdd = ["w-100"];

    classesToAdd.forEach(cls => {
      if (!table.classList.contains(cls)) {
        table.classList.add(cls);
      }
    });

    const parent = table.parentElement;
    if (!parent.classList.contains("table-responsive")) {

      const wrapper = document.createElement("div");
      wrapper.classList.add("table-responsive");

      parent.insertBefore(wrapper, table);

      wrapper.appendChild(table);
    }
  });
});

document.addEventListener("DOMContentLoaded", function() {
  let currentSize = 1; // 1 = 100%
  const html = document.documentElement;
  const body = document.body;

  const MIN_SIZE = 0.8; // Don’t go smaller than 80%
  const MAX_SIZE = 1.5;   // Don’t go beyond 200%

  const increaseBtn = document.getElementById("increase-font");
  const decreaseBtn = document.getElementById("decrease-font");

  function applyFontSize() {
    html.style.fontSize = (currentSize * 100) + "%"; // Scale everything based on root font-size
    body.style.fontSize = "inherit"; // Ensure body inherits the root font size
  }

  increaseBtn.addEventListener("click", function() {
    if (currentSize < MAX_SIZE) {
      currentSize += 0.1;
      applyFontSize();
    }
  });

  decreaseBtn.addEventListener("click", function() {
    if (currentSize > MIN_SIZE) {
      currentSize -= 0.1;
      applyFontSize();
    }
  });

  // Initialize
  applyFontSize();
});
