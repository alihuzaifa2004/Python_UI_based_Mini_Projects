# 🏦 Simple Bank System using Streamlit & SQL Server

This is a **Streamlit-based web application** for managing simple banking operations using **SQL Server** for data storage. Users can create accounts, log in, deposit or withdraw money, and delete accounts. The application uses **Windows Authentication** to connect to SQL Server.

---

## 📌 Features

- ✅ Create a new account
- 🔐 Login with password
- 💰 Deposit and withdraw money
- 🗑️ Delete existing account
- 🧾 Balance inquiry
- 🔒 Logout securely

---

## 🧠 Project Logic

- **Database**: SQL Server with a table `Accounts` to store user data
- **Authentication**: Users must enter their password to access their account
- **Session Management**: Handled using `st.session_state` to manage login sessions
- **SQL Operations**: Insert, Select, Update, Delete using `pyodbc` library
- **Form Inputs**: Streamlit widgets for user-friendly data input

---

## 🗃️ Table Schema

```sql
CREATE DATABASE BankSystemDB;
GO

USE BankSystemDB;
GO

CREATE TABLE Accounts (
    Name NVARCHAR(100) PRIMARY KEY,
    DOB DATE,
    Age INT,
    City NVARCHAR(100),
    NIC NVARCHAR(50),
    Address NVARCHAR(255),
    Password NVARCHAR(100),
    Balance FLOAT
);
```

---

## 💡 How to Run

1. Ensure SQL Server is running with the instance `SQLEXPRESS`.
2. Create the database and table using the schema above.
3. Install dependencies:
   ```bash
   pip install streamlit pyodbc
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## 🛡️ Important Notes

- Make sure to adjust the server and instance name in `get_connection()` function as per your SQL Server setup.
- This app uses **Windows Authentication** (no SQL login/password required).
- Do **not** use this app for real banking use — it is for **educational purposes only**.

---

## 📁 File Structure

```
app.py           # Main Streamlit application
README.md        # Project description and instructions
```

---

## 📞 Contact

For queries or support, please contact the project maintainer.
