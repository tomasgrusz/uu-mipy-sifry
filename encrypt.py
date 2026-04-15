from constants import ALPHABET

def encrypt(text, key):
    # Substitute each supported character using the provided permutation key.
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