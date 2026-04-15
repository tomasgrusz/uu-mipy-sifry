from constants import ALPHABET

def decrypt(text, key):
    # Reverse the substitution by locating each ciphertext symbol in the key.
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