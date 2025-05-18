# 📁 Python Mini Projects with GUI

This repository is created to deliver a collection of Python mini projects with GUI interfaces. The included projects are:

- Student Management System  
- Contact Book  
- Rock Paper Scissor  
- Virtual Bank System  
- ChatBot with OpenAI  
- MCQ Quiz App

---

## 📘 Student Management System

This is a Python mini project that provides a GUI-based student management system. It allows users to manage student records using a simple and intuitive interface.

### ✅ Features
- Add new student records  
- View all student records  
- Update existing student information  
- Delete student records  
- Data stored in `data.json` file for persistence  

### 🛠️ Technologies Used
- Python  
- Streamlit (for GUI)  
- JSON (for data storage)  

---

## 📒 Contact Book

The Contact Book project provides a GUI for storing and managing contact information. Users can add, view, search, and delete contact details easily.

### ✅ Features
- Add new contacts (name, phone number, email)  
- View all saved contacts  
- Search contacts by name or number  
- Delete specific contacts  

### 🛠️ Technologies Used
- Python  
- Streamlit (for GUI)  
- File handling (e.g., text or JSON format for saving contacts)  

---

## ✊ Rock Paper Scissor

A classic Rock Paper Scissor game with a GUI that lets users play against the computer.

### ✅ Features
- Interactive GUI gameplay  
- Random computer move generation  
- Real-time result display  

### 🛠️ Technologies Used
- Python  
- Streamlit (for GUI)  
- Random module  

---

## 🏦 Virtual Bank System

This project is a basic banking system simulation that allows users to create accounts, log in, deposit, withdraw, and delete accounts through a Streamlit-powered interface.

### ✅ Features
- Create new bank accounts  
- Secure login with password (stored in JSON)  
- View current account balance  
- Deposit and withdraw funds  
- Delete existing accounts  
- Data stored in `accounts.json` for persistence  

### 🛠️ Technologies Used
- Python  
- Streamlit (for GUI)  
- JSON (for storing account data)  

---

## 🤖 ChatBot with OpenAI

This project demonstrates a simple chatbot using the OpenAI GPT-3.5 model integrated with Streamlit.

### ✅ Features
- Interactive chat interface with memory of conversation  
- Uses OpenAI’s GPT-3.5 for generating responses  
- Text-based input/output in the browser  

### 🛠️ Technologies Used
- Python  
- Streamlit (for GUI)  
- OpenAI API (GPT-3.5 Turbo)  

### 📄 How to Use
1. Set your OpenAI API key in the script (`openai.api_key = "your-api-key"`).  
2. Run the Streamlit app:  
   ```bash
   streamlit run ChatBotwithOpenAI.py
   ```
3. Interact with the chatbot using the provided input field.

---

## 🧠 MCQ Quiz App

A simple yet interactive multiple-choice quiz application built using **Python** and **Streamlit**. This app presents users with a series of 20 general knowledge questions and evaluates their score at the end.

### ✅ Features
- 20 general knowledge questions  
- Multiple choice options for each question  
- Real-time scoring and result display  
- Option to restart the quiz  
- Fully browser-based UI using Streamlit  

### 🛠️ Technologies Used
- Python  
- Streamlit (for GUI)  

### 🧪 How It Works
1. Each question is displayed with multiple options.  
2. Users select one option and click **Next** to proceed.  
3. After answering all questions, click **Show Result** to view your score and correct answers.  
4. Option to **Restart Quiz** to try again.  

### 📂 Project Structure
```
MCQ_Quiz_App/
│
├── mcq_quiz_app.py         # Main Streamlit application file
└── README.md               # Project documentation (this file)
```

### ▶️ How to Run
1. Install Streamlit (if not already installed):
```bash
pip install streamlit
```

2. Run the app:
```bash
streamlit run mcq_quiz_app.py
```

3. The app will open in your default web browser.

### 📌 Example Questions
- What is the capital of France?  
- What is 2 + 2?  
- Who wrote *Romeo and Juliet*?  
- What is the tallest mountain in the world?  

---

## 📂 Project Structure

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
```

---

## 📜 License

This project is for **educational purposes** only.
