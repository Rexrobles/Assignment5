def lowest_of_three():
    a = int(input("First Number: "))
    b = int(input("Second Number: "))
    c = int(input("Thrid Number: "))
    if a < b and a < c:
        print(f"The lowest number among the three is {a}. ")
    elif b < a and b < c:
        print(f"The lowest number among the three is {b}.")
    else:
        print(f"The lowest number among the three is {c}.")
        
lowest_of_three()
print("-DONE-")
    