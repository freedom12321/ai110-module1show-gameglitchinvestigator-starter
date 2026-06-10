import random
import streamlit as st
from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def get_hot_cold_indicator(guess: int, secret: int, range_size: int) -> tuple[str, str]:
    """
    Get a hot/cold indicator based on how close the guess is to the secret.

    Returns: (emoji, description)
    """
    distance = abs(guess - secret)
    percentage = distance / range_size

    if percentage <= 0.05:  # Within 5% of range
        return "🔥", "BURNING HOT!"
    elif percentage <= 0.10:  # Within 10%
        return "🌡️", "Very Hot"
    elif percentage <= 0.20:  # Within 20%
        return "♨️", "Hot"
    elif percentage <= 0.30:  # Within 30%
        return "🟡", "Warm"
    elif percentage <= 0.50:  # Within 50%
        return "🔵", "Cool"
    else:  # More than 50% away
        return "❄️", "Ice Cold"


st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "history_details" not in st.session_state:
    st.session_state.history_details = []

st.subheader("Make a guess")

# Visual progress bar for attempts
attempts_used = st.session_state.attempts - 1
attempts_remaining = attempt_limit - attempts_used
progress_value = attempts_used / attempt_limit
st.progress(progress_value, text=f"Attempts: {attempts_used}/{attempt_limit}")

# Color-coded info based on attempts remaining
if attempts_remaining > 4:
    st.info(f"🎯 Guess a number between {low} and {high}. You have {attempts_remaining} attempts left!")
elif attempts_remaining > 2:
    st.warning(f"⚠️ Guess a number between {low} and {high}. Only {attempts_remaining} attempts remaining!")
else:
    st.error(f"🚨 URGENT: Only {attempts_remaining} attempts left! Guess between {low} and {high}!")

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    st.session_state.attempts = 1
    st.session_state.secret = random.randint(low, high)
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.history_details = []
    st.session_state.score = 0
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)

        outcome, message = check_guess(guess_int, st.session_state.secret)

        # Get hot/cold indicator
        range_size = high - low
        emoji, temp = get_hot_cold_indicator(guess_int, st.session_state.secret, range_size)

        # Store detailed history for table
        st.session_state.history_details.append({
            "Attempt": st.session_state.attempts - 1,
            "Guess": guess_int,
            "Result": outcome,
            "Temperature": f"{emoji} {temp}",
            "Hint": message if show_hint else "Hidden"
        })

        if outcome == "Too High":
            if show_hint:
                st.error(f"### 📉 {message}")
                st.info(f"{emoji} Temperature: **{temp}**")
            else:
                st.warning(f"❌ Wrong guess!")
                st.info(f"{emoji} Temperature: **{temp}**")
        elif outcome == "Too Low":
            if show_hint:
                st.error(f"### 📈 {message}")
                st.info(f"{emoji} Temperature: **{temp}**")
            else:
                st.warning(f"❌ Wrong guess!")
                st.info(f"{emoji} Temperature: **{temp}**")

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"🎉 You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"💀 Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

# Display game summary table if there's any history
if len(st.session_state.history_details) > 0:
    st.divider()
    st.subheader("📊 Game Summary")

    # Create metrics row
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Guesses", len(st.session_state.history_details))
    with col2:
        st.metric("Current Score", st.session_state.score)
    with col3:
        status_emoji = "🏆" if st.session_state.status == "won" else "🎮" if st.session_state.status == "playing" else "💔"
        status_text = "Won!" if st.session_state.status == "won" else "Playing" if st.session_state.status == "playing" else "Lost"
        st.metric("Status", f"{status_emoji} {status_text}")

    # Display history table
    st.dataframe(
        st.session_state.history_details,
        use_container_width=True,
        hide_index=True
    )

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
