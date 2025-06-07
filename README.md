
# 📁 Python Mini Projects with GUI

This repository is created to deliver a collection of Python mini projects with GUI interfaces. The included projects are:

- Student Management System  
- Contact Book  
- Rock Paper Scissor  
- Virtual Bank System  
- ChatBot with OpenAI  
- MCQ Quiz App  
- Tic-Tac-Toe Game  
- Plagiarism Detection System  
- Password Generator 🔐  
- Real-Time Stopwatch  ⏱️

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

---

## 🎮 Tic-Tac-Toe Game

An interactive browser-based Tic-Tac-Toe game for two players using Streamlit.

### ✅ Features
- Two-player mode with name input  
- Alternating turns and move tracking  
- Automatic win or tie detection  
- Option to restart the game  

### 🛠️ Technologies Used
- Python  
- Streamlit (for GUI)  

### ▶️ How to Run
```bash
pip install streamlit
streamlit run app.py
```

---

## 🕵️ Plagiarism Detection System

A tool to detect plagiarism between two text documents or inputs using either TF-IDF or Sentence Transformers for similarity calculation.

### ✅ Features
- Upload PDF, DOCX, or TXT files or input text manually  
- Choose between TF-IDF or Transformer-based similarity  
- Highlights line-by-line similarities  
- Gives similarity score with interpretation (high/moderate/low)  

### 🛠️ Technologies Used
- Python  
- Streamlit (for GUI)  
- scikit-learn (TF-IDF, cosine similarity)  
- SentenceTransformers (for BERT-based embeddings)  
- PyMuPDF and python-docx (for PDF and DOCX parsing)  

---

## 🔐 Password Generator

A secure and customizable password generator with a simple GUI interface. Users can generate passwords that always start with a letter and include a mix of letters, digits, and special characters.

### ✅ Features
- User-defined password length (between 6 and 15 characters)
- Passwords always start with a letter (A–Z, a–z)
- Includes letters, digits, and punctuation characters
- Simple and secure password generation
- Web-based interface using Streamlit

### 🛠️ Technologies Used
- Python  
- Streamlit (for GUI)  
- `random` and `string` modules for password generation  

### ▶️ How to Run
```bash
pip install streamlit
streamlit run password_generator.py
```

---

## ⏱️ Real-Time Stopwatch

This is a simple **Real-Time Stopwatch** web application built using Streamlit in Python.

### ✅ Features
- Start/Stop the stopwatch  
- Reset the stopwatch  
- Real-time updates of minutes, seconds, and milliseconds  
- Minimal, centered layout  

### 🛠️ Technologies Used
- Python  
- Streamlit (for GUI)  

### ▶️ How to Run
```bash
pip install streamlit
streamlit run stopwatch.py
```

### Limitations
⚠️ Since Streamlit is not designed for continuous loops, this app relies on simple hacks using session state and `st.empty()`. It is best for small utilities but not a high-precision stopwatch.

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
├── Password Generator/
│   └── app.py
```

---

## 📜 License

This project is for **educational purposes** only.
