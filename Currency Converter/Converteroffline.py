import tkinter as tk
from tkinter import ttk, messagebox

# Static Exchange Rates (Base: USD)
exchange_rates = {
    'USD': {'USD': 1, 'EUR': 0.85, 'GBP': 0.75, 'PKR': 278.5, 'JPY': 110.0, 'INR': 83.3},
    'EUR': {'USD': 1.18, 'EUR': 1, 'GBP': 0.88, 'PKR': 327.6, 'JPY': 129.5, 'INR': 98.0},
    'GBP': {'USD': 1.33, 'EUR': 1.14, 'GBP': 1, 'PKR': 370.2, 'JPY': 147.5, 'INR': 111.5},
    'PKR': {'USD': 0.0036, 'EUR': 0.0031, 'GBP': 0.0027, 'PKR': 1, 'JPY': 0.40, 'INR': 0.30},
    'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0068, 'PKR': 2.50, 'JPY': 1, 'INR': 0.75},
    'INR': {'USD': 0.012, 'EUR': 0.010, 'GBP': 0.009, 'PKR': 3.33, 'JPY': 1.33, 'INR': 1}
}

# Main Window
window = tk.Tk()
window.title("Currency Converter (Offline)")
window.geometry("400x400")
window.resizable(False, False)

# Function to perform conversion
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from.get()
        to_currency = combo_to.get()
        rate = exchange_rates[from_currency][to_currency]
        result = amount * rate
        label_result.config(text=f"{amount} {from_currency} = {round(result, 2)} {to_currency}")
    except Exception as e:
        messagebox.showerror("Error", "Please enter a valid amount.")

# Heading
label_heading = tk.Label(window, text="Currency Converter", font=("Arial", 18, "bold"))
label_heading.pack(pady=10)

# Amount Entry
label_amount = tk.Label(window, text="Enter Amount:", font=("Arial", 12))
label_amount.pack()

entry_amount = tk.Entry(window, font=("Arial", 12))
entry_amount.pack(pady=5)

# From Currency Dropdown
label_from = tk.Label(window, text="From Currency:", font=("Arial", 12))
label_from.pack()

combo_from = ttk.Combobox(window, values=list(exchange_rates.keys()), font=("Arial", 12))
combo_from.current(0)
combo_from.pack(pady=5)

# To Currency Dropdown
label_to = tk.Label(window, text="To Currency:", font=("Arial", 12))
label_to.pack()

combo_to = ttk.Combobox(window, values=list(exchange_rates.keys()), font=("Arial", 12))
combo_to.current(1)
combo_to.pack(pady=5)

# Convert Button
btn_convert = tk.Button(window, text="Convert", font=("Arial", 12, "bold"), bg="blue", fg="white", command=convert_currency)
btn_convert.pack(pady=15)

# Result Label
label_result = tk.Label(window, text="", font=("Arial", 14, "bold"))
label_result.pack()

window.mainloop()
