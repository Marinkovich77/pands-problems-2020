# Mario Stolba
# This program asks the user to input any positive
# integer and outputs the successive values of
# the following calculation:
# at each step it calculates the next value by
# taking the current value and, if it is even,
# divides it by 2, but if it is odd, multiplies
# it by 3 and adds 1
# Program ends if the current value is 1

# My initial mistake in making this program was corrected
# thanks to idea given by GMIT colleague Efim Teleaga
#https://learnonline.gmit.ie/mod/forum/discuss.php?d=7714#p12015

a = int(input("Enter any positive integer number: "))
b = 2

# Purpose of the condition in line 21 is to run the 
# program until value of variable a becomes 1

while a > 1:

# Lines 27 and 28 define that if the current value
# is even, it is divided by 2 
# Lines define that if the current value is odd, it
# is multiplies by 3 and 1 is added
    if a % b == 0:
         a = a / 2    
    else:
        a = a * 3 + 1
    print(int(a))     