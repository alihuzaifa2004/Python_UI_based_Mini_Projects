
# 🧑‍🎓 Student Management System (Streamlit)

This is a simple Student Management System built using **Python** and **Streamlit** that allows users to **add**, **update**, **delete**, and **view** student records stored in a JSON file.

---

## 🚀 Features

- 📥 **Add Student**: Enter student ID, name, age, and city to add a new student.
- ✏️ **Update Student**: Modify details of an existing student using their student ID.
- 🗑️ **Delete Student**: Remove a student entry by providing their student ID.
- 📋 **View All Students**: Display all student records in a neatly formatted table.

---

## 🧠 Logic & Key Components

### 🔹 Data Handling
- Student records are stored in a local JSON file named `data.json`.
- On app launch, the file is read (or created if not present) to load existing student data.
- Data is stored in a dictionary format where keys are student IDs and values contain details.

### 🔹 Functions
- `add_student()`: Adds new student to the JSON file.
- `update_student()`: Searches by ID and updates name, age, or city.
- `delete_student()`: Deletes a student by ID.
- `view_all_students()`: Displays all data in table format using `st.table()`.

### 🔹 Streamlit UI
- A sidebar menu is used to switch between actions.
- Dynamic forms for each action (Add, Update, Delete, View).
- Input validations ensure fields are not left empty.

---

## 📁 JSON Structure

```
{
  "1001": {
    "name": "Alice",
    "Age": 21,
    "Id": "1001",
    "City": "Lahore"
  },
  "1002": {
    "name": "Bob",
    "Age": 22,
    "Id": "1002",
    "City": "Karachi"
  }
}
```

---

## 💻 How to Run

1. Install Streamlit if not already installed:
```bash
pip install streamlit
```

2. Save the Python file (e.g., `student_management.py`) and run:
```bash
streamlit run student_management.py
```

---

## 📌 Requirements

- Python 3.x
- Streamlit
- JSON (built-in module)
- OS (built-in module)

---

## 🏁 Conclusion

This project demonstrates a clean way to manage basic CRUD operations with JSON files in a Streamlit UI, great for beginners learning Python, Streamlit, or file-based data handling.

---

## 🛠️ Author

Developed by Ali Huzaifa – Customize this to add more features such as search, filter, or exporting to CSV.
