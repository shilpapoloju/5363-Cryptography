#########################################################
#Name: Shilpa Poloju
#Class: CMPS 5363 Cryptography
#Date: 28th July 2015
#Program 2 - Randomized Vigenere Cipher
#########################################################


import argparse
import sys
import randomized_vigenere as rv

def main():

	#adding parser arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
	parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
	parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
	parser.add_argument("-s", "--seed", dest="seed",help="Integer seed")

	args = parser.parse_args()

	#generating a keyword
	seed = args.seed

	f = open(args.inputFile,'r')
	message = f.read()

	#encrypting the plaintext
	if(args.mode == 'encrypt'):
		data = rv.encrypt(message,int(args.seed))
		o = open(args.outputFile,'w')
		o.write(str(data))
		o.close()
		#decrypting the encoded message
	else:
		data = rv.decrypt(message,int(args.seed))
		o = open(args.outputFile,'w')
		o.write(str(data))
		o.close()


if __name__ == '__main__':
	main()
