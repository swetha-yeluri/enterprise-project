# Enterprise Employee Management System — Backend API

A RESTful backend service built with **FastAPI** for the Enterprise Employee Management System project.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Framework | FastAPI |
| Runtime | Python 3.11+ |
| Validation | Pydantic v2 |
| Server | Uvicorn |
| Data | Mock JSON (Phase 1) |

---

## Project Structure

```
backend/
├── app/
│   ├── config/
│   │   └── settings.py          # App-wide configuration & env vars
│   ├── controllers/
│   │   └── employee_controller.py  # Business logic layer
│   ├── database/
│   │   └── mock_data.py         # Static mock employee data
│   ├── models/
│   │   └── employee_model.py    # Pydantic request/response schemas
│   ├── routes/
│   │   └── employee_routes.py   # API route definitions
│   ├── utils/
│   │   └── response_utils.py    # Shared response helpers
│   └── main.py                  # App factory & middleware setup
├── requirements.txt
├── run.py                        # Entry point
└── README.md
```

---

## Getting Started

### 1. Create & activate a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the development server

```bash
python run.py
```

The API will be available at **http://localhost:8000**

---

## API Endpoints

### Base URL: `http://localhost:8000/api/v1`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/api/v1/employees` | List all employees |
| GET | `/api/v1/employees/{id}` | Get employee by ID |
| GET | `/api/v1/employees/departments/summary` | Department headcount |
| GET | `/api/v1/employees/status/summary` | Status breakdown |

### Query Parameters for `GET /employees`

| Parameter | Type | Description |
|-----------|------|-------------|
| `department` | string | Filter by department name |
| `status` | string | Filter by status (Active / Inactive / On Leave) |
| `search` | string | Search by name or email |

### Example Requests

```bash
# All employees
curl http://localhost:8000/api/v1/employees

# Filter by department
curl http://localhost:8000/api/v1/employees?department=Engineering

# Search by name
curl http://localhost:8000/api/v1/employees?search=priya

# Get employee with ID 1
curl http://localhost:8000/api/v1/employees/1
```

---

## Interactive API Docs

- Swagger UI → http://localhost:8000/docs
- ReDoc → http://localhost:8000/redoc

---

## Environment Variables

Create a `.env` file in the `backend/` root if you wish to override defaults:

```env
APP_NAME=Enterprise Employee Management System
DEBUG=True
```

---

## Naming Conventions

- **Files** → `snake_case`
- **Classes / Models** → `PascalCase`
- **Functions / Variables** → `snake_case`
- **Routes** → `kebab-case` REST conventions

---

## Roadmap

- [ ] Task 4: PostgreSQL / SQLite database integration
- [ ] Task 5: CRUD endpoints (POST, PUT, DELETE)
- [ ] Task 6: JWT Authentication
- [ ] Task 7: Attendance module
