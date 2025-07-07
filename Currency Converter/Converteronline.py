import tkinter as tk
from tkinter import ttk, messagebox
from forex_python.converter import CurrencyRates

# Initialize CurrencyRates
cr = CurrencyRates()

# Main Window
window = tk.Tk()
window.title("Currency Converter(Online)")
window.geometry("400x400")
window.resizable(False, False)

# Function to perform conversion
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from.get()
        to_currency = combo_to.get()
        result = cr.convert(from_currency, to_currency, amount)
        label_result.config(text=f"{amount} {from_currency} = {round(result, 2)} {to_currency}")
    except Exception as e:
        messagebox.showerror("Error", "Invalid input or connection issue.")

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

combo_from = ttk.Combobox(window, values=["USD", "EUR", "GBP", "PKR", "JPY", "INR"], font=("Arial", 12))
combo_from.current(0)
combo_from.pack(pady=5)

# To Currency Dropdown
label_to = tk.Label(window, text="To Currency:", font=("Arial", 12))
label_to.pack()

combo_to = ttk.Combobox(window, values=["USD", "EUR", "GBP", "PKR", "JPY", "INR"], font=("Arial", 12))
combo_to.current(1)
combo_to.pack(pady=5)

# Convert Button
btn_convert = tk.Button(window, text="Convert", font=("Arial", 12, "bold"), bg="blue", fg="white", command=convert_currency)
btn_convert.pack(pady=15)

# Result Label
label_result = tk.Label(window, text="", font=("Arial", 14, "bold"))
label_result.pack()

window.mainloop()
