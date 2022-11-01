def friend(x):
    """Make a program that filters a list of strings and returns a list with only your friends name in it.

        If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

        Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

        i.e.

        friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
        Note: keep the original order of the names in the output."""
    l = []
    for f in x:
        if f:
            print(f)
            last_letter = f[-1]
            pos = f.rfind(last_letter)
            if pos == 3:
                l.append(f)
    return l