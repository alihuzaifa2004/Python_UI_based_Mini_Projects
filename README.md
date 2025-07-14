# 📁 Python Mini Projects with GUI

This repository is created to deliver a collection of Python mini projects with GUI interfaces. The included projects are:

* Student Management System
* Contact Book
* Rock Paper Scissor
* Virtual Bank System
* ChatBot with OpenAI
* MCQ Quiz App
* Tic-Tac-Toe Game
* Plagiarism Detection System
* Password Generator 🔐
* Real-Time Stopwatch ⏱️
* Basic Data Analysis with Streamlit 📊
* E-Commerce Management System 🛒
* Scientific Calculator 🧮
* Currency Converter 🌍
* Weather App 🌐
* Word Counter Application 📝
---

## 📘 Student Management System

This is a Python mini project that provides a GUI-based student management system. It allows users to manage student records using a simple and intuitive interface.

### ✅ Features

* Add new student records
* View all student records
* Update existing student information
* Delete student records
* Data stored in `data.json` file for persistence

### 🛠️ Technologies Used

* Python
* Streamlit (for GUI)
* JSON (for data storage)

---

## 📒 Contact Book

The Contact Book project provides a GUI for storing and managing contact information. Users can add, view, search, and delete contact details easily.

### ✅ Features

* Add new contacts (name, phone number, email)
* View all saved contacts
* Search contacts by name or number
* Delete specific contacts

### 🛠️ Technologies Used

* Python
* Streamlit (for GUI)
* File handling (e.g., text or JSON format for saving contacts)

---

## ✊ Rock Paper Scissor

A classic Rock Paper Scissor game with a GUI that lets users play against the computer.

### ✅ Features

* Interactive GUI gameplay
* Random computer move generation
* Real-time result display

### 🛠️ Technologies Used

* Python
* Streamlit (for GUI)
* Random module

---

## 🏦 Virtual Bank System

This project is a basic banking system simulation that allows users to create accounts, log in, deposit, withdraw, and delete accounts through a Streamlit-powered interface.

### ✅ Features

* Create new bank accounts
* Secure login with password (stored in JSON)
* View current account balance
* Deposit and withdraw funds
* Delete existing accounts
* Data stored in `accounts.json` for persistence

### 🛠️ Technologies Used

* Python
* Streamlit (for GUI)
* JSON (for storing account data)

---

## 🤖 ChatBot with OpenAI

This project demonstrates a simple chatbot using the OpenAI GPT-3.5 model integrated with Streamlit.

### ✅ Features

* Interactive chat interface with memory of conversation
* Uses OpenAI’s GPT-3.5 for generating responses
* Text-based input/output in the browser

### 🛠️ Technologies Used

* Python
* Streamlit (for GUI)
* OpenAI API (GPT-3.5 Turbo)

### 📄 How to Use

1. Set your OpenAI API key in the script (`openai.api_key = "your-api-key"`).
2. Run the Streamlit app:

   ```bash
   streamlit run ChatBotwithOpenAI.py
   ```

---

## 🧠 MCQ Quiz App

A simple yet interactive multiple-choice quiz application built using **Python** and **Streamlit**. This app presents users with a series of 20 general knowledge questions and evaluates their score at the end.

### ✅ Features

* 20 general knowledge questions
* Multiple choice options for each question
* Real-time scoring and result display
* Option to restart the quiz
* Fully browser-based UI using Streamlit

### 🛠️ Technologies Used

* Python
* Streamlit (for GUI)

---

## 🎮 Tic-Tac-Toe Game

An interactive browser-based Tic-Tac-Toe game for two players using Streamlit.

### ✅ Features

* Two-player mode with name input
* Alternating turns and move tracking
* Automatic win or tie detection
* Option to restart the game

### 🛠️ Technologies Used

* Python
* Streamlit (for GUI)

### ▶️ How to Run

```bash
pip install streamlit
streamlit run app.py
```

---

## 🕵️ Plagiarism Detection System

A tool to detect plagiarism between two text documents or inputs using either TF-IDF or Sentence Transformers for similarity calculation.

