from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_update_score_win_early():
    # Winning on attempt 1 should give maximum points
    result = update_score(0, "Win", 1)
    assert result == 80

def test_update_score_win_late():
    # Winning on a late attempt should give minimum 10 points
    result = update_score(0, "Win", 20)
    assert result == 10

def test_update_score_too_high():
    # Guessing too high deducts 5 points
    result = update_score(50, "Too High", 1)
    assert result == 45

def test_update_score_too_low():
    # Guessing too low deducts 5 points
    result = update_score(50, "Too Low", 1)
    assert result == 45

def test_update_score_floor_at_zero():
    # Score should not go below 0
    result = update_score(3, "Too High", 1)
    assert result == 0

def test_update_score_unknown_outcome():
    # Unknown outcome should leave score unchanged
    result = update_score(50, "Unknown", 1)
    assert result == 50
