import string
import sys
import vigtools

def decodev(t, k):
    """
    Runs a decode script to decode messages that are encoded with
    Vigeneres Cypher.
    Takes an encoded message and the known key as str arguments.
    
    """
    # Safety check if the arguments are of type string:
    if vigtools.checkargs(t, k) != 0:
        return
    
    # Retrieve the message to decode as a string of lower case chars:
    msg = str(t.lower())
    # Convert key to a lost of unique sub-keys:
    key = vigtools.uniqify(k.lower())