### ✅ Features

* Upload PDF, DOCX, or TXT files or input text manually
* Choose between TF-IDF or Transformer-based similarity
* Highlights line-by-line similarities
* Gives similarity score with interpretation (high/moderate/low)

### 🛠️ Technologies Used

* Python
* Streamlit (for GUI)
* scikit-learn (TF-IDF, cosine similarity)
* SentenceTransformers (for BERT-based embeddings)
* PyMuPDF and python-docx (for PDF and DOCX parsing)

---

## 🔐 Password Generator

A secure and customizable password generator with a simple GUI interface. Users can generate passwords that always start with a letter and include a mix of letters, digits, and special characters.

### ✅ Features

* User-defined password length (between 6 and 15 characters)
* Passwords always start with a letter (A–Z, a–z)
* Includes letters, digits, and punctuation characters
* Simple and secure password generation
* Web-based interface using Streamlit

### 🛠️ Technologies Used

* Python
* Streamlit (for GUI)
* `random` and `string` modules for password generation

### ▶️ How to Run

```bash
pip install streamlit
streamlit run password_generator.py
```

---

## ⏱️ Real-Time Stopwatch

This is a simple **Real-Time Stopwatch** web application built using Streamlit in Python.

### ✅ Features

* Start/Stop the stopwatch
* Reset the stopwatch
* Real-time updates of minutes, seconds, and milliseconds
* Minimal, centered layout

### 🛠️ Technologies Used

* Python
* Streamlit (for GUI)

### ▶️ How to Run

```bash
pip install streamlit
streamlit run stopwatch.py
```

### Limitations

⚠️ Since Streamlit is not designed for continuous loops, this app relies on simple hacks using session state and `st.empty()`. It is best for small utilities but not a high-precision stopwatch.

---

## 📊 Basic Data Analysis with Streamlit

This is a simple Streamlit web application that allows users to upload a CSV file and instantly view an overview of the data, including the first few rows and summary statistics.

### ✅ Features

* Upload a CSV file (`.csv` format)
* Display the first five rows of the dataset
* Show basic descriptive statistics using `pandas.describe()`

### 🛠️ Technologies Used

* Python
* Streamlit (for GUI)
* Pandas (for data analysis)

### ▶️ How to Run

```bash
pip install streamlit pandas
streamlit run app.py
```

### 📂 File Structure

```
Basic Data Analysis with Streamlit/
├── app.py
├── README.md
└── requirements.txt  # Optional: for specifying dependencies
```

### 📝 Example

When you upload a CSV file, you'll see:

* The first five rows of the dataset
* Summary statistics such as count, mean, std, min, and max

### 🧩 Notes

* The CSV is read with `encoding='ISO-8859-1'` to handle non-UTF-8 files.
* You can adjust the encoding as needed (e.g., `utf-8`, `latin1`).

---
Here's your **updated project README** with the new **🛒 E-Commerce Management System** section added and fully integrated into the existing project list and structure:

---
## 🛒 E-Commerce Management System

This is a **Streamlit-based desktop web app** that simulates an **E-Commerce Management System** backed by a **SQL Server database**. The app enables customers to view and purchase products and provides admin-level access for managing product inventory and customer records.

### ✅ Features

#### 👥 Customers

* Add new customers
* View all registered customers
* View individual customer order history

#### 🛒 Products

* Browse all available products with images
* Buy products (place orders)
* Admins can add new products with images

#### 📦 Orders

* Place new orders
* View all orders
* View specific customer's order history via stored procedure

#### 🔐 Admin

* Login system for admin access
* Admin-only features (like product addition)

### 🛠️ Technologies Used

* Python
* Streamlit (for GUI)
* SQL Server (database)
* pyodbc (for DB connection)
* Pandas (data manipulation)
* OS module (file handling)

### ▶️ Running the App

1. **Install dependencies:**

   ```bash
   pip install streamlit pyodbc pandas
   ```

2. **Run the app:**

   ```bash
   streamlit run app.py
   ```

