days = int(input("Enter number of days: "))

limit = 20 

for i in range(days):
    print("\nDay", i + 1)

    prepared = int(input("Enter meals prepared: "))
    served = int(input("Enter meals served: "))
    leftovers = int(input("Enter leftover meals: "))

    if prepared <= 0 or served < 0 or leftovers < 0:
        print("Invalid input")
    elif served + leftovers > prepared:
        print("Invalid data: meals exceed prepared meals")
    else:
        percentage = (leftovers / prepared) * 100

        print("Wastage percentage:", round(percentage, 2), "%")

        if percentage > limit:
            print("Warning: Food wastage is too high!")
        else:
            print("Food wastage is acceptable.")