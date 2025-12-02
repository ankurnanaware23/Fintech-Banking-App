# ⚡ Django + React Project

A modern full-stack project created by [Ankur Nanaware].  
It combines a **Django REST Framework backend** with a **React + Vite + TailwindCSS frontend**, including light/dark mode support, base routing, and ready-to-use authentication.

---

## ✨ Features

### 🌐 Frontend (React + Vite + Tailwind)

-   ⚡ Blazing fast bundling with **Vite.js**
-   🎨 **TailwindCSS** preconfigured with custom themes
-   🌞🌙 Built-in **Light/Dark mode** toggle
-   🛣️ Base routes: `Home`, `Login`, `Register`, `Dashboard`
-   🔗 Axios client pre-setup for API calls

### 🛠 Backend (Django + DRF)

-   🐍 Django 5.x with **Django REST Framework**
-   🔐 Auth endpoints: `register`, `login`, `logout`, `refresh token`
-   ⚙️ Configurable `.env` support (via `python-decouple`)
-   📦 SQLite default, Postgres-ready
-   🚀 CORS + JWT authentication included

---

## 📂 Project Structure

```

boilerplate/
├── backend/                # Django project
│   ├── manage.py
│   ├── core/               # Main Django app (settings, urls, etc.)
│   ├── users/              # User & Auth logic
│   └── requirements.txt
│
├── frontend/               # React + Vite + Tailwind app
│   ├── index.html
│   ├── src/
│   │   ├── routes/         # Base routes
│   │   ├── components/     # Shared UI components
│   │   └── App.tsx
│   └── package.json
│
└── README.md

```

---

## 🙌 Credits

Generated with 💜 by [Ankur Nanaware].
Start building faster, skip the boring setup.
