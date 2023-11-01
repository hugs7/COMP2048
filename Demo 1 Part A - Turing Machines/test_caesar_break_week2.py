# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr" 

#frequency of each letter
letter_counts = Counter(message)
#print(letter_counts)

#find max letter
maxFreq = -1
maxLetter = None
for letter, freq in letter_counts.items(): 
    print(letter, ":", freq)
    if freq > maxFreq and letter != " ":
        maxLetter = letter
        maxFreq = freq

print("Max Occurring Letter:", maxLetter, maxFreq)

#predict shift
#assume max letter is 'e'
letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
shift = (letters.index(maxLetter) - letters.index("e")) #COMPUTE SHIFT HERE
print("Predicted Shift:", shift)

#create the Caesar cypher
offset = shift #choose your shift
totalLetters = 26
keys = {} #use dictionary for letter mapping
invkeys = {} #use dictionary for inverse letter mapping, you could use inverse search from original dict
for index, letter in enumerate(letters):
    # cypher setup
    if index < totalLetters: #lowercase
        keys[letter] = letters[(index + offset) % totalLetters]
        invkeys[letter] = letters[(index - offset) % totalLetters]
    else: #uppercase
        keys[letter] = letters[(index + offset) % totalLetters + totalLetters]
        invkeys[letter] = letters[(index - offset) % totalLetters + totalLetters]
print("Cypher Dict:", keys)
print("Cypher Dict inv:", invkeys)

#decrypt
decryptedMessage = []
for letter in message:
    if letter == ' ': #spaces
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])
print("Decrypted Message:", ''.join(decryptedMessage)) #join is used to put list inot string
