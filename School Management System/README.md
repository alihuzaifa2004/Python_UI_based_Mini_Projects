## 🏫 School Management System

A full-featured School Management System built with **Python**, **Tkinter GUI**, and **JSON** for data persistence. This application supports three user roles — **Student**, **Teacher**, and **Admin** — with tailored dashboards and functionalities for each.

---

### 🚀 Features

#### 👩‍🎓 Student

* Register/Login
* Enroll in available classes
* View class schedule
* View grades uploaded by teachers

#### 👨‍🏫 Teacher

* Register/Login
* View assigned classes
* Upload student grades

#### 🛠 Admin

* Register/Login
* Create/edit/delete classes
* Assign teachers to classes
* View all students, teachers, and classes

---

### 📂 Project Structure

```
school_management_system/
├── main.py              # Launchpad: Login and Registration GUI
├── auth.py              # Handles login and registration logic
├── student.py           # Student dashboard and functions
├── teacher.py           # Teacher dashboard and functions
├── admin.py             # Admin dashboard and class management
├── grades.py            # Grade upload/view logic
├── schedule.py          # Optional: Scheduling logic (placeholder)
├── database.py          # JSON file handler for users, classes, and grades
├── utils.py             # (Optional) Reusable helper functions
├── data/
│   ├── users.json       # User data: usernames, passwords, roles
│   ├── classes.json     # Class data: subjects, schedules, students
│   └── grades.json      # Grade data: student marks per class
└── README.md            # Project documentation
```

---

### 🧠 Data Models (ERD Summary)

#### User

* `username`
* `password`
* `role` (student | teacher | admin)

#### Class

* `class_id`
* `subject`
* `schedule`
* `teacher`
* `students` (list)

#### Grade

* `student`
* `class`
* `marks`

---

### 🎯 Use Case Summary

#### Student:

* Login/Register
* Enroll in classes
* View schedule
* View grades

#### Teacher:

* Login/Register
* View assigned classes
* Upload grades for enrolled students

#### Admin:

* Login/Register
* Add/delete users
* Create classes
* Assign teachers to classes
* View reports

---

### 💾 Setup Instructions

1. **Install Python (>= 3.7)**

2. **Clone this repository or download the ZIP**

3. **Create `data` folder** in the project root and add three JSON files:

   * `users.json` – `{}` (empty object)
   * `classes.json` – `{}` (empty object)
   * `grades.json` – `{}` (empty object)

4. **Run the application**

```bash
python main.py
```

---

### 📸 Screenshots (Optional)

*Add images of Student, Teacher, and Admin dashboards here.*

---

### 📘 Requirements

* Python 3.7+
* Tkinter (comes with Python standard library)

---

### 📌 Notes

* This version uses **JSON files** to simulate a simple persistent database.
* For scalability, you can replace JSON with SQLite or PostgreSQL.
* Error handling is basic — could be extended for production use.

---

### ✨ Future Enhancements

* Add class editing & deletion features
* Add password recovery
* Use SQLite or a proper database
* Export reports to PDF or Excel
* Improve GUI styling (e.g., themes, frames, tabs)

---

### 📄 License

This project is licensed under the MIT License. Feel free to use and modify it for educational or commercial purposes.
