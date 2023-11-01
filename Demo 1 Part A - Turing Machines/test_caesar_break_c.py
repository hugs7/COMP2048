# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

# message = "K jqrg vjku oguucig hkpfu aqw ygnn K ycpvgf vq vqwej dcug ykvj aqw tgictfkpi vjg rtqlgev ygtg yqtmkpi qp vqigvjgt Kxg tgxkgygf vjgncvguv xgtukqp qh vjg tgrqtv cpf K jcxg c hgy uwiiguvkqpu hqt tgxkukqpu Yqwnf kv dg rquukdng vq uejgfwng c swkem ecnn vq iq qxgt vjgo vqigvjgt"
# message = "Namuy nuayk oy gz luaxze lobk yrgyn ykbkt rgtjyhuxuamn zkxxgik Zuucutm gtj nk ngy g yvkiogr lxoktj igrrkj Pkyyoig"
message = "gyyngybuob"
print(len(message))
# Frequency of each letter
# letter_counts = Counter(message)
# print(letter_counts)          # Check letter_counts of message has worked properly
# print("\n")
# letter_counts.pop(' ') # remove spaces as these do not get shifted

letter_counts = {}
for letter in message:
    if letter.isalpha():    # Skip non-alpha chars
        if letter.lower() in letter_counts:
            letter_counts[letter.lower()] += 1
        else:
            letter_counts[letter.lower()] = 1

# Sort letter counts descending by num
sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
print("Sorted letter counts", sorted_letter_counts, "\n")

# Letters in alphabet (lowercase and UPPERCASE)
letters = string.ascii_letters  # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Predict the fixed shift using the concept that the Vowels are the most common letters appearing
# in any given sentence of English. That's a, e, i, o, u. We know these letters are a fixed offset
# away from each other, and so we can use this to align our shift.
# common_letters = ['e', 't', 'a', 'i', 'o', 'n', 's', 'h', 'r']
common_letters = list(letters[:26])
print(common_letters)
common_letters_dict = {}


# Now we can use the ten most common letters as a heuristic
shifts = []
for l in common_letters:
    slc = letters.index(sorted_letter_counts[0][0])
    l_index = letters.index(l)
    shifts.append(slc - l_index)

# print("Estimated probably shifts:", shifts)

for i, es_shift in enumerate(shifts):
    print("Predicted Shift:", es_shift, "for letter", common_letters[i])
    offset = es_shift              #choose your shift
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

    #print("Cypher Dict:", keys)
    #print("\nCypher Dict inv:", invkeys)

    # Decrypt
    decryptedMessage = []
    for letter in message:
        if letter == ' ':   # Skip spaces as these do not get shifted
            decryptedMessage.append(letter)
        else:
            decryptedMessage.append(invkeys[letter])

    print("Decrypted Message " + str(i) + ": ", ''.join(decryptedMessage))      # join is used to put list into string
    print()
