
function googleTranslateElementInit() {
  new google.translate.TranslateElement(
    {
      pageLanguage: "en",  // Your page's language
      includedLanguages: "en,hi",  // Languages to include (English and Hindi in this case)
      layout: google.translate.TranslateElement.InlineLayout.SIMPLE,  // Choose layout
      // autoDisplay: false,
    },
    "google_translate_element"  // ID of the div to render the translate widget in
  );
}

// Custom translations dictionary
const translations = {
  en: {
   
    "मुखपृष्ठ": "Home",        
    "निविदा": "Tenders",
    "कर्मचारी प्रोफ़ाइल": "Staff Profile",  
    "मुख्य पृष्ठ पर जाएं" : "Skip to Main Content",
    "बोली शुद्धिपत्र": "Bid Corrigendum",
    "शुद्धिपत्र-01": "Corrigendum-01",
    "शुद्धिपत्र-02": "Corrigendum-02",
    "शुद्धिपत्र-03": "Corrigendum-03",
    "शुद्धिपत्र-04": "Corrigendum-04",
    "शुद्धिपत्र-05": "Corrigendum-05",
    "शुद्धिपत्र-06": "Corrigendum-06",
    "शुद्धिपत्र-07": "Corrigendum-07",
    "शुद्धिपत्र-08": "Corrigendum-08",
    "शुद्धिपत्र-09": "Corrigendum-09",
    "शुद्धिपत्र-10": "Corrigendum-10",

    "नया": "NEW",
    "निदेशक की कलम से": "Director's Message",
"राष्ट्रीय पवन ऊर्जा संस्थान, पिछले 25 वर्षों से देश में पवन ऊर्जा के व्यवस्थित विकास के लिए नवीन और नवीकरणीय ऊर्जा मंत्रालय को समर्थन प्रदान करने में अग्रणी रहा है। हम अनुसंधान एवं विकास, पवन संसाधन मूल्यांकन तटवर्ती एवं अपतट), मानकों के विकास, परीक्षण, प्रमाणन और कौशल विकास में पवन ऊर्जा क्षेत्र को अपनी सेवाएँ प्रदान करते आ रहे हैं। हम, देश में अपतट पवन विकास के लिए नोडल एजेंसी के रूप में, राष्ट्रीय अपतटीय पवन ऊर्जा नीति के कार्यान्वयन में भी मंत्रालय को समर्थन प्रदान करते आ रहे हैं। यह वेब-पृष्‍ठ पवन ऊर्जा संबंधी जानकारी के लिए एक केन्‍द्र का कार्य करते हुए नीवे के साथ सहयोग/साझेदारी के क्षेत्रों पर पणधारियों को जानकारी प्रदान करने के लिए तैयार किया गया है। इस संबंध में आपकी प्रतिक्रिया हमें आपको उत्‍कृष्‍ट सेवा करने में सहायक होगा।" : "National Institute of Wind Energy is at the forefront supporting the Ministry of New and Renewable Energy for the orderly development of wind power in the country, for 25 years now. We offer our services to the wind energy sector in Research and Development, Wind Resource Assessment (onshore and offshore), development of Standards, Testing, Certification and Skill Development. As the Nodal Agency for offshore wind development in the country, we also support the Ministry in the implementation of the National offshore wind energy policy. This web page has been created as a knowledge hub on wind energy and information to stakeholders on areas of collaboration / partnerships with NIWE. Your feedback will enable us to serve you better."
  },
  hi: {
    
    "Home": "मुखपृष्ठ",   
    "Tenders": "निविदा",
    "Staff Profile": "कर्मचारी प्रोफ़ाइल",   
    "Skip to Main Content" : "मुख्य पृष्ठ पर जाएं", 
    "Bid Corrigendum":"बोली शुद्धिपत्र",
    "Corrigendum-01": "शुद्धिपत्र-01",  
    "Corrigendum-02": "शुद्धिपत्र-02",
    "Corrigendum-03": "शुद्धिपत्र-03",
    "Corrigendum-04": "शुद्धिपत्र-04",
    "Corrigendum-05": "शुद्धिपत्र-05",
    "Corrigendum-06": "शुद्धिपत्र-06",
    "Corrigendum-07": "शुद्धिपत्र-07",
    "Corrigendum-08": "शुद्धिपत्र-08",   
    "Corrigendum-09": "शुद्धिपत्र-09",
    "Corrigendum-10": "शुद्धिपत्र-10", 
    "NEW": "नया",
    "Director's Message": "निदेशक की कलम से",
    "National Institute of Wind Energy is at the forefront supporting the Ministry of New and Renewable Energy for the orderly development of wind power in the country, for 25 years now. We offer our services to the wind energy sector in Research and Development, Wind Resource Assessment (onshore and offshore), development of Standards, Testing, Certification and Skill Development. As the Nodal Agency for offshore wind development in the country, we also support the Ministry in the implementation of the National offshore wind energy policy. This web page has been created as a knowledge hub on wind energy and information to stakeholders on areas of collaboration / partnerships with NIWE. Your feedback will enable us to serve you better.":"राष्ट्रीय पवन ऊर्जा संस्थान, पिछले 25 वर्षों से देश में पवन ऊर्जा के व्यवस्थित विकास के लिए नवीन और नवीकरणीय ऊर्जा मंत्रालय को समर्थन प्रदान करने में अग्रणी रहा है। हम अनुसंधान एवं विकास, पवन संसाधन मूल्यांकन तटवर्ती एवं अपतट), मानकों के विकास, परीक्षण, प्रमाणन और कौशल विकास में पवन ऊर्जा क्षेत्र को अपनी सेवाएँ प्रदान करते आ रहे हैं। हम, देश में अपतट पवन विकास के लिए नोडल एजेंसी के रूप में, राष्ट्रीय अपतटीय पवन ऊर्जा नीति के कार्यान्वयन में भी मंत्रालय को समर्थन प्रदान करते आ रहे हैं। यह वेब-पृष्‍ठ पवन ऊर्जा संबंधी जानकारी के लिए एक केन्‍द्र का कार्य करते हुए नीवे के साथ सहयोग/साझेदारी के क्षेत्रों पर पणधारियों को जानकारी प्रदान करने के लिए तैयार किया गया है। इस संबंध में आपकी प्रतिक्रिया हमें आपको उत्‍कृष्‍ट सेवा करने में सहायक होगा।",

    
  },
};

