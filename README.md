# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
guess the number and then with different attempt in different difficulty game and then each attempt will give you hint whether need to go higher or lower, and if you win you will see you win with some balloon show up and earn some score. You will lose if end of attempt.
- [ ] Detail which bugs you found.
1. the comparison of the number vs true number is not correct. seems that the number actually is higher than ture. it let me go higher which is not make sense
2. new game button not work
3. when you unclick the hint there is nothings to show when you guess a number, nothhing correct nothing incorrect. you only know when you end of attempt. 
4. when guess is even like 4, and then it will transform the true number to string "23", which will have a 4>"23", and let us go higher. this is wrong
- [ ] Explain what fixes you applied.
fix all of its logic with the help of AI

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 43
2. Game returns Go LOWER!
3. User enters a guess of 30 → "Go LOWER!"
4. Score updates correctly after each guess
5. Game ends after the end of the attempt

**Screenshot** *(optional)*:

## 🧪 Test Results

```
platform darwin -- Python 3.13.1, pytest-9.0.3, pluggy-1.6.0 -- /Users/lihanxia/Documents/GitHub/ai110-module1show-gameglitchinvestigator-starter/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/lihanxia/Documents/GitHub/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 10 items                                                                                                                                              

tests/test_game_logic.py::test_winning_guess PASSED                                                                                                       [ 10%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                                                                      [ 20%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                                                                       [ 30%]
tests/test_game_logic.py::test_high_guess_should_say_go_lower PASSED                                                                                      [ 40%]
tests/test_game_logic.py::test_low_guess_should_say_go_higher PASSED                                                                                      [ 50%]
tests/test_game_logic.py::test_hint_direction_multiple_scenarios PASSED                                                                                   [ 60%]
tests/test_game_logic.py::test_single_digit_vs_double_digit_secret PASSED                                                                                 [ 70%]
tests/test_game_logic.py::test_winning_score_is_positive PASSED                                                                                           [ 80%]
tests/test_game_logic.py::test_win_bonus_decreases_with_attempts PASSED                                                                                   [ 90%]
tests/test_game_logic.py::test_wrong_guesses_dont_decrease_score PASSED                                                                                   [100%]

```

## 🚀 Stretch Features: Enhanced UI

### UI Enhancements Overview
The game now includes a rich, user-friendly interface with visual feedback, progress tracking, and a comprehensive game summary. All enhancements were made in `app.py` without modifying core game logic in `logic_utils.py`.

### 1. Visual Progress Bar
**Location:** `app.py` lines 47-51

**What it does:**
- Displays a visual progress bar showing attempts used vs. total attempts allowed
- Updates dynamically as the player makes guesses
- Example output: `[▓▓▓░░░░░] Attempts: 3/8`

**Code:**
```python
attempts_used = st.session_state.attempts - 1
attempts_remaining = attempt_limit - attempts_used
progress_value = attempts_used / attempt_limit
st.progress(progress_value, text=f"Attempts: {attempts_used}/{attempt_limit}")
```

### 2. Color-Coded Status Messages
**Location:** `app.py` lines 54-59

**What it does:**
- Changes message color and urgency based on remaining attempts
- Green info box (🎯): More than 4 attempts left
- Yellow warning box (⚠️): 2-4 attempts remaining
- Red error box (🚨): Less than 2 attempts - URGENT!

**Output examples:**
- `🎯 Guess a number between 1 and 100. You have 8 attempts left!`
- `⚠️ Only 3 attempts remaining!`
- `🚨 URGENT: Only 1 attempts left!`

### 3. Hot/Cold Temperature System
**Location:** `app.py` lines 6-26 (function) and 133-150 (usage)

**What it does:**
- New `get_hot_cold_indicator()` function calculates proximity to secret number
- Returns emoji and temperature description based on distance percentage
- Provides additional feedback beyond just "higher" or "lower"

