(function () {
  const STORAGE_KEY = "site-lang";
  const DEFAULT_LANG = "pt";

  function getInitialLang() {
    const saved = window.localStorage.getItem(STORAGE_KEY);
    if (saved === "pt" || saved === "en") return saved;
    const browserLang = (navigator.language || "").toLowerCase();
    return browserLang.startsWith("pt") ? "pt" : "en";
  }

  function applyLanguage(lang) {
    const dict = translations[lang] || translations[DEFAULT_LANG];

    document.querySelectorAll("[data-i18n]").forEach((el) => {
      const key = el.getAttribute("data-i18n");
      const value = dict[key];
      if (value === undefined) return;
      if (el.hasAttribute("data-i18n-html")) {
        el.innerHTML = value;
      } else {
        el.textContent = value;
      }
    });

    document.querySelectorAll("[data-i18n-attr]").forEach((el) => {
      const spec = el.getAttribute("data-i18n-attr");
      spec.split(";").forEach((pair) => {
        const [attr, key] = pair.split(":").map((s) => s.trim());
        if (attr && dict[key] !== undefined) {
          el.setAttribute(attr, dict[key]);
        }
      });
    });

    document.documentElement.setAttribute("lang", lang === "pt" ? "pt-BR" : "en");
    document.querySelectorAll(".lang-toggle [data-lang-option]").forEach((btn) => {
      btn.classList.toggle("active", btn.getAttribute("data-lang-option") === lang);
    });

    window.localStorage.setItem(STORAGE_KEY, lang);
  }

  function initLangToggle() {
    document.querySelectorAll(".lang-toggle [data-lang-option]").forEach((btn) => {
      btn.addEventListener("click", () => {
        applyLanguage(btn.getAttribute("data-lang-option"));
      });
    });
  }

  function initNavToggle() {
    const toggle = document.querySelector(".nav-toggle");
    const links = document.querySelector(".nav-links");
    if (!toggle || !links) return;
    toggle.addEventListener("click", () => {
      links.classList.toggle("is-open");
    });
  }

  function initCurrentPage() {
    const path = window.location.pathname.split("/").pop() || "index.html";
    document.querySelectorAll(".nav-links a").forEach((a) => {
      const href = a.getAttribute("href");
      if (href === path) {
        a.setAttribute("aria-current", "page");
      }
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    initLangToggle();
    initNavToggle();
    initCurrentPage();
    applyLanguage(getInitialLang());
  });
})();
