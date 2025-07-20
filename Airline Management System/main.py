import tkinter as tk
from ui.login import login_screen
from ui.register import register_screen

def main():
    root = tk.Tk()
    root.title("Airline Management System")
    root.geometry("400x300")
    root.resizable(False, False)
    root.config(padx=20, pady=20)

    tk.Label(root, text="🛫 Airline Management System", font=("Arial", 18, "bold")).pack(pady=20)

    tk.Button(root, text="Login", width=20, command=lambda: login_screen(root)).pack(pady=10)
    tk.Button(root, text="Register", width=20, command=lambda: register_screen(root)).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
