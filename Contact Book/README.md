
# 📞 Contact Book – Streamlit Web App

## Overview

The **Contact Book** is a simple and interactive web-based application built using [Streamlit](https://streamlit.io/) and Python. It allows users to **Add**, **Search**, **Update**, **Delete**, and **View** contact information, storing data in a JSON file (`contact.json`).

---

## 🚀 Features

- **Add Contact**: Store a new contact with name, phone number, and email.
- **Search Contact**: Retrieve contact details using a name.
- **Update Contact**: Modify existing phone number or email of a contact.
- **Delete Contact**: Remove a contact from the list.
- **Show Contact List**: Display all saved contacts with their details.

---

## 📁 Project Structure

```
📁 project-directory/
│
├── contact.json         # Data storage file for contacts (auto-created)
├── app.py               # Main Streamlit app file
└── README.md            # Project description and usage
```

---

## 🧠 Application Logic

### 1. **Data Storage**
- Contacts are stored in a **JSON** file named `contact.json` as a dictionary:
  ```json
  {
    "John Doe": {
      "Phone": "1234567890",
      "Email": "john@example.com"
    }
  }
  ```

### 2. **Functions**
- `load_contact()`: Reads the JSON file and loads contact data.
- `save_contact(contact)`: Writes updated contact data to the file.
- `add_contact(name, email, phone_no)`: Adds a new contact.
- `search_contact(name)`: Retrieves contact details by name.
- `update_contact(name, phone_no, email)`: Updates phone/email for a contact.
- `del_contact(name)`: Deletes a contact.

### 3. **Streamlit Interface**
- Uses a sidebar menu to choose the action.
- Each action (Add, Search, Update, Delete, Show) has its own input forms and feedback messages.
- Contact list is displayed with names and associated details.

---

## ✅ Key Technologies

| Tech         | Purpose                             |
|--------------|-------------------------------------|
| **Python**   | Core programming logic              |
| **Streamlit**| Web UI framework                    |
| **JSON**     | Contact data storage (lightweight)  |
| **OS module**| File path checking and management   |

---

## 📌 How to Run

1. **Install Streamlit** (if not already):
   ```bash
   pip install streamlit
   ```

2. **Run the app**:
   ```bash
   streamlit run app.py
   ```

3. The app will open in your browser at:
   ```
   http://localhost:8501
   ```

---

## 💡 Notes

- Make sure `contact.json` is in the same directory as `app.py` (it will be created if not present).
- Names are used as **unique keys**. To prevent overwriting, avoid duplicating names.
- This app is intended for **educational/demo purposes** and not for production use.

---

## 🛠️ Future Improvements

- Add validation for phone and email formats.
- Export/import contacts.
- Add contact images or address fields.
- Use a database (e.g., SQLite) for larger-scale data.

---

## 📬 Contact

For improvements or feedback, feel free to connect.

---
