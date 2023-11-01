# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr" 

# Frequency of each letter
letter_counts = Counter(message)
# print(letter_counts)          # Check letter_counts of message has worked properly

# Find max letter
# Set the current maximum frequency to -1 and set the current letter to Null/None
maxFreq = -1
maxLetter = None
# Loop over each distinct letter in the message and where the frequency is greater than the maximum frequency, update
# the maxFreq variable
for letter, freq in letter_counts.items(): 
    print(letter, ":", freq)
    if freq > maxFreq and letter != " ":
        maxLetter = letter
        maxFreq = freq

# We're left with the maximum occurring letter maxLetter which appears maxFreq times
print("\nThe maximum occurring letter is", maxLetter, "which occurs", maxFreq, "times.")

# Predict the fixed shift using the assumption that the most frequent letter is 'e'.
letters = string.ascii_letters  # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
shift = (letters.index(maxLetter) - letters.index("e"))     # COMPUTE SHIFT HERE
print("Predicted Shift:", shift)

# --- The below is copied from test_caesar.py ---

# Create the Caesar cypher
offset = shift              #choose your shift
totalLetters = 26
keys = {}               # Create dictionary to be used for letter mapping
invkeys = {}            # Create dictionary to be used for the inverted letter mapping

# Encrypt
for index, letter in enumerate(letters):
    # cypher setup
    if index < totalLetters:        # lowercase
        keys[letter] = letters[(index + offset) % totalLetters]
        invkeys[letter] = letters[(index - offset) % totalLetters]
    else:                           # uppercase
        keys[letter] = letters[(index + offset) % totalLetters + totalLetters]
        invkeys[letter] = letters[(index - offset) % totalLetters + totalLetters]

print("Cypher Dict:", keys)
print("\nCypher Dict inv:", invkeys)

# Decrypt
decryptedMessage = []
for letter in message:
    if letter == ' ':   # Skip spaces as these do not get shifted
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])

print("\nDecrypted Message:", ''.join(decryptedMessage))      # join is used to put list into string
print()
