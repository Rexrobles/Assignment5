import math
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

Mark = round(float(input("Enter you mark:")))
grade = round_half_up (Mark)
if grade >= 97 and grade <= 100:
    print("Excellent!")
    print("Your mark is 1.0!")
elif grade >= 94 and grade <= 96:
    print("Excellent!")
    print("Your mark is 1.25!")
elif grade >= 91 and  grade <= 93:
    print("Very Good!")
    print("Your mark is 1.5!")
elif grade >= 88 and grade <= 90:
    print("Very Good!")
    print("Your mark is 1.75!")
elif grade >= 85 and grade <= 87:
    print("Good!")
    print("Your mark is 2.0!")
elif grade >= 82 and grade <= 84:
    print("Good!")
    print("Your mark is 2.25!")
elif grade >= 79 and grade <= 81:
    print("Satisfactory!")
    print("Your mark is 2.50!")
elif grade >= 76 and grade <= 78:
    print("Satisfactory!")
    print("Your mark is 2.75!")
elif grade == 75:
    print("Passing!")
    print("Your mark is 3.0!")
elif grade >= 65 and grade <= 74:
    print("Failure!")
    print("Your mark is 5.0!")

grade = input("Enter your the status of you mark (Inc.,W,D):")
if grade == "Inc.":
        print("Your status on this subject is INCOMPLETE.")
elif grade == "W":
        print("Your status on this subject is WITHDRAWN")
elif grade == "D":
        print("Your status on this subject is DROPPED")

print("Your grade is recorded!")
   