> Make sure your SQL Server is running and accessible.

### 🔑 Default Admin Login

* **Username:** `admin`
* **Password:** `admin123`

### 📁 Folder Structure

```
E-Commerce Management System/
├── app.py
├── product_images/
├── README.md
```


## 🧮 Scientific Calculator (Tkinter)

This is a GUI-based Scientific Calculator built using Python's Tkinter library. It supports both basic arithmetic and advanced scientific functions with a responsive, scrollable layout.

### ✅ Features

* Standard operations: `+`, `-`, `*`, `/`, `()`
* Scientific functions:
  * Trigonometry: `sin`, `cos`, `tan`
  * Logarithmic: `log`, `ln`
  * Exponential and powers: `exp`, `pow`
  * Square root: `sqrt`
* Constants: `π`, `e`
* Control buttons:
  * `C` to clear all input
  * `⌫` to delete a single character
  * `=` to evaluate the expression
* Scrollable interface for small screens

### 🛠️ Technologies Used

* Python 3.x
* Tkinter (for GUI)
* Math module (for scientific calculations)

### ▶️ How to Run

```bash
python scientific_calculator.py
```

> No external libraries are required. This project runs with Python’s built-in modules.
---

Here’s your **updated README file with the Currency Converter project fully integrated** into the original document:

---

## 💱 Currency Converter (Python Tkinter)

This is a **Currency Converter Application** built using **Python Tkinter**. It allows users to convert currencies from one type to another using both:

* ✅ **Online Mode:** Real-time exchange rates using the `forex-python` library.
* ✅ **Offline Mode:** Instant conversion using pre-defined static exchange rates.

### ✅ Features

* User-friendly GUI with Tkinter.
* Currency selection via dropdown menus.
* Real-time conversion (online mode).
* Instant response without internet (offline mode).
* Error handling for invalid inputs.

---

### 🔌 Project Scenarios

#### 🌐 Online Currency Converter

* Uses the `forex-python` library.
* Fetches **live exchange rates** from external APIs.
* Requires an **active internet connection**.

**Pros:**

* Real-time rates.
* Wide currency support.

**Cons:**

* Depends on API speed.
* May hang if API is slow.

---

#### 🚀 Offline Currency Converter

* Uses **pre-defined exchange rates** stored in the program.
* Works **without internet**.
* Provides **instant results**.

**Pros:**

* Fast and reliable.
* Fully offline.

**Cons:**

* Exchange rates need manual updating.

---

### 🛠️ Installation

**Requirements:**

```bash
pip install forex-python
```


### 📁 Folder Structure

```
Currency Converter/
├── online.py
├── offline.py
├── README.md
```

---

### ▶️ How to Run

**Online Mode:**

```bash
python currency_converter_online.py
```

**Offline Mode:**

```bash
python currency_converter_offline.py
```

---

### 📌 Notes

* You can extend the offline exchange rate table with more currencies.
* In online mode, the system fetches live rates but may take a few seconds depending on internet speed.

---

### 💡 Future Enhancements

* Add more currencies.
* Improve UI with themes or dark mode.
* Integrate local database or Excel support for offline rates.
* Add historical exchange rate graphs.


# Weather App using Python Tkinter and WeatherAPI

