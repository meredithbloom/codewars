# Vigenère Cipher Helper - 4 kyu
# The Vigenère cipher is a classic cipher originally developed by Italian cryptographer Giovan Battista Bellaso and published in 1553. It is named after a later French cryptographer Blaise de Vigenère, who had developed a stronger autokey cipher (a cipher that incorporates the message of the text into the key).

# The cipher is easy to understand and implement, but survived three centuries of attempts to break it, earning it the nickname "le chiffre indéchiffrable" or "the indecipherable cipher."

'''
From wikipedia...
The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It is a simple form of polyalphabetic substitution.
. . .

In a Caesar cipher, each letter of the alphabet is shifted along some number of places; for example, in a Caesar cipher of shift 3, A would become D, B would become E, Y would become B and so on. The Vigenère cipher consists of several Caesar ciphers in sequence with different shift values.

Assume the key is repeated for the length of the text, character by character. Note that some implementations repeat the key over characters only if they are part of the alphabet -- this is not the case here.

The shift is derived by applying a Caesar shift to a character with the corresponding index of the key in the alphabet.

Visual representation:
"my secret code i want to secure"  // message
"passwordpasswordpasswordpasswor"  // key

Write a class that, when given a key and an alphabet, can be used to encode and decode from the cipher.

'''

abc = "abcdefghijklmnopqrstuvwxyz"
key = 'password'

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        # to find index count to shift letter
        self.alphabet = alphabet
        # to repeat until it matches length of string to encode/decode
        self.key = key
        
    
    # function to match repeated key to string
    def repeat_key(self, key, target_length):
        return (self.key * (target_length//len(self.key)+1))[:target_length]
    
    
    def encode(self, text):
        new_key = self.repeat_key(self.key, len(text))
        #print(new_key)
        text = list(text)
        for i in range(len(text)):
            # only convert chars in given alphabet
            if (text[i] in abc):
                letter, match = text[i], new_key[i]
                start_index, shift = self.alphabet.index(letter), self.alphabet.index(match)
                new_index = start_index + shift
                #print(new_index)
                if new_index >= len(self.alphabet):
                    new_index = new_index - len(self.alphabet)
                #print(letter, match, self.alphabet[new_index])
                text[i] = self.alphabet[new_index]
        print("".join(text))
        return("".join(text))
                
            
    def decode(self, text):
        new_key = self.repeat_key(self.key, len(text))
        text = list(text)
    

c = VigenereCipher(key, abc)
c.encode('my secret code i want to secure')
c.encode('codewars')