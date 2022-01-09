def lowest_of_three():
    Firstnum = int(input("First Number: "))
    Secondnum = int(input("Second Number: "))
    Thirdnum = int(input("Thrid Number: "))
    if Firstnum < Secondnum and Firstnum < Thirdnum:
        print(f"The lowest number among the three is {firstnum}. ")
    elif Secondnum < Firstnum and Secondnum < Thirdnum:
        print(f"The lowest number among the three is {Secondnum}.")
    else:
        print(f"The lowest number among the three is {Thirdnum}.")
        
lowest_of_three()
print("-DONE-")
    