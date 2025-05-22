# utils/ranking.py

def rank_items(preferences):
    """
    Ranks items based on the number of wins.
    Items with more wins are ranked higher.
    Ties are broken arbitrarily (by Python's sort stability or item name).
    """
    if not preferences:
        return []

    # Convert preferences dict to a list of tuples (item, score_dict)
    # Then sort based on 'wins'
    # Example preference: {"Option A": {"wins": 2, "losses": 1}, ...}
    
    # Calculate a simple score: wins - losses can also be an option
    # For now, just using wins, as per the simplified example.
    
    sorted_items = sorted(preferences.items(), key=lambda item: item[1].get('wins', 0), reverse=True)
    
    # ranked_list = [(item_name, details['wins'], details['losses']) for item_name, details in sorted_items]
    ranked_list = [item_name for item_name, details in sorted_items]
    return ranked_list

def generate_pairs(items):
    """
    Generates all unique pairs from a list of items.
    Example: items = ['A', 'B', 'C'] -> [('A', 'B'), ('A', 'C'), ('B', 'C')]
    """
    if len(items) < 2:
        return []
    
    import itertools
    pairs = list(itertools.combinations(items, 2))
    return pairs