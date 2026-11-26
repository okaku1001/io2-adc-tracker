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
    const links = Array.prototype.slice.call(toc.querySelectorAll('ol a[href^="#"]'));
    const targets = links
      .map(function (a) {
        return document.getElementById((a.getAttribute("href") || "").slice(1));
      })
      .filter(Boolean);

    const storageKey = "io2-toc-last:" + location.pathname.replace(/\/+$/, "");
    const launch = document.querySelector(".toc-launch");
    const closeBtn = toc.querySelector(".toc-close");
    const resume = toc.querySelector(".toc-resume");
    let backdrop = document.querySelector(".toc-backdrop");
    if (!backdrop) {
      backdrop = document.createElement("div");
      backdrop.className = "toc-backdrop";
      backdrop.hidden = true;
      document.body.appendChild(backdrop);
    }

    const setCurrent = function (id) {
      links.forEach(function (a) {
        const on = a.getAttribute("href") === "#" + id;
        a.classList.toggle("is-current", on);
        if (on) a.setAttribute("aria-current", "location");
        else a.removeAttribute("aria-current");
      });
    };

    const remember = function (id) {
      if (!id) return;
      const link = links.filter(function (a) { return a.getAttribute("href") === "#" + id; })[0];
      if (!link) return;
      const date = (link.querySelector(".toc-date") || {}).textContent || "";
      const title = (link.querySelector(".toc-title") || {}).textContent || "";
      try {
        localStorage.setItem(storageKey, JSON.stringify({ id: id, date: date, title: title }));
      } catch (err) {}
      updateResume();
    };

    const readLast = function () {
      try {
        return JSON.parse(localStorage.getItem(storageKey) || "null");
      } catch (err) {
        return null;
      }
    };

    const updateResume = function () {
      if (!resume) return;
      const last = readLast();
      links.forEach(function (a) { a.classList.remove("is-last"); });
      if (!last || !last.id) {
        resume.classList.add("hidden");
        resume.innerHTML = "";
        return;
      }
      const link = links.filter(function (a) { return a.getAttribute("href") === "#" + last.id; })[0];
      if (!link || !document.getElementById(last.id)) {
        resume.classList.add("hidden");
        resume.innerHTML = "";
        return;
      }
      link.classList.add("is-last");
      const label = (last.date ? last.date + " " : "") + (last.title || "上次读到的条目");
      resume.innerHTML = '<a href="#' + last.id + '">回到上次阅读：' + label + "</a>";
      resume.classList.remove("hidden");
    };

    let lockY = 0;
    const instantScroll = function (to) {
      const root = document.documentElement;
      const prev = root.style.scrollBehavior;
      root.style.scrollBehavior = "auto";
      if (typeof to === "number") window.scrollTo(0, to);
      else if (to && to.scrollIntoView) to.scrollIntoView({ behavior: "auto", block: "start" });
      root.style.scrollBehavior = prev;
    };
    const isDrawer = function () {

      return launch && window.getComputedStyle(launch).display !== "none";
    };
    const setOpen = function (open) {
      if (!isDrawer() && open) return;
      if (open) {
        lockY = window.scrollY || window.pageYOffset || 0;
        document.body.classList.add("toc-open");
        document.body.style.position = "fixed";
        document.body.style.top = "-" + lockY + "px";
        document.body.style.left = "0";
        document.body.style.right = "0";
        document.body.style.width = "100%";
        backdrop.hidden = false;
        if (launch) launch.setAttribute("aria-expanded", "true");
        const focusEl = closeBtn || toc;
        if (focusEl && focusEl.focus) focusEl.focus();
      } else {
        document.body.classList.remove("toc-open");
        const y = lockY;
        document.body.style.position = "";
        document.body.style.top = "";
        document.body.style.left = "";
        document.body.style.right = "";
        document.body.style.width = "";
        backdrop.hidden = true;
        instantScroll(y);
        if (launch) {
          launch.setAttribute("aria-expanded", "false");
          launch.focus({ preventScroll: true });
        }
      }
    };

    const goToId = function (id) {
      const el = document.getElementById(id);
      if (!el) return;
      remember(id);
      setCurrent(id);
      const wasOpen = document.body.classList.contains("toc-open");
      if (wasOpen) setOpen(false);
      const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      const jump = function () {
        if (reduce || wasOpen) instantScroll(el);
        else el.scrollIntoView({ behavior: "smooth", block: "start" });
      };
      jump();
      requestAnimationFrame(jump);
    };

    if (launch) {
      launch.setAttribute("aria-label", "打开本页时间线目录");
      launch.addEventListener("click", function () {
        const open = !document.body.classList.contains("toc-open");
        setOpen(open);
      });
    }
    if (closeBtn) closeBtn.addEventListener("click", function () { setOpen(false); });
    backdrop.addEventListener("click", function () { setOpen(false); });
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && document.body.classList.contains("toc-open")) {
        ev.preventDefault();
        setOpen(false);
      }
    });
    window.addEventListener("resize", function () {
      if (document.body.classList.contains("toc-open") && !isDrawer()) setOpen(false);
    });

    toc.addEventListener("click", function (ev) {
      const a = ev.target.closest ? ev.target.closest('a[href^="#"]') : null;
      if (!a || !toc.contains(a)) return;
      const id = (a.getAttribute("href") || "").slice(1);
      if (!id || !document.getElementById(id)) return;
      ev.preventDefault();
      goToId(id);
    });

    updateResume();

    if (targets.length) {
      const last = readLast();
      if (last && document.getElementById(last.id)) setCurrent(last.id);
      else setCurrent(targets[0].id);
    }
    let allowRemember = false;
    window.addEventListener("scroll", function () { allowRemember = true; }, { passive: true, once: true });

    if (targets.length && "IntersectionObserver" in window) {
      const vis = {};
      const io = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (en) {
            vis[en.target.id] = en.isIntersecting;
          });
          let current = null;
          targets.forEach(function (el) {
            if (vis[el.id] && !current) current = el.id;
          });
          if (!current) {
            for (let i = targets.length - 1; i >= 0; i--) {
              if (targets[i].getBoundingClientRect().top <= 140) {
                current = targets[i].id;
                break;
              }
            }
          }
          if (current) {
            setCurrent(current);
            if (allowRemember) remember(current);
          }
        },
        { rootMargin: "-18% 0px -62% 0px", threshold: 0 }
      );
      targets.forEach(function (el) {
        io.observe(el);
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
