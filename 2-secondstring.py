# Mario Stolba
# Weekly task 3
# This program asks a user to input a string 
# and outputs every second letter in reverse order

# [::-1] puts the string (sentence enterd by user) in a
# reverse order. It means start at the end of the
# string and end at position of 0; move with a step
# -1 (negative one). I found this solution at
# https://www.w3schools.com/python/python_howto_reverse_string.asp
s = input("Please enter a sentence:") [::-1]

# Line 21 prints the slice of the string in reverse order
# from character 0 (which is . and which is included) 
# to character 44 (which is not included in the slice)
# Hence [0:44:2] - print from character 0 (including it)
# to character 44 (not including it). 2 means print every
# second character in that slice. 44 is number of characters
# in the slice i.e in the sentence The quick brown fox jumps 
# over the lazy dog. (including space)
print(s[0:44:2])