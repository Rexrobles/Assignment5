def lowest_of_three():
    a = int(input("First Number: "))
    b = int(input("Second Number: "))
    c = int(input("Thrid Number: "))
    lowest = a
    if b < lowest:
        lowest = b
        if c < lowest:
            lowest = c
    return lowest     
lowest3 = lowest_of_three()
print(lowest3)
