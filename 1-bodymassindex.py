# Mario Stolba
# Week 2 task
# This file calculates body mass index

# in the lines 9 and 10 float is used because without
# it Python would e.g. interpret inputed mass of 65kg
# as numbers 6 and 5

weight = float(input ("Enter weight in kg:"))
height = float(input ("Enter height in cm:"))

#In the line 19, (height/100) is used because
# we input height in cm and output must be
# weight in kg divided by height in METRES
# squared. One metre is 100cm. Operator **
# is used to raise
# the heigth in metres to the power of 2

BMI = weight / (height/100)**2

print("BMI is", BMI)