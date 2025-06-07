import streamlit as st
import random
import string

def generate_password(length):
    if length < 1:
        return ""
    
    chars = string.ascii_letters + string.digits + string.punctuation
    # First character must be a letter
    first_char = random.choice(string.ascii_letters)
    # Remaining characters can be from all chars
    remaining_chars = ''.join(random.choice(chars) for _ in range(length - 1))
    return first_char + remaining_chars

# Streamlit UI
st.set_page_config(page_title="Password Generator", layout="centered")
st.title("🔐 Random Password Generator")

# Password length between 6 and 15
length = st.slider("Select Password Length", min_value=6, max_value=15, value=12)

if st.button("Generate Password"):
    password = generate_password(length)
    st.success("Generated Password:")
    st.code(password, language='text')
