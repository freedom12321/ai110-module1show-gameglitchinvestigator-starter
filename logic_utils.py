def get_range_for_difficulty(difficulty: str):
    """
    Return (low, high) inclusive range for a given difficulty.

    Args:
        difficulty: str - One of "Easy", "Normal", or "Hard"

    Returns:
        tuple: (low: int, high: int) - The inclusive range for guessing
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Args:
        raw: str - The raw user input string

    Returns:
        tuple: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"

    Args:
        guess: int - The player's guess
        secret: int - The secret number to guess

    Returns:
        tuple: (outcome: str, message: str)
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update score based on outcome and attempt number.

    Args:
        current_score: int - The current score
        outcome: str - The outcome ("Win", "Too High", "Too Low")
        attempt_number: int - The current attempt number

    Returns:
        int: The updated score
    """
    if outcome == "Win":
        # Award points based on how quickly they won
        # Attempt 1: 100 points, Attempt 2: 90 points, etc.
        points = 110 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    # Wrong guesses don't change the score
    # (The original logic caused negative scores)
    return current_score
