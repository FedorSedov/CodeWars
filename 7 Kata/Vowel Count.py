def get_count(sentence):
    """Return the number (count) of vowels in the given string.
        We will consider a, e, i, o, u as vowels for this Kata (but not y).
        The input string will only consist of lower case letters and/or spaces."""
    count = 0
    for letter in sentence:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count