def uniqify(unchkd):
    """
    Converts a string, presented as a list, to a list with one of each of its characters,
    while preserving its original order. Essentially ensures the key has no double-ups,
    thereby lessening the chance of patterns appearing in the encoded message.

    :param unchkd:
    :return:
    """
    chkd = []
    for char in list(unchkd):
        if char not in chkd:
            chkd.append(char)
    return chkd

def checkargs(t, k):
    """
    Checks the arguments (in this case, the args of the encode and decode functions of
    this cypher program) to see if they are of type string.
    Returns 0 if they are and a non-zero value if either are not string objects.
    """
    if not isinstance(t, str):
        print("Message argument needs to be a string object.")
    
    if not isinstance(k, str):
        print("Key argument needs to be a string object.")

    if not isinstance(k, str) or not isinstance(t, str):
        return -1
    else:
        return 0