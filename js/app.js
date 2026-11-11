(function () {
  const root = document.documentElement;
  const stored = localStorage.getItem("theme");
  if (stored === "light" || stored === "dark") {
    root.setAttribute("data-theme", stored);
  } else if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
    root.setAttribute("data-theme", "dark");
  }

  const themeBtn = document.getElementById("theme-toggle");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      localStorage.setItem("theme", next);
      themeBtn.setAttribute("aria-label", next === "dark" ? "切换到浅色" : "切换到深色");
    });
  }

  const nav = document.querySelector(".nav");
  const toggle = document.querySelector(".nav-toggle");
  if (nav && toggle) {
    toggle.addEventListener("click", function () {
      const open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  const progress = document.querySelector(".read-progress span");
  if (progress) {
    const updateProgress = function () {
      const doc = document.documentElement;
      const max = doc.scrollHeight - window.innerHeight;
      const p = max > 0 ? Math.min(1, Math.max(0, window.scrollY / max)) : 0;
      progress.style.transform = "scaleX(" + p + ")";
    };
    updateProgress();
    window.addEventListener("scroll", updateProgress, { passive: true });
    window.addEventListener("resize", updateProgress);
  }

  const toc = document.querySelector(".toc");
  if (toc) {
    const links = Array.prototype.slice.call(toc.querySelectorAll('a[href^="#"]'));
    const targets = links
      .map(function (a) {
        return document.getElementById((a.getAttribute("href") || "").slice(1));
      })
      .filter(Boolean);

    const setCurrent = function (id) {
      links.forEach(function (a) {
        const on = a.getAttribute("href") === "#" + id;
        a.classList.toggle("is-current", on);
        if (on) a.setAttribute("aria-current", "location");
        else a.removeAttribute("aria-current");
      });
    };

    if (targets.length) {
      setCurrent(targets[0].id);
    }
    if (targets.length && "IntersectionObserver" in window) {
      const vis = {};
      const io = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (en) {
            vis[en.target.id] = en.isIntersecting;
          });
          let current = null;
          targets.forEach(function (t) {
            if (vis[t.id] && !current) current = t.id;
          });
          if (!current) {
            for (let i = targets.length - 1; i >= 0; i--) {
              if (targets[i].getBoundingClientRect().top <= 140) {
                current = targets[i].id;
                break;
              }
            }
          }
          if (current) setCurrent(current);
        },
        { rootMargin: "-18% 0px -62% 0px", threshold: 0 }
      );
      targets.forEach(function (t) {
        io.observe(t);
      });
    }
  }

  const search = document.getElementById("entry-search");
  const buttons = document.querySelectorAll(".filter-btn");
  const cards = document.querySelectorAll("[data-entry-card]");
  const empty = document.getElementById("filter-empty");
  if (!cards.length) return;

  const state = { q: "", company: "全部", drug: "全部", indication: "全部" };

  function norm(s) {
    return (s || "").toLowerCase();
  }

  function apply() {
    let shown = 0;
    cards.forEach(function (card) {
      const hay = norm(card.getAttribute("data-search"));
      const companies = card.getAttribute("data-companies") || "";
      const drugs = card.getAttribute("data-drugs") || "";
      const indications = card.getAttribute("data-indications") || "";
      const okQ = !state.q || hay.indexOf(norm(state.q)) !== -1;
      const okC = state.company === "全部" || companies.split("|").indexOf(state.company) !== -1;
      const okD = state.drug === "全部" || drugs.split("|").indexOf(state.drug) !== -1;
      const okI = state.indication === "全部" || indications.split("|").indexOf(state.indication) !== -1;
      const vis = okQ && okC && okD && okI;
      card.classList.toggle("hidden", !vis);
      if (vis) shown += 1;
    });
    if (empty) empty.classList.toggle("hidden", shown > 0);
  }

  if (search) {
    search.addEventListener("input", function () {
      state.q = search.value.trim();
      apply();
    });
  }

  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      const key = btn.getAttribute("data-key");
      const val = btn.getAttribute("data-val");
      state[key] = val;
      document.querySelectorAll('.filter-btn[data-key="' + key + '"]').forEach(function (b) {
        b.setAttribute("aria-pressed", b === btn ? "true" : "false");
      });
      apply();
    });
  });
})();
