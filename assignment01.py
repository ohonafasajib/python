# 1. Write a python program to accept two integers and check whether they are equal or not.
num1 = int(input("please enter your 1st number = "))
num2 = int(input("please enter your 2nd number = "))
 if num1 == num2:
     print("your provided numbers are equal.")
 else:
     print("your provided numbers are not equal.")

# 2. Write a python program to check whether a given number is positive or negative.
num1 = int(input("Please enter your 1st number = "))
if num1 < 0:
    print("Your number is a negative number.")
elif num1 == 0:
    print("Your number is zero which is a non-negative number.")
elif num1 > 0:
    print("Your number is a positive number.")

# 3. Write a python program to accept a coordinate point in a XY 
#    coordinate system and determine in which quadrant the coordinate point lies.
x = int(input("Enter your values of X = "))
y = int(input("Enter your values of Y = "))
if  x == y == 0:
    print("your values are pointing into the ORIGIN.")
elif    x > 0 and y > 0:
    print("your values are pointing into the 1st quadrant.")
elif    x < 0 and y > 0:
    print("your values are pointing into the 2nd quadrant.")
elif    x < 0 and y < 0:
    print("your values are pointing into the 3rd quadrant.")
elif    x > 0 and y < 0:
    print("your values are pointing into the 4rd quadrant.")

# 4. Write a python program to check whether an alphabet is a vowel or consonant.
alphabet = input("Enter your desired alphabet to know its vowl or consonant = ")
if alphabet in ('a','A','e','E','i','I','o','O','u','U'):
    print("Your alphabet %s is a vowl." % alphabet)
else:
    print("Your alphabet %s is a consonant." % alphabet)

# 5. Write a python program to check whether a number is a even or odd.
num = int(input("Please enter your number = "))
if  num%2 == 0:
    print("your number %s is an even number." % num)
else:
    print("your number %s is an odd number." % num)