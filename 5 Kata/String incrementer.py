def increment_string(strng):
    """Your job is to write a function which increments a string, to create a new string.

        If the string already ends with a number, the number should be incremented by 1.
        If the string does not end with a number. the number 1 should be appended to the new string.
        Examples:

        foo -> foo1

        foobar23 -> foobar24

        foo0042 -> foo0043

        foo9 -> foo10

        foo099 -> foo100

        Attention: If the number has leading zeros the amount of digits should be considered."""
    first_number_index = 0
    if strng:
        if strng[-1].isnumeric():
            for count, value in reversed(list(enumerate(strng))):
                if not value.isnumeric():
                    first_number_index = count +1
                    break
            left, right = strng[:first_number_index], strng[first_number_index:]
            number_length = len(right)
            return left + str(int(right)+1).zfill(number_length)
        else:
            return strng + '1'
    else:
        return '1'
