# GeoIndia 🚀

GeoIndia is a Full Stack Geo Location API Platform built using FastAPI, React, PostgreSQL, JWT Authentication, and API Key Security.

This project provides APIs for Indian States, Districts, and Villages with secure authentication, API usage tracking, analytics dashboard, and search functionality.

---

# 🌟 Features

## 🔐 Authentication System

* User Registration
* User Login
* JWT Authentication
* Protected Routes
* Secure Logout

## 🔑 API Key Security

* Generate API Keys
* Secure API Access
* x-api-key Header Verification
* API Request Validation

## 🌍 Geo APIs

* Fetch States
* Fetch Districts
* Fetch Villages
* Search Villages

## 📊 Dashboard Features

* Analytics Cards
* Usage Tracking
* Search System
* Sidebar Navigation
* Dynamic Data Updates
* Modern UI using Tailwind CSS

## ⚙️ Backend Features

* FastAPI Backend
* PostgreSQL Database
* SQLAlchemy ORM
* Swagger Documentation
* Usage Logging
* API Security Middleware

---

# 🛠️ Tech Stack

## Frontend

* React.js
* Vite
* Tailwind CSS
* Axios
* React Router DOM

## Backend

* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* JWT Authentication

---

# 📂 Project Structure

```bash
geoindia/
│
├── app/
│   ├── core/
│   ├── models/
│   ├── routes/
│   └── main.py
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   └── api.js
│
├── requirements.txt
└── README.md
```

---

# 🚀 Backend Setup

## 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

## 2️⃣ Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Run Backend

```bash
uvicorn app.main:app --reload --port 8008
```

Backend Runs On:

```bash
http://127.0.0.1:8008
```

Swagger Docs:

```bash
http://127.0.0.1:8008/docs
```

---

# 🚀 Frontend Setup

## 1️⃣ Move To Frontend

```bash
cd frontend
```

## 2️⃣ Install Dependencies

```bash
npm install
```

## 3️⃣ Run Frontend

```bash
npm run dev
```

Frontend Runs On:

```bash
http://localhost:5173
```

---

# 🔐 Authentication Flow

1. Register User
2. Login User
3. Receive JWT Token
4. Generate API Key
5. Access Protected APIs

---

# 🌍 Available APIs

## Authentication APIs

### Register

```http
POST /auth/register
```

### Login

```http
POST /auth/login
```

---

## Location APIs

### Get States

```http
GET /location/states
```

### Get Districts

```http
GET /location/districts/{state_id}
```

### Get Villages

```http
GET /location/villages/{district_id}
```

### Search Villages

```http
GET /location/search?q=village_name
```

### Usage Analytics

```http
GET /location/usage-count
```

---

# 🔑 Headers Required

```http
Authorization: Bearer <JWT_TOKEN>
```

```http
x-api-key: <YOUR_API_KEY>
```

---

# 📸 Dashboard Modules

* Authentication Status
* API Key Generator
* States Explorer
* District Explorer
* Village Explorer
* Search System
* Usage Analytics

---

# 🎯 Future Improvements

* Map Integration
* Admin Dashboard
* Export APIs
* Dark Mode
* Charts & Graphs
* Rate Limiting
* API Documentation Portal

---

# 👨‍💻 Author

## Abhay Yadav

Full Stack Developer 🚀

---

# ⭐ Support

If you like this project:

⭐ Star the Repository
⭐ Fork the Project
⭐ Contribute to Improvements

---

# 📜 License

This project is licensed under the MIT License.
