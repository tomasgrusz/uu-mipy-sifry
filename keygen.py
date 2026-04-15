import collections
from constants import ALPHABET
from constants import CZECH_FREQ_ORDER

def get_frequency_order(text):
    # Rank ciphertext symbols by how often they appear.
    text = text.upper()
    counts = collections.Counter(c for c in text if c in ALPHABET)
    sorted_chars = [item[0] for item in counts.most_common()]
    return ''.join(sorted_chars)

def generate_initial_key(ciphertext):
    # Start from a frequency-based guess for the substitution mapping.
    freq_order = get_frequency_order(ciphertext)
    key_map = {}

    for i, c in enumerate(freq_order):
        if i < len(CZECH_FREQ_ORDER):
            key_map[c] = CZECH_FREQ_ORDER[i]

    # Fill in any missing symbols so the result is a full permutation key.
    used = set(key_map.values())
    remaining = [c for c in ALPHABET if c not in used]
    unused_cipher = [c for c in ALPHABET if c not in key_map]

    for c, r in zip(unused_cipher, remaining):
        key_map[c] = r

    final_key = ''.join(key_map.get(c, c) for c in ALPHABET)
    return final_key