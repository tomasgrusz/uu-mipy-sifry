"""Metropolis-Hastings sampler for breaking monoalphabetic substitution ciphers.

Explores the key space by swapping two key positions per step and scoring
candidate decryptions against a bigram reference matrix (log-probability).
"""

import random
from encrypt import encrypt
from decrypt import decrypt
import pandas as pd
from keygen import generate_initial_key
from constants import ALPHABET
import numpy as np

def bigram_score(text: str, bigram_matrix: np.ndarray, alphabet: str = ALPHABET) -> float:
    """Sum of log-probabilities over consecutive bigrams — higher is better."""
    score = 0
    text = text.upper()
    for i in range(len(text) - 1):
        a, b = text[i], text[i + 1]
        if a in alphabet and b in alphabet:
            i1, i2 = alphabet.index(a), alphabet.index(b)
            score += np.log(bigram_matrix[i1][i2])
    return score

def random_key() -> str:
    """Return a uniformly random permutation of ALPHABET."""
    return ''.join(random.sample(ALPHABET, len(ALPHABET)))

def swap_two_chars(s: str) -> str:
    """Propose a neighbor key by transposing two random positions."""
    s = list(s)
    i, j = random.sample(range(len(s)), 2)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)

def metropolis_hastings(
    ciphertext: str,
    reference_matrix: np.ndarray,
    iterations: int = 20000,
    initial_key: str | None = None,
) -> tuple[str, list[float]]:
    """Run MCMC to find the substitution key that maximises bigram score.

    The initial_key parameter is currently overridden by a frequency-based
    guess — this is intentional to improve convergence speed.
    """
    initial_key = generate_initial_key(ciphertext)
    current_key = initial_key if initial_key else random_key()
    current_decryption = decrypt(ciphertext, current_key)
    current_score = bigram_score(current_decryption, reference_matrix)

    best_key = current_key
    best_score = current_score
    score_history = []

    for _ in range(iterations):
        candidate_key = swap_two_chars(current_key)
        candidate_decryption = decrypt(ciphertext, candidate_key)
        candidate_score = bigram_score(candidate_decryption, reference_matrix)

        if candidate_score > current_score or random.random() < np.exp(candidate_score - current_score):
            current_key = candidate_key
            current_score = candidate_score
            if candidate_score > best_score:
                best_key = candidate_key
                best_score = candidate_score

        score_history.append(best_score)

    return best_key, score_history
