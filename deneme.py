import string

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    alphabet = {}
    shifted = {}
    for i, item in zip(range(26), string.ascii_uppercase):
        alphabet[i] = item

    for i, letter in zip(alphabet, string.ascii_uppercase):
        shifted[letter] = alphabet[(i+shift) % 26]
    temp  = shifted.keys()
    for key in temp:
        shifted[key.lower()] = shifted[key].lower()
    return shifted

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    result = ''
    for letter in text:
        if letter in coder:
            result += coder[letter]
        else:
            result += letter
    return result

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))

