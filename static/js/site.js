document.addEventListener("DOMContentLoaded", () => {
    document.body.classList.add("js-ready");

    const nav = document.querySelector(".site-nav");
    const toggle = document.querySelector(".nav-toggle");
    const menu = document.querySelector("#primary-menu");

    if (nav && toggle && menu) {
        toggle.addEventListener("click", () => {
            const isOpen = nav.classList.toggle("is-open");
            toggle.setAttribute("aria-expanded", String(isOpen));
        });

        menu.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => {
                nav.classList.remove("is-open");
                toggle.setAttribute("aria-expanded", "false");
            });
        });
    }

    const themes = ["default", "rose", "green"];
    const savedTheme = localStorage.getItem("portfolio-theme");
    const themeToggle = document.querySelector("[data-theme-toggle]");

    if (savedTheme && themes.includes(savedTheme)) {
        document.body.dataset.theme = savedTheme === "default" ? "" : savedTheme;
    }

    if (themeToggle) {
        themeToggle.addEventListener("click", () => {
            const currentTheme = document.body.dataset.theme || "default";
            const nextTheme = themes[(themes.indexOf(currentTheme) + 1) % themes.length];
            document.body.dataset.theme = nextTheme === "default" ? "" : nextTheme;
            localStorage.setItem("portfolio-theme", nextTheme);
        });
    }

    const revealItems = document.querySelectorAll(".reveal");

    if (!("IntersectionObserver" in window)) {
        revealItems.forEach((item) => item.classList.add("is-visible"));
        return;
    }

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.14 }
    );

    revealItems.forEach((item) => observer.observe(item));
});
