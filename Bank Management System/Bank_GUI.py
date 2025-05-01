import streamlit as st
import json
import os

# File to store accounts
ACCOUNT_FILE = "accounts.json"

# Load accounts from file
def load_accounts():
    if os.path.exists(ACCOUNT_FILE):
        with open(ACCOUNT_FILE, "r") as file:
            return json.load(file)
    return {}

# Save accounts to file
def save_accounts(accounts):
    with open(ACCOUNT_FILE, "w") as file:
        json.dump(accounts, file, indent=4)

# Initialize session state
if "accounts" not in st.session_state:
    st.session_state.accounts = load_accounts()

if "selected_account" not in st.session_state:
    st.session_state.selected_account = None

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# App title
st.title("🏦 Simple Bank System")

# Sidebar navigation
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
        if name in st.session_state.accounts:
            st.warning("Account already exists!")
        else:
            # Save the account with personal details, initial balance, and password
            st.session_state.accounts[name] = {
                "balance": 0,
                "dob": str(dob),
                "age": age,
                "city": city,
                "nic": nic,
                "address": address,
                "password": password  # Store the password (should be hashed in real-world applications)
            }
            save_accounts(st.session_state.accounts)
            st.success(f"Account for {name} created successfully with a balance of $0.")

# Select and operate on an account
elif menu == "Select Account":
    st.header("Account Operations")
    if not st.session_state.accounts:
        st.info("No accounts available. Please create one first.")
    else:
        if not st.session_state.logged_in:
            # Login section
            name = st.selectbox("Select an account:", list(st.session_state.accounts.keys()))
            password = st.text_input("Enter your password to proceed:", type="password")

            if st.button("Login"):
                # Check if password is correct
                if password == st.session_state.accounts[name]["password"]:
                    st.session_state.selected_account = name
                    st.session_state.logged_in = True
                    st.subheader(f"Welcome, {name}!")
                    st.write(f"**Current Balance**: ${st.session_state.accounts[name]['balance']:.2f}")
                else:
                    st.error("Incorrect password! Please try again.")
        else:
            # Logged in section - perform transactions
            name = st.session_state.selected_account

            st.subheader(f"Welcome back, {name}!")
            st.write(f"**Current Balance**: ${st.session_state.accounts[name]['balance']:.2f}")

            # Deposit
            deposit_amount = st.number_input("Deposit amount:", min_value=0.0, step=0.01)
            if st.button("Deposit"):
                if deposit_amount > 0:
                    st.session_state.accounts[name]['balance'] += deposit_amount
                    save_accounts(st.session_state.accounts)
                    st.success(f"${deposit_amount} deposited into {name}'s account.")
                else:
                    st.error("Deposit amount must be greater than 0.")

            # Withdraw
            withdraw_amount = st.number_input("Withdraw amount:", min_value=0.0, step=0.01)
            if st.button("Withdraw"):
                if withdraw_amount > st.session_state.accounts[name]['balance']:
                    st.error("Insufficient funds!")
                elif withdraw_amount > 0:
                    st.session_state.accounts[name]['balance'] -= withdraw_amount
                    save_accounts(st.session_state.accounts)
                    st.success(f"${withdraw_amount} withdrawn from {name}'s account.")
                else:
                    st.error("Withdraw amount must be greater than 0.")

            # Logout option
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.session_state.selected_account = None
                st.success("Logged out successfully!")

# Delete account
elif menu == "Delete Account":
    st.header("Delete an Account")
    if not st.session_state.accounts:
        st.info("No accounts to delete.")
    else:
        name = st.selectbox("Select an account to delete:", list(st.session_state.accounts.keys()))
        if name:
            # Ask for confirmation before deleting
            confirm = st.radio(f"Are you sure you want to delete the account for {name}?", ["No", "Yes"])
            if confirm == "Yes" and st.button("Delete Account"):
                # Delete the account and save the changes
                del st.session_state.accounts[name]
                save_accounts(st.session_state.accounts)
                st.success(f"Account for {name} has been deleted.")
            elif confirm == "No":
                st.info("Account deletion cancelled.")

# Exit (displayed just for UI consistency)
elif menu == "Exit":
    st.info("Thank you for using the banking system!")
