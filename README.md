# 📝 Product Requirements Document (PRD)

## Project Title: **User Login System using Flask-WTF**

---

## 🔍 Objective

The goal of this project is to develop a secure and functional **user login interface** using the Flask web framework. The application handles form rendering, validation, and simple session logic using **Flask-WTF** and **WTForms**.

---

## ✅ Functional Requirements

### 1. Login Page
- **URL:** `/login`
- **Features:**
  - Form Fields:
    - `username`: Text field
    - `password`: Password field
    - `remember_me`: Boolean checkbox
  - `submit`: Submit button with label "Sign In"
  - Form validation for required fields
  - CSRF protection

### 2. Homepage Route
- **URL:** `/`
- Redirects to `/login` or displays a basic homepage (if implemented)

### 3. Post-Login Flash Feedback
- After successful form submission:
  - Shows a flash message with username and `remember_me` status
  - Redirects to `/index`

---

## 🗂️ Folder Structure

project-root/
│
├── app/
│ ├── init.py # Initializes the Flask app and loads config
│ ├── routes.py # Application routes and view logic
│ ├── forms.py # WTForm for login
│ ├── config.py # Configuration file (secret key, etc.)
│ └── templates/
│ ├── base.html # Base HTML layout with navigation and flash
│ └── login.html # Login form template
│
├── venv/ # Python virtual environment
└── run.py (optional) # Entry point (if using)

yaml
Copy
Edit
## ⚙️ Tech Stack

- **Backend:** Python 3.x, Flask
- **Forms:** Flask-WTF, WTForms
- **Templating Engine:** Jinja2 (HTML)
- **Frontend:** Basic HTML (can be enhanced with CSS or Bootstrap)

---

## 🔐 Security Features

- CSRF protection via `FlaskForm`
- Flask `SECRET_KEY` for session security
- Input validation with `DataRequired()` validator
## 👨‍💻 Author

**Devasye Sachdeva**  
This is a beginner-friendly Flask app built for learning form validation and session handling.

---
