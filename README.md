# uu-mipy-sifry

Utilities for experimenting with a monoalphabetic substitution cipher over the alphabet `A-Z` plus `_` (underscore as a word separator).

## Requirements

- Python 3.13 (project currently uses `.venv` with Python 3.13.2)
- Dependencies listed in `requirements.txt`

Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## File Documentation

### Python files

- `constants.py`
  - Central shared constants used across modules.
  - `ALPHABET`: `ABCDEFGHIJKLMNOPQRSTUVWXYZ_`
  - `CZECH_FREQ_ORDER`: letter order heuristic for initial key estimation.

- `encrypt.py`
  - `encrypt(text, key)`
  - Applies monoalphabetic substitution using `key` as a permutation of `ALPHABET`.
  - Non-alphabet characters are passed through unchanged.

- `decrypt.py`
  - `decrypt(text, key)`
  - Reverses the substitution done by `encrypt` by locating symbols in `key`.

- `keygen.py`
  - `get_frequency_order(text)`
    - Counts symbol frequencies and returns symbols in descending frequency order.
  - `generate_initial_key(ciphertext)`
    - Creates a frequency-based initial substitution key using `CZECH_FREQ_ORDER`.

- `bigram_generator.py`
  - Reads `data/krakatit.txt`, normalizes text to uppercase and `_`, filters unsupported characters.
  - Builds a bigram count matrix with Laplace smoothing (`+1` in each cell).
  - Outputs absolute and relative bigram matrices into CSV files.

- `metropolis-hastings.py`
  - `bigram_score(text, bigram_matrix, alphabet=ALPHABET)`
    - Scores text by summing log probabilities of adjacent bigrams.
  - `random_key()`
    - Generates a random substitution key.
  - `swap_two_chars(s)`
    - Produces a neighboring key proposal by swapping two characters.
  - `metropolis_hastings(ciphertext, reference_matrix, iterations=10000, initial_key=None)`
    - Runs stochastic search over keys to maximize bigram score.
    - Returns `(best_key, score_history)`.

### Relevant non-Python files

- `requirements.txt`
  - Python package dependencies used by data processing and scoring.

- `data/krakatit.txt`
  - Training corpus for language bigram statistics.

- `data/bigram-absolute.csv`
  - Generated absolute bigram counts.

- `data/bigram-relative.csv`
  - Generated relative bigram probabilities used for scoring.

- `test/`
  - Reference plaintext/key files and many prepared ciphertext samples.
  - Useful for manual evaluation of encryption/decryption and key search quality.
