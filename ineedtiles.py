#This program calculates how many
#tiles you need when tiling the floor

length = float(input("Enter room length:"))
width = float(input("Enter room width"))

#length = 4.0
#width = 2.0

area = length * width

needed = area * 1.05

print ("You need", needed, "tiles in square meters")