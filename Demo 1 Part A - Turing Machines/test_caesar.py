# -*- coding: utf-8 -*-
"""
Caesar cypher script

Encode and decode messages by scrambling the letters in your message

Created on Fri Feb  1 23:06:50 2019

@author: shakes
"""
import string

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = "The quick brown fox jumped over the lazy dog" #type your message here
message = "Hugos house is at fourty five slash seven landsborough terrace Toowong and he has a special friend called" \
          " Jessica"
# message = "I hope this message finds you well I wanted to touch base with you regarding the project were working on together Ive reviewed the latest version of the report and I have a few suggestions for revisions Would it be possible to schedule a quick call to go over them together"
print("Message:", message)

# Create the Caesar cypher
offset = 6              #choose your shift
totalLetters = 26
keys = {}               # Create dictionary to be used for letter mapping
invkeys = {}            # Create dictionary to be used for the inverted letter mapping

for index, letter in enumerate(letters):
    # cypher setup
    if index < totalLetters:        # lowercase
        keys[letter] = letters[(index + offset) % totalLetters]
        invkeys[letter] = letters[(index - offset) % totalLetters]
    else:                           # uppercase
        keys[letter] = letters[(index + offset) % totalLetters + totalLetters]
        invkeys[letter] = letters[(index - offset) % totalLetters + totalLetters]

print("Cypher Dict:", keys)
print("Cypher Dict inv:", invkeys)

# Encrypt
encryptedMessage = []
for letter in message:
    if letter == ' ':   # Skip spaces as these do not get shifted
        encryptedMessage.append(letter)
    else:
        encryptedMessage.append(keys[letter])

print("\nEncrypted Message:", ''.join(encryptedMessage))      # join is used to put list into string

# Decrypt
decryptedMessage = []
for letter in encryptedMessage:
    if letter == ' ':   # Skip spaces as these do not get shifted
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])

print("\nDecrypted Message:", ''.join(decryptedMessage), "\n")      # join is used to put list into string
