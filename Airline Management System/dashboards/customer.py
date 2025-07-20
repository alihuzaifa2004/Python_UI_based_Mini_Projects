import tkinter as tk
from tkinter import messagebox
from core.flight_ops import load_flights
from core.database import read_json, write_json

BOOKING_PATH = "data/bookings/bookings.json"

def customer_dashboard(username, logout_callback):
    win = tk.Toplevel()
    win.title("Customer Dashboard")
    tk.Label(win, text="Customer Portal", font=("Arial", 16)).pack(pady=5)
    
    win.geometry("400x450")
    win.protocol("WM_DELETE_WINDOW", lambda: (logout_callback(), win.destroy()))

    tk.Label(win, text=f"Welcome {username}", font=("Arial", 10)).pack(pady=10)

    def view_flights():
        flights = load_flights()
        valid_flights = [
            f for f in flights
            if isinstance(f, dict) and all(k in f for k in ("id", "origin", "destination", "date", "time"))
        ]
        if not valid_flights:
            messagebox.showinfo("Available Flights", "No valid flights available.")
            return

        msg = "\n".join([
            f"{f['id']}: {f['origin']} → {f['destination']} | {f['date']} at {f['time']}"
            for f in valid_flights
        ])
        messagebox.showinfo("Available Flights", msg)

    def book_flight():
        flights = load_flights()
        flight_ids = [f["id"] for f in flights if "id" in f]
        if not flight_ids:
            messagebox.showinfo("Book Flight", "No flights available to book.")
            return

        book_win = tk.Toplevel(win)
        book_win.title("Book Flight")
        book_win.geometry("300x250")
        tk.Label(book_win, text="Booking Portal").pack(pady=10)
        tk.Label(book_win, text="Enter Flight ID to book:").pack(pady=5)
        entry = tk.Entry(book_win)
        entry.pack(pady=5)

        def submit_booking():
            flight_id = entry.get().strip()
            if flight_id not in flight_ids:
                messagebox.showerror("Error", "Invalid Flight ID")
                return

            bookings = read_json(BOOKING_PATH)
            if not isinstance(bookings, list):
                bookings = []

            selected_flight = next((f for f in flights if f.get("id") == flight_id), None)
            if not selected_flight:
                messagebox.showerror("Error", "Flight details not found.")
                return

            selected_date = selected_flight.get("date")
            if not selected_date:
                messagebox.showerror("Error", "Selected flight does not have a date.")
                return

            # Prevent booking multiple flights on the same date
            for b in bookings:
                if b.get("user") == username:
                    booked_flight = next((f for f in flights if f.get("id") == b.get("flight_id")), None)
                    if booked_flight and booked_flight.get("date") == selected_date:
                        messagebox.showerror("Error", f"You already booked a flight on {selected_date}.")
                        return

            bookings.append({"user": username, "flight_id": flight_id})
            write_json(BOOKING_PATH, bookings)
            messagebox.showinfo("Booked", f"Flight {flight_id} booked successfully!")
            book_win.destroy()

        tk.Button(book_win, text="Submit", command=submit_booking).pack(pady=10)

    def view_booked_flights():
        bookings = read_json(BOOKING_PATH)
        flights = load_flights()
        user_bookings = [b for b in bookings if b.get("user") == username]

        if not user_bookings:
            messagebox.showinfo("My Bookings", "No bookings found.")
            return

        booked_details = []
        for b in user_bookings:
            flight = next((f for f in flights if f.get("id") == b["flight_id"]), None)
            if flight:
                booked_details.append(
                    f"{flight['id']}: {flight['origin']} → {flight['destination']} | {flight.get('date', 'N/A')} at {flight.get('time', '')}"
                )
            else:
                booked_details.append(f"{b['flight_id']}: (details unavailable)")

        msg = "\n".join(booked_details)
        messagebox.showinfo("My Booked Flights", msg)

    def search_flight():
        search_win = tk.Toplevel(win)
        search_win.title("Search Flights")
        search_win.geometry("300x250")
        tk.Label(search_win, text="Search Flights", font=("Arial", 16)).pack(pady=10)


        tk.Label(search_win, text="Origin").pack()
        origin_entry = tk.Entry(search_win)
        origin_entry.pack()

        tk.Label(search_win, text="Destination").pack()
        dest_entry = tk.Entry(search_win)
        dest_entry.pack()

        tk.Label(search_win, text="Date (YYYY-MM-DD) (optional)").pack()
        date_entry = tk.Entry(search_win)
        date_entry.pack()

        def perform_search():
            origin = origin_entry.get().strip().lower()
            dest = dest_entry.get().strip().lower()
            date = date_entry.get().strip()

            flights = load_flights()

            matches = [
                f for f in flights
                if f.get("origin", "").lower() == origin and
                f.get("destination", "").lower() == dest and
                (not date or f.get("date") == date)
            ]

            if not matches:
                messagebox.showinfo("Search Results", "No matching flights found.")
                return

            msg = "\n".join([
                f"{f['id']}: {f['origin']} → {f['destination']} | {f['date']} at {f['time']}"
                for f in matches
            ])
            messagebox.showinfo("Matching Flights", msg)

        tk.Button(search_win, text="Search", command=perform_search).pack(pady=10)

    def logout():
        logout_callback()
        win.destroy()

    # Buttons
    tk.Button(win, text="View Flights", command=view_flights).pack(pady=10)
    tk.Button(win, text="Search Flight", command=search_flight).pack(pady=10)
    tk.Button(win, text="Book Flight", command=book_flight).pack(pady=10)
    tk.Button(win, text="View Booked Flights", command=view_booked_flights).pack(pady=10)
    tk.Button(win, text="Logout", command=logout, fg="white", bg="red").pack(pady=10)
