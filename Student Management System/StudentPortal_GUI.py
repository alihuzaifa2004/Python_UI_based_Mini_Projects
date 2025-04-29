import streamlit as st
import json
import os

filename = "data.json"

# Load existing data or create a new file if not exists
if os.path.exists(filename):
    with open(filename, "r") as file:
        try:
            all_data = json.load(file)
        except json.JSONDecodeError:
            all_data = {}
else:
    all_data = {}

# Function to add new student
def add_student():
    student_id = st.text_input("Enter Student ID")
    name = st.text_input("Enter Name")
    age = st.number_input("Enter Age", min_value=0, max_value=120)
    city = st.text_input("Enter City")

    if st.button("Add Student"):
        if student_id and name and city:
            all_data[student_id] = {
                "name": name,
                "Age": age,
                "Id": student_id,
                "City": city
            }
            with open(filename, "w") as file:
                json.dump(all_data, file, indent=4)
            st.success(f"Student {student_id} added successfully.")
        else:
            st.error("Please fill out all fields!")

# Function to update student data
def update_student():
    student_id = st.text_input("Enter the Student ID to update")
    if student_id in all_data:
        st.write(f"Current data: {all_data[student_id]}")

        name = st.text_input("Enter new Name (leave blank to keep current)", value=all_data[student_id]["name"])
        age_input = st.number_input("Enter new Age (leave blank to keep current)", value=all_data[student_id]["Age"])
        city = st.text_input("Enter new City (leave blank to keep current)", value=all_data[student_id]["City"])

        if st.button("Update Student"):
            if name != "":
                all_data[student_id]["name"] = name
            if age_input != 0:
                all_data[student_id]["Age"] = age_input
            if city != "":
                all_data[student_id]["City"] = city

            with open(filename, "w") as file:
                json.dump(all_data, file, indent=4)
            st.success(f"Student {student_id} updated successfully.")
    else:
        st.error("Student ID not found.")

# Function to delete a student
def delete_student():
    student_id = st.text_input("Enter the Student ID to delete")
    if st.button("Delete Student"):
        if student_id in all_data:
            del all_data[student_id]
            with open(filename, "w") as file:
                json.dump(all_data, file, indent=4)
            st.success(f"Student {student_id} deleted successfully.")
        else:
            st.error("Student ID not found.")

def view_all_students():
    if all_data:
        st.write("### All Students Data:")
        
        # Convert dictionary to list of dictionaries for display
        student_list = []
        for student_id, details in all_data.items():
            student_entry = {
                "ID": student_id,
                "Name": details["name"],
                "Age": details["Age"],
                "City": details["City"]
            }
            student_list.append(student_entry)

        # Display as a table
        st.table(student_list)  # You can also use st.dataframe(student_list) for interactivity
    else:
        st.info("No student data available.")


# Streamlit App UI
st.title("Student Management System")

# Menu for actions
st.sidebar.title("Menu")
menu_choice = st.sidebar.radio(
    "Choose an option",
    ("Add Student", "Update Student", "Delete Student", "View All Students")
)

if menu_choice == "Add Student":
    add_student()
elif menu_choice == "Update Student":
    update_student()
elif menu_choice == "Delete Student":
    delete_student()
elif menu_choice == "View All Students":
    view_all_students()

