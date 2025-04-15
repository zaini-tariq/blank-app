import streamlit as st

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.game_over = False

def check_winner(board):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in wins:
        a, b, c = combo
        if board[a] == board[b] == board[c] != "":
            return board[a]
    return None

def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.game_over = False

st.title("Tic-Tac-Toe (Streamlit Version)")

cols = st.columns(3)

for i in range(3):
    for j in range(3):
        idx = i * 3 + j
        with cols[j]:
            if st.button(st.session_state.board[idx] or " ", key=idx, use_container_width=True):
                if not st.session_state.board[idx] and not st.session_state.game_over:
                    st.session_state.board[idx] = st.session_state.current_player
                    winner = check_winner(st.session_state.board)
                    if winner:
                        st.success(f"Player {winner} wins!")
                        st.session_state.game_over = True
                    elif "" not in st.session_state.board:
                        st.info("It's a draw!")
                        st.session_state.game_over = True
                    else:
                        st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

st.markdown("### Current Player: " + st.session_state.current_player)

if st.button("Reset Game"):
    reset_game()
