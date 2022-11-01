def parse(data):
    """Write a simple parser that will parse and run Deadfish.

        Deadfish has 4 commands, each 1 character long:

        i increments the value (initially 0)
        d decrements the value
        s squares the value
        o outputs the value into the return array
        Invalid characters should be ignored.

        parse("iiisdoso")  ==>  [8, 64]"""
    value = 0
    list = []
    for command in data:
        if command == 'i':
            value += 1
        elif command == 'd':
            value -= 1
        elif command == 's':
            value *= value
        elif command == 'o':
            list.append(value)
    return list