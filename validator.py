# ---------------------------------------------------
#    Name: FATIMA REHMATULLAH
#    ID: 1631703
#    CMPUT 274, Fall  2020#
#    Weekly Assignment#1: Password Validator
# --------------------------------------------------


def validate(password):
	"""Analyzes an input password to determine if it is "Secure", "Insecure", or "Invalid" based on the assignment description criteria.
	Arguments:
	password(string):a string of characters
	Returns:result (string): either "Secure", "Insecure", or "Invalid". 
	"""

#initialize all the lists used
	forbiddencharacters = ["", "@", "#"]
	specialcharacters = ["!", "-", "$", "%", "&", "'", "(", ")", "*", "+", ",", ".", "/", ":", ";", "<", "=", ">", "?", "_", "[", "]", "^", "`", "{", "|", "}", "~"]
	Digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	#define and assign values to all the variables
	result = ""
	length = len(password)
	forbidden = 0 
	dtot = 0
	Lowercase = 0
	Uppercase = 0
	sc = 0
	Invalid = False
	Secure = False
	Securecondition2 = False
	#check for forbidden digits in the password
	#calculate and save the number of digits, uppercase, lowercase and special
	#runs the for loop for the whole legnth of the 
	#inputted password to check every character
	for i in password:
		if i in forbiddencharacters:
			forbidden = forbidden+1
		elif i in Digits:
		    dtot = dtot+1
		elif (i.isupper()):
		    Uppercase = Uppercase+1
		elif (i.islower()):
		    Lowercase = Lowercase+1
		elif i in specialcharacters:
			sc = sc+1
			#identifies if the password is strong enough 
	if dtot>=1 and sc>=1 and Uppercase>=1 and Lowercase>=1:
		Securecondition2 = True
		#deems the password invalid if it is smaller than 8 characters or contains forbidden characters
	if length<8 or forbidden>=1:
		Invalid = True
		result = "Invalid"
		#deems the password secure if it is not invalid and meets the secure condition
	elif Invalid == False and Securecondition2 == True:
		result = "Secure"
		Secure = True
		#deems the password insecure if it is neither invalid nor secure
	elif Invalid == False and Secure == False:
		result = "Insecure"

	return(result)
pass

def generate(n):
	"""Generates a password of length n which is guaranteed to be Secure according to the given criteria.
	Arguments:
	n(integer):the length of the password to generate, n >= 8.
	Returns:
	secure_password (string):a Secure password of length n. 
	"""

	import random
	#define all of the characters seperately that 
	#can be used to generate passwords
	digits = "0123456789"
	lowercase = "abcdefghijklmnopqrstuvwxyz"
	uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	special = "!-$%&'()*+,./:;<=>?_[]^`{|}~"
	secure_password = ""
	#keeps the loop running until the password 
	#equals the legnth argument passed
	#also makes sure the legnth of the 
	#generated password is greater than 8
	while n>=8 and len(secure_password)!=n:
		secure_password = secure_password + random.choice(lowercase)
		#after each addition, the program checks the pwd length
		#if it exceeds n, the loop breaks
		#in order to not exceed the legnth.
		if len(secure_password) == n:
			break
		secure_password = secure_password + random.choice(uppercase)
		if len(secure_password)==n:
			break
		secure_password = secure_password + random.choice(digits)
		if len(secure_password)==n:
			break 
		secure_password = secure_password + random.choice(special)
	if n<8:
		secure_password="Only passwords longer than (or equal to) 8 characters are generated."
	return secure_password
pass

if __name__ == "__main__":
	print(validate(input()))
	print(generate(int(input())))
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations.
pass