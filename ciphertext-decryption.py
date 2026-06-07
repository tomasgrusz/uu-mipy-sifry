"""Batch-decrypts all ciphertext files in ./test/ciphertext/ via Metropolis-Hastings.

Expects filenames matching text_N_sample_M_ciphertext.txt; writes
corresponding plaintext and recovered key to ./test/plaintext/ and ./test/keys/.
"""

import pandas as pd
from decrypt import decrypt
import metropolis
import os
import re

input_dir = "./test/ciphertext"
pattern = re.compile(r"^(text_\d+_sample_\d+)_ciphertext\.txt$")

# Iterate through all files in the input directory
for filename in os.listdir(input_dir):
    match = pattern.match(filename)

    if not match:
        continue

    base_name = match.group(1)
    input_path = os.path.join(input_dir, filename)

    # Read the encrypted text from the file
    with open(input_path, "r", encoding="utf-8") as f:
        encrypted_text = f.read()
    reference_matrix = pd.read_csv('data/bigram-relative.csv', index_col=0).values
    reference_matrix += 1e-10

    # Perform Metropolis-Hastings decryption
    best_key, score_history = metropolis.metropolis_hastings(
        ciphertext=encrypted_text,
        reference_matrix=reference_matrix,
        iterations=20000
    )

    # Decrypt the ciphertext using the best key found
    result = decrypt(encrypted_text, best_key)

    # Save the decrypted plaintext and the key to separate files
    with open(os.path.join("./test/plaintext", f"{base_name}_plaintext.txt"), "w", encoding="utf-8") as f_text:
            f_text.write(result)

    with open(os.path.join("./test/keys", f"{base_name}_key.txt"), "w", encoding="utf-8") as f_key:
            f_key.write(best_key)

    print(f"Loaded file: {filename}")