## 📋 Project Overview
This is a **Weather Application** built using **Python Tkinter** that fetches **live weather data** using the [WeatherAPI.com](https://www.weatherapi.com/) service.

The application displays:
- ✅ Current Temperature
- ✅ Weather Condition
- ✅ Humidity
- ✅ Wind Speed

---

## ✨ Features
- User-friendly GUI with Tkinter.
- Live weather updates using WeatherAPI.
- Error handling for invalid city names and connection issues.

---

## 🔌 Requirements

### Install Required Libraries:
```bash
pip install requests
```

---

## 🔑 Get Your API Key
1. Go to [https://www.weatherapi.com/](https://www.weatherapi.com/)
2. Sign up for a free account.
3. Get your API key from the dashboard.
4. Replace `'YOUR_API_KEY_HERE'` in the Python code with your API key.

---

### 📁 Folder Structure

```
Wheather App/
├── app.py
├── README.md
```


## ▶️ How to Run
```bash
python weather_app.py
```

---

## 🛠️ How It Works
- Enter a city name in the input box.
- Click "Get Weather" to fetch live weather data.
- Displays:
  - City
  - Temperature (°C)
  - Weather condition (Clear, Rainy, Cloudy, etc.)
  - Humidity
  - Wind Speed (km/h)

---

## 📌 Notes
- Make sure you have an active internet connection.
- The API key must be active and correct for the app to work.

---

## 💡 Future Enhancements
- Add weather icons.
- Add popular cities dropdown.
- Convert to EXE file for easy distribution.
- Show multi-day forecasts.


# 📝 Word Counter Application

This project contains two versions of a **Word Counter App** built using:

- ✅ **Streamlit (Web App)**
- ✅ **Tkinter (Desktop App)**

Both versions allow users to:
- Paste text manually
- Upload `.txt` or `.pdf` files
- Analyze word count, character count, sentence count, and paragraph count

---

## 📂 Project Structure

```
word_counter_app/
│
├── word_counter_streamlit.py   # Streamlit web version
├── word_counter_tkinter.py     # Tkinter desktop version
├── README.md                   # Project documentation

```

---

## 🌐 Streamlit Version

### ✅ Features
- Paste or upload `.txt`/`.pdf` files
- Extracts and displays content
- Shows counts of:
  - Words
  - Characters
  - Sentences
  - Paragraphs
- Requires pressing **Submit** button to view results

### ▶️ How to Run

1. **Install dependencies**:

```bash
pip install streamlit PyPDF2
```

2. **Run the app**:

```bash
streamlit run word_counter_streamlit.py
```

3. **Open in browser**:
Streamlit will open your default browser automatically at `http://localhost:8501`.

---

## 🖥️ Tkinter Version

### ✅ Features
- Desktop GUI with:
  - Text area for manual input
  - Upload `.txt` or `.pdf` files
  - "Analyze Text" button to process
- Displays counts of:
  - Words
  - Characters
  - Sentences
  - Paragraphs

### ▶️ How to Run

1. **Install dependencies**:

```bash
pip install PyPDF2
```

2. **Run the app**:

```bash
python word_counter_tkinter.py
```

> Make sure you're running this in a desktop environment (not headless server).

---

## 📦 Requirements

Create a `requirements.txt` with the following:

```
streamlit
PyPDF2
```

Install using:

```bash
pip install -r requirements.txt
```

---

## 📂 Project Folder Structure

```
├── Student Management System/
│   ├── data.json
│   └── StudentPortal_GUI.py
│
├── Contact Book/
│   └── [Contact Book Python Files]
│
├── Rock Paper Scissor/
│   └── [Rock Paper Scissor Python Files]
│
├── Virtual Bank System/
│   ├── accounts.json
│   └── VirtualBank_GUI.py
│
├── ChatBot with OpenAI/
│   └── ChatBotwithOpenAI.py
│
├── MCQ Quiz App/
│   └── mcq_quiz_app.py
│
├── Tic Tac Toe Game/
│   └── app.py
│
├── Plagiarism Detection System/
│   └── plagiarism_app.py
│
├── Password Generator/
│   └── password_generator.py
│
├── Real-Time Stopwatch/
│   └── stopwatch.py
│
├── Basic Data Analysis with Streamlit/
│   ├── app.py
│   ├── README.md
│   └── requirements.txt
│
├── E-Commerce order Management System/
│   ├── app.py
│   ├── product_images/
│   └── README.md
├── Calculator/
│   ├── main.py
│   └── README.md
├── Currency Converter/
│   ├── online.py
│   ├── offline.py
│   └── README.md
├── Wheather App/
│   ├── app.py\
│   └── README.md
├── Word Counter/
│   ├── streamlit_version.py\
|   ├── tkinter_version.py\
│   └── README.md


---

## 📜 License

This project is for **educational purposes** only.
