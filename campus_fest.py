
# Campus Festival Registration and Financial Audit

participants = []
fees = 0

n = int(input("Enter number of participants: "))

for i in range(n):
    name = input("Enter participant name: ")

    if name in participants:
        print("Duplicate registration!")
    else:
        participants.append(name)
        fee = int(input("Enter registration fee: "))
        fees = fees + fee

sponsorship = int(input("Enter sponsorship amount: "))
expenses = int(input("Enter total expenses: "))

balance = fees + sponsorship - expenses

print("\n--- Festival Report ---")
print("Valid Participants:", len(participants))
print("Registration Fees:", fees)
print("Sponsorship:", sponsorship)
print("Expenses:", expenses)
print("Final Balance:", balance)

if balance >= 0:
    print("Festival Result: Profit")
else:
    print("Festival Result: Loss")