// Function to apply custom replacements based on the current language
function applyCustomReplacements(language) {
  const elements = document.querySelectorAll("a, p, h1, div, span, h2, h1, li"); // Add other tags if needed
  elements.forEach((el) => {
    const originalHTML = el.innerHTML.trim();     
    const targetHTML = translations[language]?.[originalHTML];
    if (targetHTML) {
      el.innerHTML = targetHTML; // Replace with the target HTML        
    }
  });
}

// Monitor changes in the page language
function monitorLanguageChange() {
  const observer = new MutationObserver(() => {
    const currentLanguage = document.documentElement.lang; // Detect current language

    if (currentLanguage === "hi") {
      applyCustomReplacements("hi"); // Apply Hindi translations
    } else if (currentLanguage === "en") {
      applyCustomReplacements("en"); // Apply English translations
    }
  });

  // Observe changes in the `<html>` tag's `lang` attribute
  observer.observe(document.documentElement, { attributes: true, attributeFilter: ["lang"] });
}

// Reapply translations when navigating links
function reapplyTranslationsOnLinkClick() {
  const links = document.querySelectorAll("a");
  links.forEach((link) => {
    link.addEventListener("click", () => {
      const currentLanguage = document.documentElement.lang || "en"; // Default to English if not set
      setTimeout(() => applyCustomReplacements(currentLanguage), 5000); // Delay to handle navigation
    });
  });
}

// Initialize on page load
document.addEventListener("DOMContentLoaded", () => {
  const defaultLanguage = "en"; // Set the default language
  document.documentElement.lang = defaultLanguage; // Ensure initial language is set
  applyCustomReplacements(defaultLanguage); // Apply default language translations
  monitorLanguageChange(); // Monitor language changes
  reapplyTranslationsOnLinkClick(); // Handle link navigation
});





