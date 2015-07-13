######################################################################
# Name:Shilpa Poloju
# Class: CMPS 5363 Cryptography
# Date: 13 July 2015
# Program1 - Playfair Cipher
######################################################################

import pprint
import re

class StringManip:
    """
    Helper class to speed up simple string manipulation
    """

    def generateAlphabet(self):
        #Create empty alphabet string
        alphabet = ""

        #Generate the alphabet
        for i in range(0,26):
            alphabet = alphabet + chr(i+65)

        return alphabet


    def cleanString(self,s,options = {'up':1,'reNonAlphaNum':1,'reSpaces':'','spLetters':'X'}):
        """
        Cleans message by doing the following:
        - up            - uppercase letters
        - spLetters     - split double letters with some char
        - reSpaces      - replace spaces with some char or '' for removing spaces
        - reNonAlphaNum - remove non alpha numeric
        - reDupes       - remove duplicate letters
        @param   string -- the message
        @returns string -- cleaned message
        """
        if 'up' in options:
            s = s.upper()

        if 'spLetters' in options:
            #replace 2 occurrences of same letter with letter and 'X'
            s = re.sub(r'([ABCDEFGHIJKLMNOPQRSTUVWXYZ])\1', r'\1X\1', s)

        if 'reSpaces' in options:
            space = options['reSpaces']
            s = re.sub(r'[\s]', space, s)

        if 'reNonAlphaNum' in options:
            s = re.sub(r'[^\w]', '', s)

        if 'reDupes' in options:
            s= ''.join(sorted(set(s), key=s.index))

        return s


class PlayFair:
    """
    Class to encrypt via the PlayFair cipher method
    Methods:
    - generateSquare
    - transposeSquare
    -
    """

    def __init__(self,key,message):
        self.Key = key
        self.Message = message
        self.Square = []
        self.Transposed = []
        self.StrMan = StringManip()
        self.Alphabet = ""

        self.generateSquare()
        self.transposeSquare()

        self.Message = self.StrMan.cleanString(self.Message,{'up':1,'reSpaces':'','reNonAlphaNum':1,'spLetters':1})

    def generateSquare(self):
        """
        Generates a play fair square with a given keyword.
        @param   string   -- the keyword
        @returns nxn list -- 5x5 matrix
        """
        row = 0     #row index for sqaure
        col = 0     #col index for square

        #Create empty 5x5 matrix
        self.Square = [[0 for i in range(5)] for i in range(5)]

        self.Alphabet = self.StrMan.generateAlphabet()

        #uppercase key (it may be read from stdin, so we need to be sure)
        self.Key = self.StrMan.cleanString(self.Key,{'up':1,'reSpaces':'','reNonAlphaNum':1,'reDupes':1})

        #Load keyword into square
        for i in range(len(self.Key)):
            self.Square[row][col] = self.Key[i]
            self.Alphabet = self.Alphabet.replace(self.Key[i], "")
            col = col + 1
            if col >= 5:
                col = 0
                row = row + 1

        #Remove "J" from alphabet
        self.Alphabet = self.Alphabet.replace("J", "")

        #Load up remainder of playFair matrix with
        #remaining letters
        for i in range(len(self.Alphabet)):
            self.Square[row][col] = self.Alphabet[i]
            col = col + 1
            if col >= 5:
                col = 0
                row = row + 1

    def transposeSquare(self):
        """
        Turns columns into rows of a cipher square
        @param   list2D -- playFair square
        @returns list2D -- square thats transposed
        """
        #Create empty 5x5 matrix
        self.Transposed = [[0 for i in range(5)] for i in range(5)]

        for col in range(5):
            for row in range(5):
               self.Transposed[col][row] = self.Square[row][col]


    def getCodedDigraph(self,digraph):
        """
        Turns a given digraph into its encoded digraph whether its on
        the same row, col, or a square
        @param   list -- digraph
        @returns list -- encoded digraph
        """
        newDigraph = ['','']

        #Check to see if digraph is in same row
        for row in self.Square:
            if digraph[0] in row and digraph[1] in row:
                newDigraph[0] = row[((row.index(digraph[0])+1)%5)]
                newDigraph[1] = row[((row.index(digraph[1])+1)%5)]
                return newDigraph

        #Check to see if digraph is in same column
        for row in self.Transposed:
            if digraph[0] in row and digraph[1] in row:
                newDigraph[0] = row[((row.index(digraph[0])+1)%5)]
                newDigraph[1] = row[((row.index(digraph[1])+1)%5)]
                return newDigraph


        #Digraph is in neither row nor column, so it's a square
        location1 = self.getLocation(digraph[0])
        location2 = self.getLocation(digraph[1])

        return self.Square[location1[0]][location2[1]] + self.Square[location2[0]][location1[1]] 
        
   
    def getDCodedDigraph(self,digraph):
        """
        Turns a given digraph into its decoded digraph whether its on
        the same row, col, or a square
        @param   list -- digraph
        @returns list -- decoded digraph
        """
        newDigraph = ['','']

        #Check to see if digraph is in same row
        for row in self.Square:
            if digraph[0] in row and digraph[1] in row:
                newDigraph[0] = row[((row.index(digraph[0])-1)%5)]
                newDigraph[1] = row[((row.index(digraph[1])-1)%5)]
                return newDigraph

        #Check to see if digraph is in same column
        for row in self.Transposed:
            if digraph[0] in row and digraph[1] in row:
                newDigraph[0] = row[((row.index(digraph[0])-1)%5)]
                newDigraph[1] = row[((row.index(digraph[1])-1)%5)]
                return newDigraph


        #Digraph is in neither row nor column, so it's a square
        location1 = self.getLocation(digraph[0])
        location2 = self.getLocation(digraph[1])

       
        return self.Square[location1[0]][location2[1]] + self.Square[location2[0]][location1[1]] 
       
      
      
    def getLocation(self,letter):
        row = 0
        col = 0

        count = 0
        for list in self.Square:
            if letter in list:
                row = count
            count += 1

        count = 0
        for list in self.Transposed:
            if letter in list:
                col = count
            count += 1
        return [row,col]

    #############################################
    # Helper methods just to see what's going on
    #############################################
    def printNewKey(self):
        print(self.Key)

    def printNewMessage(self):
        print(self.Message)
        return self.Message

    def printSquare(self):
        for list in self.Square:
            print(list)
        print('')

    def printTransposedSquare(self):
        for list in self.Transposed:
            print(list)
        print('')

		
