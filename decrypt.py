from constants import ALPHABET

def decrypt(text: str, key: str) -> str:
    """Reverse a monoalphabetic substitution: key[i] -> ALPHABET[i].

    Characters outside the key pass through unchanged.
    """
    decrypted_text = ''
    for char in text:
        upper_char = char.upper()
        if upper_char in key:
            index = key.index(upper_char)
            original = ALPHABET[index]
            decrypted_text += original
        else:
            decrypted_text += char
    return decrypted_text