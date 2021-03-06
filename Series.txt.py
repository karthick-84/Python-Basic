def slices(series, length):
    """
    Given a string of digits, output all the contiguous substrings of length `n` in
that string in the order that they appear.
 
For example, the string "49142" has the following 3-digit series:
 
- "491"
- "914"
- "142"
 
And the following 4-digit series:
 
- "4914"
- "9142"
    """
    if len(series) < length or length < 1:
        raise ValueError
    return [series[index:index + length] for index in range(len(series)) if index + length <= len(series)]
    pass