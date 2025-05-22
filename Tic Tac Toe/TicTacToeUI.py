import streamlit as st

# Function to check if a player has won
def check_winner(board, player):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    return any(all(board[i] == player for i in line) for line in wins)

# Function to display the board (for reference, optional)
def display_board(board):
    st.write(
        f"{board[0]} | {board[1]} | {board[2]}\n"
        f"---------\n"
        f"{board[3]} | {board[4]} | {board[5]}\n"
        f"---------\n"
        f"{board[6]} | {board[7]} | {board[8]}"
    )

# Initialize the session state
if "turn" not in st.session_state:
    st.session_state.turn = 0
    st.session_state.board = [" " for _ in range(9)]
    st.session_state.player = "X"
    st.session_state.game_over = False
    st.session_state.player_X_name = ""
    st.session_state.player_O_name = ""
    st.session_state.winner = None

# Title
st.title("Tic-Tac-Toe Game")

# Player name input
if st.session_state.player_X_name == "" and st.session_state.player_O_name == "":
    st.session_state.player_X_name = st.text_input("Enter name for Player X:", "")
    st.session_state.player_O_name = st.text_input("Enter name for Player O:", "")

    if st.session_state.player_X_name != "" and st.session_state.player_O_name != "":
        st.session_state.player = "X"
        st.session_state.turn = 0
        st.session_state.board = [" " for _ in range(9)]
        st.session_state.game_over = False
        st.session_state.winner = None

# Display current player
if not st.session_state.game_over:
    st.subheader(f"Current Player: {st.session_state.player}")

# Function to handle move
def make_move(index):
    if st.session_state.board[index] == " " and not st.session_state.game_over:
        st.session_state.board[index] = st.session_state.player
        st.session_state.turn += 1

        if check_winner(st.session_state.board, st.session_state.player):
            st.session_state.game_over = True
            if st.session_state.player == "X":
                st.session_state.winner = st.session_state.player_X_name
            else:
                st.session_state.winner = st.session_state.player_O_name
        elif st.session_state.turn == 9:
            st.session_state.game_over = True
            st.session_state.winner = "Tie"
        else:
            st.session_state.player = "O" if st.session_state.player == "X" else "X"

# Display the 3x3 button grid
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        idx = row * 3 + col
        if cols[col].button(st.session_state.board[idx], key=f"button_{idx}"):
            make_move(idx)

# Game result display
if st.session_state.game_over:
    if st.session_state.winner == "Tie":
        st.success("It's a tie!")
    else:
        st.success(f"Congratulations, {st.session_state.winner} wins!")

    # Restart game button
    if st.button("Restart Game"):
        st.session_state.turn = 0
        st.session_state.board = [" " for _ in range(9)]
        st.session_state.player = "X"
        st.session_state.game_over = False
        st.session_state.player_X_name = ""
        st.session_state.player_O_name = ""
        st.session_state.winner = None
