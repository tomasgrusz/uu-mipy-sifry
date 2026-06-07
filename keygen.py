import collections
from constants import ALPHABET
from constants import CZECH_FREQ_ORDER

def get_frequency_order(text: str) -> str:
    """Return ALPHABET characters sorted by descending frequency in text."""
    text = text.upper()
    counts = collections.Counter(c for c in text if c in ALPHABET)
    sorted_chars = [item[0] for item in counts.most_common()]
    return ''.join(sorted_chars)

def generate_initial_key(ciphertext: str) -> str:
    """Build a starting key by aligning ciphertext frequencies to Czech frequencies.

    Symbols absent from the ciphertext are filled in arbitrarily to form
    a complete permutation — the Metropolis step will fix them.
    """
    freq_order = get_frequency_order(ciphertext)
    key_map = {}

    for i, c in enumerate(freq_order):
        if i < len(CZECH_FREQ_ORDER):
            key_map[c] = CZECH_FREQ_ORDER[i]

    used = set(key_map.values())
    remaining = [c for c in ALPHABET if c not in used]
    unused_cipher = [c for c in ALPHABET if c not in key_map]

    for c, r in zip(unused_cipher, remaining):
        key_map[c] = r

    final_key = ''.join(key_map.get(c, c) for c in ALPHABET)
    return final_key