
# ✊🖐✌️ Rock Paper Scissors Game (Streamlit)

A simple interactive Rock-Paper-Scissors game built using [Streamlit](https://streamlit.io/) in Python. This project allows a user to play against the computer, view real-time score updates, and reset the game state.

---

## 🚀 Features

- User interface with three buttons: Rock, Paper, and Scissors.
- Random move generation for the computer opponent.
- Scoreboard displaying current scores of the user and the computer.
- Score memory during session using Streamlit's `session_state`.
- Option to reset the game.

---

## 🧠 Game Logic

- Rock beats Scissors.
- Scissors beats Paper.
- Paper beats Rock.
- If both the player and the computer choose the same move, it's a tie.

---

## 🧩 How It Works

1. **UI Creation:**
   - A centered title is displayed at the top.
   - Buttons for Rock, Paper, and Scissors are aligned in columns.
   - Upon pressing a button, the player's choice is recorded.

2. **Random CPU Move:**
   - The computer randomly selects a move from the same three choices.

3. **Decision Making:**
   - Player’s move is compared to the computer’s move.
   - Based on standard RPS rules, a winner is declared or it's a tie.
   - Scores are updated using `st.session_state`.

4. **Scoreboard:**
   - Displays current scores of both player and computer.
   - Remains updated through user interaction.

5. **Reset Button:**
   - A centered button that resets scores and restarts the game state.

---

## 🔧 Requirements

- Python 3.x
- Streamlit

Install dependencies using:

```bash
pip install streamlit
```

---

## ▶️ Run the App

To launch the Streamlit app, navigate to the script directory and run:

```bash
streamlit run your_script_name.py
```

---

## 📁 Project Structure

```
rock-paper-scissors/
│
├── rps_game.py          # Main Streamlit app
└── README.md            # Project documentation
```

---

## ✍️ Author

Developed as a basic fun project for learning Streamlit and implementing session states and interactive UI in Python.

---

## 📜 License

This project is open-source and free to use under the [MIT License](https://opensource.org/licenses/MIT).
