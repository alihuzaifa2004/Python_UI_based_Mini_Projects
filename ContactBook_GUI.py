import streamlit as st
import json
import os

CONTACT_FILE = "contact.json"

# Load contacts
def load_contact():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

# Save contacts
def save_contact(contact):
    with open(CONTACT_FILE, "w") as file:
        json.dump(contact, file, indent=4)

# Add contact
def add_contact(name, email, phone_no):
    contact = load_contact()
    contact[name] = {"Phone": phone_no, "Email": email}
    save_contact(contact)

# Search contact
def search_contact(name):
    contact = load_contact()
    return contact.get(name, None)

# Update contact
def update_contact(name, phone_no=None, email=None):
    contact = load_contact()
    if name in contact:
        if phone_no:
            contact[name]["Phone"] = phone_no
        if email:
            contact[name]["Email"] = email
        save_contact(contact)
        return True
    return False

# Delete contact
def del_contact(name):
    contact = load_contact()
    if name in contact:
        del contact[name]
        save_contact(contact)
        return True
    return False

# Streamlit UI
st.title("📞 Contact Book")

menu = st.sidebar.radio("Choose an action", 
                        ["Add Contact", "Search Contact", "Update Contact", "Delete Contact", "Show Contact List"])

if menu == "Add Contact":
    st.subheader("➕ Add New Contact")
    name = st.text_input("Enter Name")
    email = st.text_input("Enter Email")
    phone = st.text_input("Enter Phone No")

    if st.button("Save Contact"):
        if name and email and phone:
            add_contact(name, email, phone)
            st.success(f"Contact '{name}' added.")
        else:
            st.warning("Please fill all fields.")

elif menu == "Search Contact":
    st.subheader("🔍 Search Contact")
    name = st.text_input("Enter Name to Search")
    if st.button("Search"):
        result = search_contact(name)
        if result:
            st.info(f"📞 Phone: {result['Phone']}")
            st.info(f"📧 Email: {result['Email']}")
        else:
            st.error("Contact not found.")

elif menu == "Update Contact":
    st.subheader("✏️ Update Contact")
    name = st.text_input("Enter Name to Update")
    new_phone = st.text_input("New Phone No (leave blank to skip)")
    new_email = st.text_input("New Email (leave blank to skip)")

    if st.button("Update Contact"):
        success = update_contact(name, new_phone or None, new_email or None)
        if success:
            st.success(f"Contact '{name}' updated.")
        else:
            st.error("Contact not found.")

elif menu == "Delete Contact":
    st.subheader("🗑️ Delete Contact")
    name = st.text_input("Enter Name to Delete")
    if st.button("Delete Contact"):
        success = del_contact(name)
        if success:
            st.success(f"Contact '{name}' deleted.")
        else:
            st.error("Contact not found.")

elif menu == "Show Contact List":
    st.subheader("📋 All Contacts")
    contact = load_contact()
    if contact:
        for name, details in contact.items():
            st.markdown(f"**{name}**")
            st.markdown(f"- 📞 Phone: {details['Phone']}")
            st.markdown(f"- 📧 Email: {details['Email']}")
            st.markdown("---")
    else:
        st.info("No contacts available.")
