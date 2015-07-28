#########################################################
#Name: Shilpa Poloju
#Class: CMPS 5363 Cryptography
#Date: 28th July 2015
#Program 2 - Randomized Vigenere Cipher
#########################################################

import random


#########################################################
# keywordFromSeed -
#    Works by peeling off two digits at a time, and using modulo to map it into
#    the proper range of A-Z for use as a keyword.
# Example:
#    This example spells math, and I chose values 0-25 on purpose, but
#    it really doesn't matter what values we choose because 99 % 26 = 21 or 'V' 
#    or any value % 26 for that matter.
#
#    seed = 12001907
#    l1   = 12001907 % 100 = 07 = H
#    seed = 12001907 // 100 = 120019
#    l2   = 120019 % 100 = 19 = T
#    seed = 120019 // 100 = 1200
#    l3   = 1200 % 100 = 0 = A
#    seed = 1200 // 100 = 12
#    l4   = 12 % 100 = 12 = M
#    seed = 12 // 100 = 0
#
# @param {int} seed - An integer value used to seed the random number generator
#                     that we will use as our keyword for vigenere
# @return {string} keyword - a string representation of the integer seed
##############################################################

symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
n = len(symbols)
vigenere = [[0 for i in range(n)] for i in range(n)]

#generating a key based on the seed value
def keywordFromSeed(seed):
    Letters = []

    while seed > 0:
        Letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 100
    return ''.join(Letters)
 
################################################################

chars = ' '
for i in range(32,127):
	chars += chr(i)
	#print(chars)
	size=len(chars)
	#print(size)

#constructing a 95X95 matrix randomly	
def buildVigenere(symbols,seed):
    random.seed(seed)

    
    symbols = list(symbols)
    random.shuffle(symbols)
    symbols = ''.join(symbols)
    
    for sym in symbols:
        random.seed(seed)
        myList = []
    
        for i in range(n):
            r = random.randrange(n)
            
            if r not in myList:
                myList.append(r)
            else:
                while(r in myList):
                    r = random.randrange(n)
            
                myList.append(r)
                               
            while(vigenere[i][r] != 0):
                r = (r + 1) % n
            
            vigenere[i][r] = sym

######################################################################

#function to create and print randomized vigenere matrix
def printMatrix():
    i=0
    j=0
    k=0
    line = ""

    for i in range(len(symbols)*len(symbols)):
        line = line + vigenere[j][k]
        j = j + 1
        if j >= 26:
            print(line)
            line = ""
            j = 0
            k = k + 1	
			
#############################################################

#function to encrypt a plain text using seed as a keyword
def encrypt(Message,SeedVal):
	buildVigenere(symbols,SeedVal)
	KeyVal = keywordFromSeed(SeedVal)
	ki=0
	encriptedVal = ""
	#print("**************",Message)
	#print("**************",KeyVal)
	for mi in range(len(Message)-1):
		row = ord(KeyVal[ki]) - 32
		col = ord(Message[mi])- 32
		encriptedVal = encriptedVal + str(vigenere[row][col])
		#print("*******",row)
		#print("*******",col)
		#print("*******",str(vigenere[row][col]))
		ki = ki+1
		ki = ki % len(KeyVal)
	return encriptedVal

###############################################################

#function to decrypt an encrypted text using seed as a keyword
def decrypt(encriptedVal,SeedVal):
	buildVigenere(symbols,SeedVal)
	KeyVal = keywordFromSeed(SeedVal)
	mi = 0
	ki = 0
	
	decryptedVal = ""
	#print("**************",encriptedVal)
	#print("**************",KeyVal)
	
	for mi in range(len(encriptedVal)):
		row = ord(KeyVal[ki]) - 32
		for i in range(len(symbols)):
			if(encriptedVal[mi]==vigenere[row][i]):
				decryptedVal=decryptedVal + chr(i+32)
		ki = ki+1
		ki = ki % len(KeyVal)	
	return decryptedVal
#################################################################