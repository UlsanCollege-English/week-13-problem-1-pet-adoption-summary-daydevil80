def summarize_adoptions(adoptions):
    """
    Given a list of animal type strings, return a dictionary mapping each
    distinct animal type to how many times it appears in the list.

    Example:
    summarize_adoptions(["cat", "dog", "cat"]) -> {"cat": 2, "dog": 1}
    """

    counts = {}  # empty dictionary

    for animal in adoptions:          # loop through each item
        if animal not in counts:      # if we haven't seen it before
            counts[animal] = 0        # create new key with count 0
        counts[animal] += 1           # add 1 to the count

    return counts
