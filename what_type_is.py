def what_type_is(s: str):
    """Helper function. This function takes a string and return a number that represent it type:
    0 for int
    1 for float
    2 for string
    :param s: string that we need to check.
    :type s: str
    :return: the string type
    :return type: int
    """
    try:
        int(s)
        return 0
    except ValueError:
        try:
            float(s)
            return 1
        except ValueError:
            return 2
