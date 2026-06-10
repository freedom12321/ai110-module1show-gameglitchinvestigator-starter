from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# Bug-specific tests: Tests that the high/low hint directions are correct
def test_high_guess_should_say_go_lower():
    """
    BUG FIX TEST: When guess is TOO HIGH, the hint should tell user to go LOWER.

    This test catches the bug where the hints were reversed:
    - Old (buggy): guess > secret returned "Go HIGHER!"
    - Fixed: guess > secret returns "Go LOWER!"
    """
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High", "Outcome should be 'Too High' when guess > secret"
    assert "LOWER" in message, f"Message should contain 'LOWER' when guess is too high, got: {message}"
    assert "HIGHER" not in message, f"Message should NOT contain 'HIGHER' when guess is too high, got: {message}"


def test_low_guess_should_say_go_higher():
    """
    BUG FIX TEST: When guess is TOO LOW, the hint should tell user to go HIGHER.

    This test catches the bug where the hints were reversed:
    - Old (buggy): guess < secret returned "Go LOWER!"
    - Fixed: guess < secret returns "Go HIGHER!"
    """
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low", "Outcome should be 'Too Low' when guess < secret"
    assert "HIGHER" in message, f"Message should contain 'HIGHER' when guess is too low, got: {message}"
    assert "LOWER" not in message, f"Message should NOT contain 'LOWER' when guess is too low, got: {message}"


def test_hint_direction_multiple_scenarios():
    """
    BUG FIX TEST: Comprehensive test for hint directions across multiple scenarios.

    Tests various guess/secret combinations to ensure hints always point
    in the correct direction.
    """
    # Secret is 50
    secret = 50

    # Test multiple high guesses
    for high_guess in [51, 60, 75, 99, 100]:
        outcome, message = check_guess(high_guess, secret)
        assert outcome == "Too High", f"Guess {high_guess} should be 'Too High' for secret {secret}"
        assert "LOWER" in message, f"High guess {high_guess} should suggest going LOWER, got: {message}"

    # Test multiple low guesses
    for low_guess in [1, 10, 25, 40, 49]:
        outcome, message = check_guess(low_guess, secret)
        assert outcome == "Too Low", f"Guess {low_guess} should be 'Too Low' for secret {secret}"
        assert "HIGHER" in message, f"Low guess {low_guess} should suggest going HIGHER, got: {message}"


def test_single_digit_vs_double_digit_secret():
    """
    BUG FIX TEST: Tests that single-digit guesses work correctly with double-digit secrets.

    This catches the bug where string/int comparison was causing issues:
    - Secret: 32 (int)
    - Guess: 4 (int) should be "Too Low"
    - Old bug: On even attempts, secret became "32" (string), causing wrong comparison
    """
    secret = 32

    # Single digit guesses should all be "Too Low"
    outcome, message = check_guess(4, secret)
    assert outcome == "Too Low", f"Guess 4 should be 'Too Low' when secret is {secret}"
    assert "HIGHER" in message, f"Should suggest going HIGHER, got: {message}"

    outcome, message = check_guess(3, secret)
    assert outcome == "Too Low", f"Guess 3 should be 'Too Low' when secret is {secret}"
    assert "HIGHER" in message, f"Should suggest going HIGHER, got: {message}"

    # Double digit guesses higher than secret
    outcome, message = check_guess(50, secret)
    assert outcome == "Too High", f"Guess 50 should be 'Too High' when secret is {secret}"
    assert "LOWER" in message, f"Should suggest going LOWER, got: {message}"


# Scoring logic tests
def test_winning_score_is_positive():
    """
    BUG FIX TEST: Winning should always give positive score, never negative.

    This catches the bug where wrong guesses decreased score, causing
    negative final scores even when winning.
    """
    # Start with 0 score, win on first attempt
    score = update_score(0, "Win", 1)
    assert score > 0, f"Winning on attempt 1 should give positive score, got: {score}"

    # Even if you had a negative score somehow, winning should make it positive
    score = update_score(-20, "Win", 5)
    assert score > 0, f"Winning should result in positive score even from negative, got: {score}"


def test_win_bonus_decreases_with_attempts():
    """
    Test that winning quickly gives more points than winning slowly.
    """
    score1 = update_score(0, "Win", 1)
    score2 = update_score(0, "Win", 2)
    score5 = update_score(0, "Win", 5)

    assert score1 > score2, f"Winning on attempt 1 ({score1}) should be more than attempt 2 ({score2})"
    assert score2 > score5, f"Winning on attempt 2 ({score2}) should be more than attempt 5 ({score5})"


def test_wrong_guesses_dont_decrease_score():
    """
    BUG FIX TEST: Wrong guesses should not decrease score.

    Old buggy behavior: "Too Low" always subtracted 5, causing negative scores.
    """
    initial_score = 0

    # Wrong guesses should not change score
    score_after_high = update_score(initial_score, "Too High", 3)
    score_after_low = update_score(initial_score, "Too Low", 4)

    assert score_after_high == initial_score, f"'Too High' should not change score, got: {score_after_high}"
    assert score_after_low == initial_score, f"'Too Low' should not change score, got: {score_after_low}"
