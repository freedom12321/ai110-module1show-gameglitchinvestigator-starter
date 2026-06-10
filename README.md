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

1. <!-- 1. User enters a guess of 43 -->
2. <!-- 2. Game returns Go LOWER! -->
3. <!-- 3. User enters a guess of 30 → "Go LOWER!" -->
4. <!-- Score updates correctly after each guess -->
5. <!-- Game ends after the end of the attempt -->

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

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

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
