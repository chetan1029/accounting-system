import math

def elo_rating_cal(choice_win, choice_loss, choice_win_rating, choice_loss_rating, result, k=32):
    """
    Calculates the new ratings for two items using the Elo rating system.
    
    Args:
        choice_win: First item.
        choice_loss: Second item.
        choice_win_rating: The current rating of the first item.
        choice_loss_rating: The current rating of the second item.
        result: The result of the comparison between the two items.
               1 if the first item won, 0 if it was a draw, and -1 if the second item won.
        k: The k-factor to use in the Elo rating system.
           The default value of 32 is generally used for matches between players of similar skill.
    
    Returns:
        A tuple containing the new ratings for the two items.
    """
    expected_score1 = 1 / (1 + math.pow(10, (choice_loss_rating - choice_win_rating) / 400))
    expected_score2 = 1 / (1 + math.pow(10, (choice_win_rating - choice_loss_rating) / 400))
    
    if result == choice_win:
        score1 = 1
        score2 = 0
    elif result == choice_loss:
        score1 = 0
        score2 = 1
    else:
        raise ValueError("Invalid result value. Must be 1, 0, or -1.")
    
    new_rating1 = choice_win_rating + k * (score1 - expected_score1)
    new_choice_loss_rating = choice_loss_rating + k * (score2 - expected_score2)

    ratings = {}
    ratings["new_choice_win_rating"] = choice_win_rating
    ratings["new_choice_loss_rating"] = new_choice_loss_rating
    
    return ratings