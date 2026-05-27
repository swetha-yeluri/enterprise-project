# Task 5 – Full-Stack User Management System (SQLite + Flask + React + Vite)

## 📁 Project Structure

```
task5/
├── backend/
│   ├── app.py          # Flask API (all endpoints)
│   ├── database.py     # SQLAlchemy db instance
│   ├── models.py       # User model / schema
│   ├── seed.py         # Auto-seed script
│   └── requirements.txt
└── frontend/
    ├── index.html
    ├── vite.config.js
    ├── package.json
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── App.css
        ├── components/
        │   ├── UserCard.jsx
        │   ├── UserFormModal.jsx
        │   ├── ConfirmDialog.jsx
        │   ├── SearchFilter.jsx
        │   ├── Pagination.jsx
        │   └── Toast.jsx
        ├── hooks/
        │   └── useUsers.js
        ├── pages/
        │   └── Dashboard.jsx
        └── utils/
            └── api.js
```

---

## 🚀 How to Run

### Step 1 — Backend (Terminal 1)

```bash
cd task5/backend

# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Run the server (auto-creates DB + seeds users)
python app.py
```
✅ Backend runs on → **http://localhost:5000**
✅ SQLite database file `users.db` is created automatically.

---

### Step 2 — Frontend (Terminal 2)

```bash
cd task5/frontend
npm install
npm run dev
```
✅ Frontend runs on → **http://localhost:5173**

---

## 🔌 API Endpoints

| Method | Endpoint       | Description                                      |
|--------|----------------|--------------------------------------------------|
| GET    | `/users`       | Get all users (supports `?search=`, `?role=`, `?page=`, `?limit=`) |
| GET    | `/users/<id>`  | Get single user by ID                            |
| POST   | `/users`       | Create new user                                  |
| PUT    | `/users/<id>`  | Update existing user                             |
| DELETE | `/users/<id>`  | Delete user                                      |
| GET    | `/roles`       | Get list of valid roles                          |

---

## ✅ Features

- SQLite persistent database via SQLAlchemy
- Full CRUD (Create, Read, Update, Delete)
- Search by name, email, or company
- Filter by role
- Pagination (6 users per page)
- Form validation (frontend + backend)
- Duplicate email detection
- Loading states, success toasts, error handling
- Responsive dark UI

## 🏆 Bonus Features
- Server-side search & role filtering
- Pagination with total count
- Auto-seed database on first run
- Clean layered architecture (model / db / routes)
