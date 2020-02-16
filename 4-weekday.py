# Mario Stolba

# Program which informs the user if
# today is weekday or a weekend

# We are importing datetime module
import datetime

# We are creatingdefining variable `now` and conferring
# it the value datetime.datetime.now() 
# That variable is a instance of a class 
# or sort of a dictionary. It has the following
# elements: year, month, day, hour, min, sec, ms 
now = datetime.datetime.now()

# now.weekday() is variable value of which depends
# on actual day of the week (it`s 0 for Mon, 1 for Tue,
# 2 for Wed, 3 for Thu, 4 for Fri, 5 for Sat, 6 for Sun).
# So if it`s less or equal 4, it`s weekday, so we get:
# "Yes, unfortunately today is weekend" message
if now.weekday() <= 4:
        print("Yes, unfortunately today is a weekday")

# If now.weekday() has values 5 or 6, it`s weekend,
# so we get "It`s weekend, yay" message
else:
    print("It is the weekend, yay!")