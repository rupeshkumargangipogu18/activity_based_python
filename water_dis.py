# Water Distribution Fairness Analysis

areas = ["Area A", "Area B", "Area C"]
demand = [0, 0, 0]
supply = [0, 0, 0]

days = int(input("Enter number of days: "))

for day in range(days):
    print("\nDay", day + 1)

    for i in range(3):
        d = int(input("Enter demand for " + areas[i] + ": "))
        s = int(input("Enter supply for " + areas[i] + ": "))

        demand[i] += d
        supply[i] += s

print("\n--- Water Distribution Report ---")

shortages = []

for i in range(3):
    shortage = max(0, demand[i] - supply[i])
    shortages.append(shortage)

    if demand[i] > 0:
        percentage = supply[i] / demand[i] * 100
    else:
        percentage = 0

    print("\nArea:", areas[i])
    print("Total Demand:", demand[i])
    print("Total Supply:", supply[i])
    print("Shortage:", shortage)
    print("Supply Percentage:", round(percentage, 2), "%")

worst = shortages.index(max(shortages))

print("\nMost Underserved Area:", areas[worst])
print("Highest Shortage:", shortages[worst])