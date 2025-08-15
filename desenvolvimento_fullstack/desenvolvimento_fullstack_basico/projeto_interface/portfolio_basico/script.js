const $ = (sel, ctx = document) => ctx.querySelector(sel);
const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));

(function themeBoot() {
  const root = document.documentElement;
  const saved = localStorage.getItem("theme"); // "light" | "dark" | null
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  const initial = saved ?? (prefersDark ? "dark" : "light");
  root.setAttribute("data-theme", initial);
  const btn = $("#themeToggle");
  if (btn) {
    btn.setAttribute("aria-pressed", initial === "dark" ? "true" : "false");
    btn.addEventListener("click", () => {
      const curr = root.getAttribute("data-theme");
      const next = curr === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      btn.setAttribute("aria-pressed", next === "dark" ? "true" : "false");
      localStorage.setItem("theme", next);
    });
  }
})();

(function mobileMenu() {
  const btn = $("#btnMenu");
  const menu = $("#menu");
  if (!btn || !menu) return;
  btn.addEventListener("click", () => {
    const open = menu.classList.toggle("is-open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  });
  // Fecha ao clicar em um link
  menu.addEventListener("click", (e) => {
    if (e.target.matches("a")) {
      menu.classList.remove("is-open");
      btn.setAttribute("aria-expanded", "false");
    }
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      menu.classList.remove("is-open");
      btn.setAttribute("aria-expanded", "false");
    }
  });
})();

(function activeSectionOnScroll() {
  const links = $$("#menu a[href^='#']");
  // Scroll suave
  links.forEach((a) => {
    a.addEventListener("click", (e) => {
      const id = a.getAttribute("href");
      const el = $(id);
      if (!el) return;
      e.preventDefault();
      el.scrollIntoView({ behavior: "smooth", block: "start" });
      history.pushState(null, "", id);
    });
  });

  const sections = links.map((a) => $(a.getAttribute("href"))).filter(Boolean);

  const obs = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const id = "#" + entry.target.id;
        const link = $(`#menu a[href='${id}']`);
        if (link) {
          if (entry.isIntersecting) {
            links.forEach((l) => l.removeAttribute("aria-current"));
            link.setAttribute("aria-current", "page");
          }
        }
      });
    },
    { rootMargin: "-40% 0px -50% 0px", threshold: 0.01 }
  );

  sections.forEach((sec) => obs.observe(sec));
})();

(function floatingFallback() {
  // Só se o navegador não suporta :has()
  const test = CSS.supports("selector(:has(*))");
  if (test) return;

  const fields = $$(".field");
  fields.forEach((wrap) => {
    const input = $("input,textarea", wrap);
    if (!input) return;
    const toggle = () => {
      wrap.classList.toggle("is-filled", !!input.value.trim());
    };
    ["input", "change"].forEach((ev) => input.addEventListener(ev, toggle));
    toggle();
  });
})();

(function contactForm() {
  const form = $("#formContato");
  const status = $("#status");
  if (!form) return;

  const showMsg = (msg, type = "ok") => {
    if (!status) return;
    status.textContent = msg;
    status.className = `msg ${type === "ok" ? "ok" : "err"}`;
  };

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const btn = $("button[type='submit']", form);
    btn?.classList.add("is-loading");

    const required = ["#nome", "#email", "#mensagem"].map((s) => $(s, form));
    let valid = true;

    required.forEach((el) => {
      const empty = !el.value.trim();
      el.setAttribute("aria-invalid", empty ? "true" : "false");
      if (empty) valid = false;
    });

    const email = $("#email", form)?.value || "";
    const emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    if (!emailOk) {
      $("#email", form)?.setAttribute("aria-invalid", "true");
      valid = false;
    }

    if (!valid) {
      showMsg("Confere os campos obrigatórios, por favor.", "err");
      btn?.classList.remove("is-loading");
      return;
    }

    try {
      await new Promise((r) => setTimeout(r, 900));
      form.reset();
      $$("#formContato [aria-invalid='true']").forEach((el) =>
        el.setAttribute("aria-invalid", "false")
      );
      showMsg("Mensagem enviada com sucesso! 💌", "ok");
      toast("Valeu! Já já te respondo 😉", "ok");
    } catch (err) {
      showMsg("Falha ao enviar. Tenta novamente.", "err");
      toast("Ops! Deu ruim no envio.", "err");
    } finally {
      btn?.classList.remove("is-loading");
    }
  });
})();

(function yearFoot() {
  const el = $("#ano");
  if (el) el.textContent = new Date().getFullYear();
})();

function toast(message, type = "ok") {
  let t = $(".toast");
  if (!t) {
    t = document.createElement("div");
    t.className = "toast";
    document.body.appendChild(t);
  }
  t.className = `toast show ${type === "ok" ? "toast--ok" : "toast--err"}`;
  t.textContent = message;
  setTimeout(() => t.classList.remove("show"), 2600);
}

(function revealOnScroll() {
  const items = $$("section .card, .project, .timeline .tl-card");
  items.forEach((el) => {
    el.style.opacity = 0;
    el.style.transform = "translateY(8px)";
  });

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.style.transition = "opacity .35s ease, transform .35s ease";
          e.target.style.opacity = 1;
          e.target.style.transform = "translateY(0)";
          io.unobserve(e.target);
        }
      });
    },
    { threshold: 0.08 }
  );

  items.forEach((el) => io.observe(el));
})();
