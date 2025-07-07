
# Currency Converter (Python Tkinter)

## 📋 Project Overview
This is a **Currency Converter Application** built using **Python Tkinter**. It allows users to convert currencies from one type to another using both:
- ✅ **Online Mode:** Real-time exchange rates using the `forex-python` library.
- ✅ **Offline Mode:** Instant conversion using pre-defined static exchange rates.

---

## ✨ Features
- User-friendly GUI with Tkinter.
- Currency selection via dropdown menus.
- Real-time conversion (online mode).
- Instant response without internet (offline mode).
- Error handling for invalid inputs.

---

## 🔌 Project Scenarios

### 1. 🌐 Online Currency Converter
- Uses the `forex-python` library.
- Fetches **live exchange rates** from external APIs.
- Requires an **active internet connection**.

#### Pros:
- Real-time rates.
- Wide currency support.

#### Cons:
- Depends on API speed.
- May hang if API is slow.

---

### 2. 🚀 Offline Currency Converter
- Uses **pre-defined exchange rates** stored in the program.
- Works **without internet**.
- Provides **instant results**.

#### Pros:
- Fast and reliable.
- Fully offline.

#### Cons:
- Exchange rates need manual updating.

---

## 🛠️ Installation

### Requirements:
```bash
pip install forex-python
```

### Files:
- `currency_converter_online.py` — For online conversion.
- `currency_converter_offline.py` — For offline conversion.

---

## ▶️ How to Run

### Online Mode:
```bash
python currency_converter_online.py
```

### Offline Mode:
```bash
python currency_converter_offline.py
```

---

## 📌 Notes:
- You can extend the offline exchange rate table with more currencies.
- In online mode, the system fetches live rates but may take a few seconds depending on internet speed.

---

## 💡 Future Enhancements
- Add more currencies.
- Improve UI with themes or dark mode.
- Integrate local database or Excel support for offline rates.
- Add historical exchange rate graphs.

---

## 🤝 Developed By
Ali Huzaifa
