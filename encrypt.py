from constants import ALPHABET

def encrypt(text: str, key: str) -> str:
    """Apply a monoalphabetic substitution: ALPHABET[i] -> key[i].

    Characters outside ALPHABET pass through unchanged.
    """
    encrypted_text = ''
    for char in text:
        upper_char = char.upper()
        if upper_char in ALPHABET:
            index = ALPHABET.index(upper_char)
            replace = key[index]
            encrypted_text += replace
        else:
            encrypted_text += char
    return encrypted_text