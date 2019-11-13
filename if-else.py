money=int(input("money for party"))
if money>=50:
    print("Congrates, you can go for party")
else:
    print("Sorry you don't have enough money")

#write a program to tell if the user is eligible to drive or not.
# Hint:should be above 18 years of age#
age=int(input("Enter your age"))
if age>=18:
    print("You are eligible to drive")
else:
    print("You are not aligible to drive")

#Write a program for grading the students based on the marks:
# 90 to 100-A,70-90-B,40-70-C,Below 40-Fail#
marks=int(input("Enter the marks of student"))
if marks>=90:
    print("Your grade is A")
elif marks>=70 and marks<90:
    print("Your grade is B")
elif marks>=40 and marks<70:
    print("Your grade is C")
else:
    print("Fail")


