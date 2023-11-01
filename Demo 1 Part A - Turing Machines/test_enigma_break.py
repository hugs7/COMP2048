# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
Student: Hugo Burton
Student Number: s4698512
COMP2048 A1 part II
"""

import string
import enigma
import rotor
import time

# Constants

END_PHRASE = "Hail Shakes!"      # crib - known phrase in the message


# Functions

def find_combination(encrypted_message) -> tuple[str, str, str, str]:
    """
    Function to find decrypted message.
    Returns string of the decryptred message
    :param encrypted_message: enigma encoded message (str)
    :return: str containing the decrypted phrase
    """
    # loop over combinations of window positions until we find combination where decoded message ends with END_PHRASE
    letters = string.ascii_letters      # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    upper_letters = letters[-26:]

    tries = 0

    for r1 in upper_letters:
        for r2 in upper_letters:
            for r3 in upper_letters:
                #print(r1_start+r2_start+r3_start)
                decrypt_engine_b = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I, rotor.ROTOR_II,
                                                 rotor.ROTOR_III, key=r1 + r2 + r3,
                                                 plugs="AA BB CC DD EE")
                decrypt_message = decrypt_engine_b.encipher(encrypted_message)
                end_length = len(END_PHRASE)

                if decrypt_message[-end_length:].__eq__(END_PHRASE):
                    # Found correct encryption
                    print("Tries (part d):", tries, "\n")
                    return r1, r2, r3, decrypt_message

                tries += 1


# Main

def main():
    ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"

    # Record start time
    st_time = time.time()

    # Break the code via brute force search using the find_combination function
    r1, r2, r3, decrypted_message = find_combination(ShakesHorribleMessage)

    # Record end time
    end_time = time.time()

    # Compute time delta
    elps_time = end_time - st_time

    # Print the Decoded message
    print("With rotor combination '" + r1 + " " + r2 + " " + r3 + "' the decrypted message is: '" + decrypted_message
          + "'\n")

    print("It took", round(elps_time, 4), "seconds to crack the code.")


if __name__ == "__main__":
    main()

# See Word Document for answers. Below was just my rough working

"""
Part D
Add a counter to your script to keep track of the number of tries.
How many attempts does it take to crack the code? How long did it take on your computer? How long do you think it 
would’ve taken for a computer in the 1940s?! 

11771 tries taken in the above program to crack the code. On my computer (i7-12700K @ 5GHz) it took 4.6394 seconds
to crack the code.

Let's compare that to a computer of the 1940s. Specifically, let's look at the Bombe as this was the computer Alan 
Turing used to crack the Enigma code in 1942. There were many versions of the Bombe machine over the years, but it is
noted http://www.ellsbury.com/gne/gne-000.htm (Cryptographic history of work on the German Naval Enigma) that for the
three rotor arrangement, the British Bombe could run through all the combinations in about 20 minutes. 

Using some mathematics, one can calculate how many operations per second that is. 17576 = 26 ^ 3 in 20 min = 20 * 60
= 1200 seconds. 17576 / 1200 = 14.6466667 ~= 15 Hz. This makes sense and is comparable to the computers of the time 
which had clock speeds of this level.

In the above code, only 11771 combinations needed to be checked. So 11771 / 17576 ~= 0.669720073.

0.669720073 * 1200 = 803.66 seconds = 13.39 minutes for British Bombe to crack the code. That's a 17,799% increase in 
the time taken to crack the code using a brute force method!

Speeds of computers improved drastically from the early 1940s to the mid and late 40s with clock speeds quickly 
entering the thousands.

Part E
If Shakes the Horrible wasn’t so ignorant and worried about money, he would have purchased both the extra 2 rotors 
and the plugboard. How much longer would have the cracking his code taken on your computer? An estimate as a number 
of tries or minutes/hours is sufficient. 

3 + 2 = 5 rotors
that's 5 x 4 x 3 x 2 x 1 combinations = 5! = 120 rotor combinations.

Rotor window combination = 26 ^ 5 = 11 881 376

Plugboard 
10 pairs of letters cross over. That means multiple the choices of letters together for 10 letters. Also divide
by 10! as it doesn't matter the order that the letters are chosen

((26 choose 2) * (24 choose 2) * (22 choose 2) * ... (8 choose 2)) / 10! = 150 738 274 937 250

Assuming linear time, if we multiply our time of 4.94 seconds by the ratio of new combinations over the existing 
combinations, we can get an estimate of how long it might take my computer to crack the code.

4.6394 * (120 * 11 881 376 * 150 738 274 937 250) / (6 * 17576) = 1.3668032 × 10 ^ 17 seconds = 4.3341 billion years.

That's quite a long time!

"""