import math
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

mark = (float(input("Enter your Grade: ")))
grade = round_half_up(mark)
if grade >= 97 and grade <= 100:
    print("Grade/Mark: 1.0")
    print("Description: Excellent")

elif grade >=94 and grade <= 96:
    print("Grade/Mark: 1.25")
    print("Description: Excellent")
    
elif grade >=91 and grade <= 93:
    print("Grade/Mark: 1.5")
    print("Description: Very Good")
    
elif grade >= 88 and grade <= 90:
    print("Grade/Mark: 1.75")
    print("Description: Very Good")
    
if grade >= 85 and grade <= 87:
    print("Grade/Mark: 2.0")
    print("Description: Good")

elif grade >=82 and grade <= 84:
    print("Grade/Mark: 2.25")
    print("Description: Good")
    
elif grade >=79 and grade <= 81:
    print("Grade/Mark: 2.5")
    print("Description: Satisfactory")
    
elif grade >= 76 and grade <= 78:
    print("Grade/Mark: 2.75")
    print("Description: Satisfactory")
    
elif grade == 75:
    print("Grade/Mark: 3.0")
    print("Description: passing")
    
elif grade >=65 and grade <=74:
    print("Grade/Mark: 5.0")
    print("Description: Failure, Better luck next time")
    
grade = input("Enter your the status of you mark (Inc.,W,D):")
if grade == "Inc.":
        print("Your status on this subject is INCOMPLETE.")
elif grade == "W":
        print("Your status on this subject is WITHDRAWN")
elif grade == "D":
        print("Your status on this subject is DROPPED")

print("Your grade is recorded!")