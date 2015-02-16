import string

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    dict = {}
    
    for i in range(26):
        dict[string.ascii_lowercase[i]] = string.ascii_lowercase[(i + shift) % 26]
        dict[string.ascii_uppercase[i]] = string.ascii_uppercase[(i + shift) % 26]
    return dict
    
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    codedtext = ''
    newchar = ''
    for c in text:
        if c in string.ascii_lowercase + string.ascii_uppercase:
            newchar = coder[c]
        else:
            newchar = c
        codedtext += newchar
    
    return codedtext
    
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
    
print applyShift("Hello, world!", 3)