import streamlit as st
import pyodbc

# SQL Server connection using Windows Authentication
def get_connection():
    return pyodbc.connect(
        r'DRIVER={SQL Server};'
        r'SERVER=DESKTOP-I1VB32G\SQLEXPRESS;'
        r'DATABASE=BankSystemDB;'
        r'Trusted_Connection=yes;'
    )

# Initialize session state
if "selected_account" not in st.session_state:
    st.session_state.selected_account = None

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("🏦 Simple Bank System (SQL Server)")

menu = st.sidebar.radio("Menu", ["Add Account", "Select Account", "Delete Account", "Exit"])

# Add account
if menu == "Add Account":
    st.header("Create a New Account")
    name = st.text_input("Full Name:")
    dob = st.date_input("Date of Birth")
    age = st.number_input("Age", min_value=1, step=1)
    city = st.text_input("City")
    nic = st.text_input("NIC Number")
    address = st.text_area("Address")
    password = st.text_input("Password", type="password")

    if st.button("Create Account"):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Name FROM Accounts WHERE Name = ?", name)
            if cursor.fetchone():
                st.warning("Account already exists!")
            else:
                cursor.execute(
                "INSERT INTO Accounts (Name, DOB, Age, City, NIC, Address, Password, Balance) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (name, str(dob), age, city, nic, address, password, 0.0)
                )

                conn.commit()
                st.success(f"Account for {name} created successfully.")

# Select account (Login and Transactions)
elif menu == "Select Account":
    st.header("Account Operations")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT Name FROM Accounts")
        accounts = [row[0] for row in cursor.fetchall()]

    if not accounts:
        st.info("No accounts available.")
    else:
        if not st.session_state.logged_in:
            name = st.selectbox("Select an account:", accounts)
            password = st.text_input("Enter your password:", type="password")

            if st.button("Login"):
                with get_connection() as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT Password FROM Accounts WHERE Name = ?", name)
                    result = cursor.fetchone()
                    if result and result[0] == password:
                        st.session_state.selected_account = name
                        st.session_state.logged_in = True
                        st.success(f"Welcome, {name}!")
                    else:
                        st.error("Incorrect password!")

        else:
            name = st.session_state.selected_account
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT Balance FROM Accounts WHERE Name = ?", name)
                balance = cursor.fetchone()[0]

            st.subheader(f"Welcome back, {name}!")
            st.write(f"**Current Balance**: ${balance:.2f}")

            deposit_amount = st.number_input("Deposit amount:", min_value=0.0, step=0.01)
            if st.button("Deposit"):
                if deposit_amount > 0:
                    with get_connection() as conn:
                        cursor = conn.cursor()
                        cursor.execute("UPDATE Accounts SET Balance = Balance + ? WHERE Name = ?", deposit_amount, name)
                        conn.commit()
                        st.success(f"${deposit_amount:.2f} deposited.")
                else:
                    st.error("Amount must be greater than 0.")

            withdraw_amount = st.number_input("Withdraw amount:", min_value=0.0, step=0.01)
            if st.button("Withdraw"):
                if withdraw_amount > balance:
                    st.error("Insufficient funds!")
                elif withdraw_amount > 0:
                    with get_connection() as conn:
                        cursor = conn.cursor()
                        cursor.execute("UPDATE Accounts SET Balance = Balance - ? WHERE Name = ?", withdraw_amount, name)
                        conn.commit()
                        st.success(f"${withdraw_amount:.2f} withdrawn.")
                else:
                    st.error("Amount must be greater than 0.")

            if st.button("Logout"):
                st.session_state.logged_in = False
                st.session_state.selected_account = None
                st.success("Logged out.")

# Delete Account
elif menu == "Delete Account":
    st.header("Delete an Account")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT Name FROM Accounts")
        accounts = [row[0] for row in cursor.fetchall()]

    if not accounts:
        st.info("No accounts available.")
    else:
        name = st.selectbox("Select an account to delete:", accounts)
        confirm = st.radio(f"Are you sure you want to delete '{name}'?", ["No", "Yes"])
        if confirm == "Yes" and st.button("Delete Account"):
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Accounts WHERE Name = ?", name)
                conn.commit()
                st.success(f"Account '{name}' deleted successfully.")

# Exit
elif menu == "Exit":
    st.info("Thank you for using the banking system!")

