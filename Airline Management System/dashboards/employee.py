import tkinter as tk
from tkinter import messagebox
from core.flight_ops import load_flights
from core.database import read_json, write_json

ASSIGN_PATH = "data/employees/assignments.json"

def employee_dashboard(username, logout_callback):
    win = tk.Toplevel()
    win.title("Employee Dashboard")
    
    tk.Label(win, text="Employee Portal", font=("Arial", 16)).pack(pady=10)
    win.geometry("500x500")
    win.protocol("WM_DELETE_WINDOW", lambda: (logout_callback(), win.destroy()))

    tk.Label(win, text=f"Welcome {username}", font=("Arial", 16)).pack(pady=10)

    # --- Section 1: Select Role ---
    tk.Label(win, text="🧑 Select Your Role", font=("Arial", 12)).pack()
    role_var = tk.StringVar(value="pilot")
    tk.OptionMenu(win, role_var, "pilot", "air_hostess", "ground_staff", "technician").pack(pady=5)

    # Show role responsibilities
    info_label = tk.Label(win, text="", fg="blue", wraplength=400, justify="left")
    info_label.pack(pady=5)

    def show_role_details():
        role = role_var.get()
        if role == "pilot":
            details = "🛫 View flight schedule\n🌦️ Weather report\n✈️ Aircraft checklist"
        elif role == "air_hostess":
            details = "🧾 View passenger list\n🧃 Service checklist\n🪑 Assigned seat map"
        elif role == "ground_staff":
            details = "🛄 Manage luggage\n🚪 Coordinate boarding\n🧭 Gate management"
        elif role == "technician":
            details = "🔧 Maintenance logs\n📋 Safety checklist\n⚙️ Equipment status"
        else:
            details = "No responsibilities available."
        info_label.config(text=f"📌 Responsibilities:\n{details}")

    tk.Button(win, text="View Role Duties", command=show_role_details).pack(pady=5)

    # --- Section 2: Flight Employment Submission ---
    tk.Label(win, text="✈️ Flight Employment Submission", font=("Arial", 12)).pack(pady=10)

    flights = load_flights()
    valid_flights = [f for f in flights if isinstance(f, dict) and "id" in f]
    if not valid_flights:
        messagebox.showinfo("No Flights", "No flights available to assign.")
        win.destroy()
        return

    flight_options = [f"{f['id']} - {f['origin']} → {f['destination']} | {f['date']}" for f in valid_flights]
    flight_map = {f"{f['id']} - {f['origin']} → {f['destination']} | {f['date']}": f for f in valid_flights}
    selected_flight_label = tk.StringVar(value=flight_options[0])
    tk.OptionMenu(win, selected_flight_label, *flight_options).pack(pady=5)

    def submit_assignment():
        flight_label = selected_flight_label.get()
        flight = flight_map.get(flight_label)
        role = role_var.get()

        if not flight:
            messagebox.showerror("Error", "Please select a valid flight.")
            return

        # Load current assignments
        data = read_json(ASSIGN_PATH)
        if not isinstance(data, list):
            data = []

        # Store assignment
        data.append({
            "employee": username,
            "role": role,
            "flight_id": flight["id"],
            "origin": flight["origin"],
            "destination": flight["destination"],
            "date": flight["date"],
            "time": flight["time"]
        })
        write_json(ASSIGN_PATH, data)

        messagebox.showinfo("Submitted", f"You are assigned as a {role} on flight {flight['id']}")
        info_label.config(text="✅  Submitted!")

    tk.Button(win, text="Submit ", command=submit_assignment, bg="green", fg="white").pack(pady=10)

    # --- Logout Button ---
    def logout():
        logout_callback()
        win.destroy()

    tk.Button(win, text="Logout", command=logout, fg="white", bg="red").pack(pady=20)
