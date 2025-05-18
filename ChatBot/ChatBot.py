import streamlit as st

st.title("Simple Rule-Based ChatBot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="user_input")

def get_bot_response(user_message):
    user = user_message.lower()
    if "hello" in user:
        return "Hi there!"
    elif "how are you" in user:
        return "I'm a bot, I don't have feelings, but thanks!"
    elif "bye" in user:
        return "Goodbye!"
    else:
        return "I don't understand that."

if user_input:
    bot_reply = get_bot_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_reply))

    if "bye" in user_input.lower():
        st.warning("Chat ended. Refresh to start again.")

# Display chat history
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