**Temperature Scale:**
| Distance | Emoji | Description |
|----------|-------|-------------|
| Within 5% of range | 🔥 | BURNING HOT! |
| Within 10% | 🌡️ | Very Hot |
| Within 20% | ♨️ | Hot |
| Within 30% | 🟡 | Warm |
| Within 50% | 🔵 | Cool |
| More than 50% | ❄️ | Ice Cold |

**Code:**
```python
def get_hot_cold_indicator(guess: int, secret: int, range_size: int) -> tuple[str, str]:
    distance = abs(guess - secret)
    percentage = distance / range_size
    # Returns emoji and temperature description
```

**Output example:**
```
📉 Go LOWER!
🔥 Temperature: BURNING HOT!
```

### 4. Enhanced Feedback Messages
**Location:** `app.py` lines 151-164

**What it does:**
- Displays larger, more prominent feedback with markdown headers
- Shows both directional hints (if enabled) and temperature simultaneously
- Uses color-coded Streamlit containers (error for wrong, success for correct)

**Output format:**
- Wrong guess with hints: Shows "📉 Go LOWER!" or "📈 Go HIGHER!" in red error box, plus temperature in blue info box
- Wrong guess without hints: Shows "❌ Wrong guess!" in yellow warning box, plus temperature
- Correct guess: Shows "🎉 Correct!" with balloons animation

### 5. Game Summary Table & Metrics Dashboard
**Location:** `app.py` lines 69-70 (state initialization), 143-149 (data collection), 189-209 (display)

**What it does:**
- Tracks detailed history of every guess in `st.session_state.history_details`
- Displays comprehensive game statistics after first guess
- Shows three key metrics: Total Guesses, Current Score, Game Status
- Presents sortable, filterable data table with all guess information

**Metrics Dashboard Output:**
```
📊 Game Summary
┌─────────────────┬──────────────────┬────────────────────┐
│ Total Guesses   │  Current Score   │      Status        │
│       5         │       60         │  🏆 Won!          │
└─────────────────┴──────────────────┴────────────────────┘
```

**History Table Columns:**
- **Attempt**: Attempt number (1, 2, 3...)
- **Guess**: The number the player guessed
- **Result**: Outcome (Win, Too High, Too Low)
- **Temperature**: Hot/cold indicator with emoji
- **Hint**: The directional hint or "Hidden" if hints disabled

**Example table:**
| Attempt | Guess | Result    | Temperature      | Hint          |
|---------|-------|-----------|------------------|---------------|
| 1       | 50    | Too High  | ❄️ Ice Cold     | 📉 Go LOWER! |
| 2       | 25    | Too Low   | 🟡 Warm         | 📈 Go HIGHER!|
| 3       | 35    | Too High  | 🌡️ Very Hot    | 📉 Go LOWER! |
| 4       | 32    | Win       | 🔥 BURNING HOT! | 🎉 Correct!  |

**Code:**
```python
# Data collection on each guess
st.session_state.history_details.append({
    "Attempt": st.session_state.attempts - 1,
    "Guess": guess_int,
    "Result": outcome,
    "Temperature": f"{emoji} {temp}",
    "Hint": message if show_hint else "Hidden"
})

# Display with metrics and table
st.dataframe(st.session_state.history_details, use_container_width=True, hide_index=True)
```

### 6. Improved Win/Loss Messages
**Location:** `app.py` lines 172-186

**What it does:**
- Enhanced win message with emoji: `🎉 You won!`
- Enhanced loss message with emoji: `💀 Out of attempts!`
- Triggers celebratory balloons animation on win
- Displays final secret number and score

**Output examples:**
- Win: `🎉 You won! The secret was 42. Final score: 90`
- Loss: `💀 Out of attempts! The secret was 73. Score: 0`

### Technical Implementation Notes
- All UI enhancements are isolated in `app.py`
- Core game logic remains untouched in `logic_utils.py`
- Uses Streamlit's built-in components: `st.progress()`, `st.metric()`, `st.dataframe()`, `st.balloons()`
- Session state management ensures data persists across Streamlit reruns
- Temperature calculation is purely UI feedback and doesn't affect game mechanics
- All tests continue to pass - no breaking changes to game logic