###########################################################################

print ("Welcome !! Please enter 1 for Encrypt, 2 for Decrypt and 3 for Exit")
print (' ')
temp = "";
str=""
c = True
c2 = True
##################################################################################
#while loop for selection of encryption, decryption and exit with there operations
##################################################################################
while c:
    while c2:
        func = input('1: Encrypt\n 2: Decrypt \n 3: Exit\n')
        if func == '1':
            print('PlayfairEncryption Tool(P.E.T)')
            print('Written by Shilpa Poloju')
            print('***************************')
            print('Encrypt')
            print ('Enter the message & Key:')
            while True:
                message = input('Enter Message:')
                print (' ')
                key = input('Enter Key:')
                print (' ')
                print('***************************')
                print ('Encrypting.....')
                myCipher = PlayFair(key,message)
                myCipher.printNewKey()
                newMessage = myCipher.printNewMessage()
                myCipher.printSquare()
                myCipher.printTransposedSquare()
                i=0 
                print(newMessage)
				
				#loop for traversing the entire message 
                while(i<len(newMessage)-1):
                    
                    returnValue = myCipher.getCodedDigraph([newMessage[i],newMessage[i+1]])
                   
                    temp = temp + str.join(returnValue)
                   
                    i=i+2
                print('')    
                print(temp)
                c2 = False
                break
        elif func == '2' :
            print('PlayfairEncryption Tool(P.E.T)')
            print('Written by Shilpa Poloju')
            print('***************************')
            print ("Decrypt")
            print ('Enter the message & Key:')
            while True:
                message = input('Enter Encrypted Message:')
                print (' ')
                key = input('Enter Key:')
                print (' ')
                print('***************************')
                print ('Decrypting.....')
                myCipher = PlayFair(key,message)
                myCipher.printNewKey()
                newMessage = myCipher.printNewMessage()
                myCipher.printSquare()
                myCipher.printTransposedSquare()
                i=0 
                print(newMessage)
				
				#loop for traversing entire message
                while(i<len(newMessage)-1):
                                           
                    returnValue = myCipher.getDCodedDigraph([newMessage[i],newMessage[i+1]])
                    
                    temp = temp + str.join(returnValue)
                               
                    i=i+2
                    temp = temp.replace('X','')
                print('')
                print(temp)
                c2 = False
				break
        elif func == '3' :
            break
 
