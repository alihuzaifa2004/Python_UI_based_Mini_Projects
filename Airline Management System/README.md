# ✈️ Airline Reservation Management System

A **GUI-based Airline Reservation System** built using **Python and Tkinter**, storing data in **JSON files**. It supports multiple user roles: **Admin**, **Employee**, and **Customer** — each with dedicated dashboards and functionalities.

---

## 📌 Key Highlights

- 🎛️ Multi-role login system: **Admin**, **Employee**, and **Customer**
- 📅 Date-based flight management with conflict checks
- 🔍 Flight search functionality by **origin**, **destination**, and optional **date**
- 🚫 Prevent duplicate flight entries and booking conflicts
- 💡 Built without external database dependencies – perfect for quick deployment and learning

---

## 📁 Project Structure

```

airline\_system/
│
├── main.py                        # App entry point (Login & Role Routing)
│
├── dashboards/                    # Role-based dashboards
│   ├── admin.py                   # Admin panel for managing flights
│   ├── employee.py                # Employee panel for service assignment
│   └── customer.py                # Customer panel for booking/searching
│
├── ui/                            # User interface components (login/register)
│   ├── login.py
│   ├── register.py
│   └── components.py              # (Optional) shared UI widgets
│
├── core/                          # Core logic
│   ├── auth.py                    # Authentication functions
│   ├── database.py                # JSON read/write handlers
│   └── flight\_ops.py              # Flight data operations (CRUD)
│
├── data/
│   ├── users/
│   │   ├── admins.json            # Admin user data
│   │   ├── staff.json             # Employee user data
│   │   └── customers.json         # Customer user data
│   ├── flights/
│   │   └── flights.json           # Flight schedule data
│   └── bookings/
│       └── bookings.json          # Booking records
│
└── README.md

````

## 👤 User Roles & Functionalities

### 🛫 Admin
- ➕ Add new flights with **unique flight ID**, **origin**, **destination**, **date**, and **time**
- 🧹 Prevents flight ID duplication
- 👀 View a list of all scheduled flights
- 📅 Includes validations for proper date/time formats

---

### 🧑‍✈️ Employee
- ✈️ Choose a flight from the current schedule
- 🛠️ Select a service role such as **Pilot**, **Air Hostess**, or **Ground Staff**
- 📝 Submit assignment to the selected flight
- 🚧 Upcoming: View list of assigned flights or shift overview

---

### 🧍 Customer
- 📋 View list of all available flights
- 🔎 Search flights by **origin**, **destination**, and (optional) **date**
- 🛑 Prevents booking multiple flights on the same date
- ✅ Book flights using flight ID
- 📖 View previously booked flights in a readable format

---

## 💾 Data Storage (JSON-based)

| File Path | Purpose |
|-----------|---------|
| `data/users/admins.json` | Stores admin credentials |
| `data/users/staff.json` | Stores employee credentials |
| `data/users/customers.json` | Stores customer accounts |
| `data/flights/flights.json` | All flight details |
| `data/bookings/bookings.json` | All customer bookings |

This approach ensures:
- Lightweight implementation (no database setup)
- Easy portability and readability
- Beginner-friendly for learning file-based persistence

---

## 🧪 How to Run

### 📦 Requirements

- Python 3.9+  
- Tkinter (comes pre-installed with Python)

### ▶️ Run the App

```bash
python main.py
````

Once launched, users can choose to **Login** or **Register**, and based on role, will be redirected accordingly.

---

## 🔐 Authentication Flow

* 🔑 Registration stores user credentials in role-specific JSON files.
* 🧭 Login checks credentials from corresponding role files.
* 🔁 Navigation is routed to the correct dashboard:

  * **Admin** → Admin Dashboard
  * **Employee** → Employee Role Assignment Panel
  * **Customer** → Booking & Search Panel

---

## 🚀 Planned Enhancements

* 📋 Admin view of all customer bookings per flight
* 🗑️ Flight deletion by Admin
* 📤 Export bookings and flights to CSV or PDF
* 🧭 Employee dashboard to view schedule and assigned shifts
* 🌐 Optional SQLite or Firebase integration for persistent cloud storage

---

## 📄 License

This project is intended for **educational purposes only**.
Feel free to explore, expand, and reuse with proper attribution.

---

## 👨‍💻 Author

**Ali Huzaifa**
Created as part of a Python Mini Projects series to demonstrate multi-role GUI app development using Tkinter.
