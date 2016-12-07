import string
import sys
import vigtools

def vigere(t, k, is_encode):
    """
    A Cypher function that takes a message and encodes it based on a given key.
    It will shift the alphabet of each character in the message based on the next character
    in the key eg:

    Message: hello world! | Static key: weld
    Key:     weldw eldwe
    Encoded: diwok azuhh!

    """
    msg = str(t.lower())
    # Convert key to a list of unique sub-keys:
    key = vigtools.uniqify(k.lower())

    # Holds the index of the current sub-key.
    key_index = 0

    # Create a dictionary of each alphabet character 0-25.
    alphabet = list(string.ascii_lowercase)

    # Append each encoded character here:
    encoded = ''

    for char in msg:
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

    # Run the cypher:
    result = vigere(text, key, True)

    # Check the result against the expected encoded message:
    alphabet = list(string.ascii_lowercase)
    # The current index  for check between the  characters of
    # the expected and resulting messages.
    index = 0
    # If this stays at zero, print that the test was successful.
    number_of_errors = 0

    # Check each letter in the expected message against its corresponding
    # letter in the result.
    for e in list(expected):
        if e in alphabet:
            # Get the value of the current characters based on its order in
            # the alphabet.
            expected_number = alphabet.index(e)
            result_number = alphabet.index(list(result)[index])

            # Calculate the difference:
            difference = expected_number - result_number

            # Print only if theres an error:
            if difference != 0:
                number_of_errors += 1
                # Print a header before any of the errors, if at least one exists.
                if number_of_errors == 1:
                    print('Errors: ')
                #... then print the difference of the characters' values.
                print('    ' + e + ' : ' + list(result)[index] + ' Difference in Position: ' + str(difference))
        # Check the next corresponding character.
        index += 1

    # Print success if there were no errors
    if number_of_errors == 0:
        print('Cypher encodes as expected.')

if __name__ == '__main__':
    if sys.argv[1] == 'encode':
        # Check if the key contains non-alpha characters:
        for c in sys.argv[3]:
            if c not in list(string.ascii_letters):
                print('Key can only contain alphabetic characters.')
                sys.exit()

        # Otherwise, run the cypher:
        coded = vigere(sys.argv[2], sys.argv[3], True)
        print(coded)
        sys.exit()
    elif sys.argv[1] == 'decode':
        # Check if the key contains non-alpha characters:
        for c in sys.argv[3]:
            if c not in list(string.ascii_letters):
                print('Key can only contain alphabetic characters.')
                sys.exit()

        # Otherwise, run the cypher:
        coded = vigere(sys.argv[2], sys.argv[3], True)
        print(coded)
        sys.exit()
    elif sys.argv[1] == 'test':
        evaluate()
        sys.exit()
