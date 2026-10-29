
budget = int(input("Enter your budget: "))
data = int(input("Enter required data in GB: "))
days = int(input("Enter required validity in days: "))

best_price = 99999
best_plan = "No plan"

for i in range(3):
    print("\nEnter details for Plan", i + 1)

    price = int(input("Enter plan price: "))
    plan_data = int(input("Enter data in GB: "))
    validity = int(input("Enter validity in days: "))

    if plan_data >= data and validity >= days and price <= budget:
        if price < best_price:
            best_price = price
            best_plan = "Plan " + str(i + 1)

if best_plan != "No plan":
    print("\nBest plan:", best_plan)
    print("Price:", best_price)
else:
    print("\nNo suitable plan found")