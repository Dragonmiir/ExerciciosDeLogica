'''
Exercício 1 (Todos os exercícios desta lista são do site https://www.w3resource.com/python-exercises/python-basic-exercises.php)

Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
'''

# solução (Correta)

'''
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star,\
      \n\tHow i Wwonder what you are")
'''

'''
Exercício 2

Write a Python program to find out what version of Python you are using.
'''

import sys

print("Python Version")
print(sys.version)

print("Version information")
print(sys.version_info)
