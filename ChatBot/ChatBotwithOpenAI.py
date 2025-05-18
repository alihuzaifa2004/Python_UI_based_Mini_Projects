import streamlit as st
import openai

# Set your API key
openai.api_key = ""  # Replace with your OpenAI API key

def get_chatgpt_response(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

st.title("ChatBot with OpenAI")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", key="input")

if user_input:
    st.session_state.history.append(("You", user_input))
    
    if user_input.lower() == "bye":
        st.session_state.history.append(("Bot", "Goodbye!"))
    else:
        reply = get_chatgpt_response(user_input)
        st.session_state.history.append(("Bot", reply))

for sender, message in st.session_state.history:
    st.write(f"**{sender}:** {message}")
