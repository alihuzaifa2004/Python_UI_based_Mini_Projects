import streamlit as st
import random

# Page title and alignment
st.markdown("<h1 style='text-align: center;'>✊🖐✌️ Rock Paper Scissors Game</h1>", unsafe_allow_html=True)
st.markdown("---")

# Initialize scores in session state
if "cpu_score" not in st.session_state:
    st.session_state.cpu_score = 0
if "player_score" not in st.session_state:
    st.session_state.player_score = 0

# Create columns for buttons
st.markdown("### Choose your move:")
col1, col2, col3 = st.columns(3)
player_choice = None

with col1:
    if st.button("✊ Rock"):
        player_choice = "Rock"
with col2:
    if st.button("🖐 Paper"):
        player_choice = "Paper"
with col3:
    if st.button("✌️ Scissors"):
        player_choice = "Scissors"

# Game logic
if player_choice:
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    st.markdown("---")
    st.markdown(f"<p style='text-align: center;'>🧠 Computer chose: <strong>{computer_choice}</strong></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>🧍 You chose: <strong>{player_choice}</strong></p>", unsafe_allow_html=True)

    if player_choice == computer_choice:
        st.info("It's a Tie!")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        st.success("You win this round!")
        st.session_state.player_score += 1
    else:
        st.error("Computer wins this round!")
        st.session_state.cpu_score += 1

# Scoreboard
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>📊 Scoreboard</h3>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>CPU Score: {st.session_state.cpu_score}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>Player Score: {st.session_state.player_score}</p>", unsafe_allow_html=True)

# Reset button centered
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("🔄 Reset Game"):
    st.session_state.cpu_score = 0
    st.session_state.player_score = 0
    st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

