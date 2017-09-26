'''
Logan Rogers
CS 3600 Project #2
11/18/2016
'''

'''
GCD AND LINEAR COMBINATION FUNCTION
This function recursively loops through, using the fact that
GCD(a,b) = GCD(b, a mod b) to find the answer for the GCD 
(Euclid's Algorithm)
After finding the GCD, the function returns, backtracking through
the steps of Euclid's algorithm (maintained via recursion) to find
the values of X and Y in the linear combination GCD = aX + bY
(Extended Euclidean Algorithm)
'''
def GCDLC(a,b):
	if b == 0:
		return[1,0,a]			 #Default case/end condition
	else:
		x,y,d = GCDLC(b, a%b)	 #Recursive call
		return y, x-(a//b)*y, d  #Backtracking

if __name__ == '__main__':

	'''
	GENERATING PRIVATE KEY d AND CALCULATING n
	Here we get user input for the source file containing p, q, and e.
	We then computes n = p*q and totient = (p-1)(q-1).
	We know e and totient are coprime, so we run GCDLC(e, totient) get x, the
	coefficient of e.  This gives us d, since e(x) = -(totient)y + 1 and we are
	solving for ed = 1 + k(totient)
	'''
	#Get file containing p, q, e
	input_file = raw_input('Enter the name of the file containing p, q, e: ')

	#Get output file for d, n
	output_file_name = raw_input('Enter the name of the output file for d and n: ')

	#Retrieve p,q,e
	with open(input_file) as f:
		p = f.readline() #line 1
		q = f.readline() #line 2
		e = f.readline() #line 3
	f.close()

	#convert p, q, e to longs (read in as strings earlier)
	p = long(p)
	q = long(q)
	e = long(e)

	#get values N and the totient value
	n = p*q
	totient = (p-1)*(q-1)

	#Use Extended Euclidean Algorithm (in GCDLC) to return value gcd, x, y
	#x will represent our private key, d
	x, y, gcd = GCDLC(e, totient)
	d = x
	if d < 0:
		d = d % totient

	#output to file
	output_file = open(output_file_name, 'w')
	output_file.write(str(d))
	output_file.write('\n')
	output_file.write(str(n))
	output_file.close()

	'''
	ENCRYPTION
	Here we get user input for the source file of the message x to be encrypted.
	We then compute the cipher of the message and outputs it to a user selected file.
	The message is encrypted using the formula: c = m^e mod n
	'''

	#Get input file for x
	input_file = raw_input('Enter the name of the file containing x to be encrypted: ')

	#Get output file for E(x)
	output_file_name = raw_input('Enter the name of the file to output E(x) (encrypted x): ')

	#Retrieve x
	with open(input_file) as f:
		x = f.readline()
	f.close()

	#x expected as a number.  Convert x from string to long
	x = long(x)

	#Compute the cipher text (encrypt x, using e and n)
	cipher = (x**e) % n

	#Output cipher to file
	output_file = open(output_file_name, 'w')
	output_file.write(str(cipher))
	output_file.close()

	'''
	DECRYPTION
	Here we get user input for the source file of the encrypted message (ciphertext)
	and then compute the value of message to be output to a user selected file.
	The message is decrypted using the formula: M = c^d mod n
	'''

	#Get file containing ciphertext c to be decrypted
	input_file = raw_input('Enter the name of the file containing ciphertext (c): ')

	#Get output file for d, n
	output_file_name = raw_input('Enter the name of the output file for D(c) (decrypted c): ')

	#Retrieve c
	with open(input_file) as f:
		c = f.readline()
	f.close()

	#Convert c from string to long
	c = long(c)

	#Compute message (decrypt c, using d and n)
	message = (c**d) % n

	#Output to file
	output_file = open(output_file_name, 'w')
	output_file.write(str(message))
	output_file.close()