import string


def encodev(t, k):
    """
    A Cipher function that takes a message and encodes it based on a given key.
    It will shift the alphabet of each character in the message based on the next character
    in the key eg:

    Message: hello world! | Static key: weld
    Key:     weldw eldwe
    Encoded: diwok azuhh!

    """
    text = str(t.lower())
    # Convert key to a list of unique sub-keys:
    key = uniqify(k.lower())

    # Holds the index of the current sub-key.
    key_index = 0

    # Create a dictionary of each alphabet character 0-25.
    alphabet = list(string.ascii_lowercase)

    # Append each encoded character here:
    encoded = ''

    for char in text:
        # Negative 1 always represents a non-alpha char.
        num = -1
        # Get the value of the current character based on its order in the alphabet.
        if char in string.ascii_lowercase:
            num = alphabet.index(char)

        # Get the amount of places to shift by when encoding, based on the current sub-key.
        total_shift = 0
        if char in string.ascii_lowercase:
            total_shift = num + alphabet.index(key[key_index])

        # If the shifted value is outside the alphabet range, overflow to the beginning:
        if total_shift > 25:
            total_shift -= 26

        # Add the current char if its not in the alphabet...
        if num == -1:
            encoded = encoded + char
        # ...or the encoded char if it is.
        else:
            encoded = encoded + alphabet[total_shift]

        # Increment the counter of the index of a sub-key, unless it is the last sub-key.
        if key_index == len(key)-1:
            key_index = 0
        elif num != -1:
            key_index += 1

    # Finally, return the encoded result:
    return encoded


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


def evaluate():
    """
    A debugging function to check if theres any deviation between the encodev function and
    a previously evaluated encoding. This uses a phrase that contains all letters of the
    alphabet.
    """
    text = 'The quick brown fox jumps over the lazy dog.'
    key = 'doggone'

    # From http://planetcalc.com/2468/:
    expected = 'wvk dylqq ovrkt ssa xaztv cbrv wvk yecm jbk.'

    # Run the cipher:
    result = encodev(text,key)

    # Check the result against the expected encoded message:
    alphabet = list(string.ascii_lowercase)

    index = 0

    assert expected == result

    for e in list(expected):
        if e in alphabet:
            expected_number = alphabet.index(e)
            result_number = alphabet.index(list(result)[index])
            print(str(expected_number) + ' : ' + str(result_number) + ' Difference: ' + str(expected_number - result_number))
        index += 1
