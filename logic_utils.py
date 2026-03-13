"""Utility functions containing the core game logic for Glitchy Guesser."""


#Fix: Adjusted the number ranges for each difficulty level to be more distinct and challenging, with Easy (1-20), Normal (1-100), and Hard (1-200).
def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100

#Fix: Added input validation to parse_guess to handle empty input, non-numeric input, negative numbers, and decimals, providing user-friendly error messages for each case.
def parse_guess(raw: str):
    if raw == "":
        return False, None, "Enter a guess."

    if "." in raw:
        return False, None, "Please enter a whole number, not a decimal."

    try:
        value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    if value < 0:
        return False, None, "Please enter a positive number."

    return True, value, None

#Fix:Swapped hint messages — "Too High" now says "Go LOWER!" and "Too Low" says "Go HIGHER!".
# Removed broken string fallback — check_guess now always compares ints directly.
# Removed type-switching — secret is no longer converted to a string on even attempts, eliminating the root cause of bug #2.
def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"

#Fix: "Too High" now always deducts 5 — removed the even/odd logic that was rewarding wrong guesses with +5.
# Score floored at 0 — max(0, ...) prevents the score from going negative for both wrong guess types.
def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return max(0, current_score - 5)

    if outcome == "Too Low":
        return max(0, current_score - 5)

    return current_score
