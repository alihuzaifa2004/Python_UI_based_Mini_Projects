
# 📚 ChatBot with OpenAI using Streamlit

This is a simple chatbot UI built with [Streamlit](https://streamlit.io) that integrates OpenAI's `gpt-3.5-turbo` model to respond to user inputs in a conversational format.

---

## 🚀 Features

- Chat interface in your browser
- Streamlit-powered UI
- Chat history tracking during the session
- Graceful exit with `"bye"` command
- Handles OpenAI errors gracefully

---

## 📦 Requirements

Make sure you have the following Python packages installed:

```bash
pip install openai streamlit
```

---

## 🔑 Setup

1. **Get your OpenAI API key** from: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

2. **Set your API key** in the code:

```python
openai.api_key = "your-api-key-here"
```

> 🔒 For better security, use environment variables instead of hardcoding.

---

## 🧠 How It Works

- Takes user input via a Streamlit text input.
- Sends the input to OpenAI's `gpt-3.5-turbo` model.
- Displays the AI response in a chat-like format.
- Maintains session history.

---

## ▶️ How to Run

Save the code in a file, e.g., `chatbot_app.py`, then run:

```bash
streamlit run chatbot_app.py
```

Then open the link in your browser (usually `http://localhost:8501`).

---

## 📸 Sample Screenshot

![ChatBot with OpenAI](preview.png) <!-- Optional: include a screenshot if needed -->

---

## 📌 Notes

- If you see an error like `insufficient_quota`, check your [OpenAI usage](https://platform.openai.com/account/usage).
- Ensure your OpenAI key is active and within quota limits.
- "bye" will end the chat politely, but the Streamlit app stays running.

---

## 📄 License

This project is for educational/demo purposes. Modify freely!
