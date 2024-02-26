import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def validate_input(username,email,password,password2):		
	if (len(username) < 5):
		return "Username too short"

	if(not re.fullmatch(regex, email)):
		return "Invalid Email"

	alpha = 0

	if (len(password) < 8):
		return "Weak Password"

	for char in password:
		if (char.isalpha()):
			alpha += 1

	if ((len(password) - alpha) < 4):
		return "Password should contain at minimum 4 digits"

	if (password != password2):
		return "Passwords don't match"

	return "valid"

 
