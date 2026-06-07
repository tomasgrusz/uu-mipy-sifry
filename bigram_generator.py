import numpy as np
import pandas as pd
import re
from collections import defaultdict

# Build bigram frequency tables from the training text.
with open('./data/krakatit.txt', 'r', encoding='utf-8') as file:
    text = file.read().replace(' ', '_').upper()

# Keep only the symbols used by the cipher alphabet.
text = re.sub(r'[^A-Z_]', '', text)
unique_chars = sorted(set(text))
char_to_index = {char: idx for idx, char in enumerate(unique_chars)}

size = len(unique_chars)
abs_matrix = np.zeros((size, size), dtype=int)
for i in range(len(text) - 1):
    # Count every adjacent character pair as a bigram.
    first_char = text[i]
    second_char = text[i + 1]
    if first_char in char_to_index and second_char in char_to_index:
        abs_matrix[char_to_index[first_char], char_to_index[second_char]] += 1

# Add smoothing only to unseen bigrams so every cell has a nonzero probability.
abs_matrix[abs_matrix == 0] = 1
total_bigrams = abs_matrix.sum()
rel_matrix = abs_matrix / total_bigrams

# Save both raw counts and normalized probabilities for later use.
df_abs = pd.DataFrame(abs_matrix, index=unique_chars, columns=unique_chars)
df_rel = pd.DataFrame(rel_matrix, index=unique_chars, columns=unique_chars)

df_abs.to_csv('./data/bigram-absolute.csv', encoding='utf-8-sig')
df_rel.to_csv('./data/bigram-relative.csv', encoding='utf-8-sig')

print("Bigram frequency matrices have been generated and saved as 'bigram-absolute.csv' and 'bigram-relative.csv'.")
