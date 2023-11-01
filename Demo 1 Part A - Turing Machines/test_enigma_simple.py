# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import enigma
import rotor

LETTERS = "abcdefghijklmnopqrstuvwxyz"
#----

engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                       rotor.ROTOR_II, rotor.ROTOR_III, key="SSC",
                       plugs="AA BB CC DD EE")

#print(engine)

# Part a)
print("Part A")
message = "Hello World"
print("Message:", message)
secret = engine.encipher(message)
print("Encoded Message:", secret)

#Write code to decrypt message below
#HINT: Reuse the code above to do it. You do not need to write a decrypt function.
#INSERT CODE HERE
# Need to define new engine because Enigma uses a rolling code. So if we were to use the same engine as the encryption
# engine, one wouldn't be able to crack the code. That is, the starting (window) positions need to be the same at
# the start. Hence we we ened to define a new engine.q
decrypt_engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                               rotor.ROTOR_II, rotor.ROTOR_III, key="SSC",
                               plugs="AA BB CC DD EE")

decrypt_message = decrypt_engine.encipher(secret)
print("Decrypted message:", decrypt_message)

print()
#Part b)
print("Part B")
ShakesHorribleMessage = "Vxye ajgh D yf? Ptn uluo yjgco L ws nznde czidn. Bsj ccj qdbk qjph wpw ypxvu!"
print("Encryped message:", ShakesHorribleMessage)
# Write code to decrypt message above
# INSERT CODE HERE
# fixed but hidden window positions

# Demonstrate basic enigma machine decryption
decrypt_engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                               rotor.ROTOR_II, rotor.ROTOR_III, key="SSC",
                               plugs="AA BB CC DD EE")

decrypt_message_a = decrypt_engine.encipher(ShakesHorribleMessage)
print("Decrypted message:", decrypt_message_a)
print("\n")