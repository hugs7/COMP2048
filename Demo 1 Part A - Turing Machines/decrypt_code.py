# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22

Section 3 of the assignment part A
"""
import math
import string

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
#print(capitalLetters)

TOTAL_LETTERS = 26

LETTERS = "abcdefghijklmnopqrstuvwxyz"

KNOWN_GOOD = "attackpearlharbor"

encrypted = [19, 17, 17, 19, 14, 20, 23, 18, 19, 8, 12, 16, 19, 8, 3, 21, 8, 25, 18, 14, 18, 6, 3, 18, 8, 15, 18, 22,
             18, 11]

remap = {}

for i, l in enumerate(KNOWN_GOOD):
    remap[encrypted[i]] = l

print(remap)

for i, l in enumerate(encrypted):
    if l in remap.keys():
        print(remap[l], ":", l)
    else:
        print("  :", l)
print("\n-\n")
for i, l in enumerate(encrypted):
    e = int((math.log10(l)) + 1) * ' '
    if l in remap.keys():
        print(remap[l] + e, end='')
    else:
        print("_" + e, end='')
print()
for i, l in enumerate(encrypted):
    if l in remap.keys():
        print(l, end=' ')
    else:
        print(str(l) + " ", end='')
print("\n")

# attackpearlharbordecemberseven

# -----------------------------
print("---------------------\n")
KNOWN_GOOD = "attackpearlharbordecemberseven"

remap = {}

for i, l in enumerate(KNOWN_GOOD):
    remap[encrypted[i]] = l

print(remap)

for i, l in enumerate(encrypted):
    if l in remap.keys():
        print(remap[l], ":", l)
    else:
        print("  :", l)
print("\n-\n")
for i, l in enumerate(encrypted):
    e = int((math.log10(l)) + 1) * ' '
    if l in remap.keys():
        print(remap[l] + e, end='')
    else:
        print("_" + e, end='')
print()
for i, l in enumerate(encrypted):
    if l in remap.keys():
        print(l, end=' ')
    else:
        print(str(l) + " ", end='')
print("\n")

# Was going to use Python to solve the rest, but it became too cumbersome and easier to do by hand.
# See document

"""
def all_possible_mappings(num_list, char_list):
    if not num_list:
        # base case: we have mapped all numbers to characters, return the mappings
        return [{}]
    else:
        # recursive case: try mapping the first number to each character that is not already in use
        mappings = []
        for char in char_list:
            if char not in mappings:
                remaining_chars = [c for c in char_list if c != char]
                partial_mappings = all_possible_mappings(num_list[1:], remaining_chars)
                for partial_mapping in partial_mappings:
                    partial_mapping[num_list[0]] = char
                    mappings.append(partial_mapping)
        return mappings


num_list = [25, 6, 15, 22, 11]
char_list = ['d', 'f', 'g', 'i', 'j', 'l', 'm', 'n', 'q', 's', 'u', 'v', 'w', 'x', 'y', 'z']
#mappings = all_possible_mappings(num_list, char_list)


print("\nm", mappings)

print("\n\n\n")

f = open("msg.txt", "w")

for m in mappings:
    for i, l in enumerate(encrypted):
        if l in remap.keys():
            #print(remap[l], end='')
            f.write(remap[l])
        else:
            #print(m[l], end='')
            f.write(m[l])

    print()
    f.write("\n")


# attackpearlharbordecemberseven

f.close()

#Print the Decoded message
#INSERT CODE HERE
"""