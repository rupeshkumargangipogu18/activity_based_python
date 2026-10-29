# Campus Event Financial Planning
venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
catering = float(input("Enter catering cost per person: Rs. "))
transport = float(input("Enter transport cost: Rs. "))
certificate = float(input("Enter certificate cost per person: Rs. "))

participants = int(input("Enter expected participants: "))
sponsorship = float(input("Enter sponsorship amount: Rs. "))
contribution = float(input("Enter registration fee per person: Rs. "))

fixed_cost = venue + equipment + transport
person_cost = catering + certificate

total_cost = fixed_cost + (person_cost * participants)


registration_money = contribution * participants
total_income = registration_money + sponsorship


shortfall = max(0, total_cost - total_income)

if contribution > person_cost:
    required = (fixed_cost - sponsorship) / (contribution - person_cost)

    if required < 0:
        required = 0

    required = int(required) + (required % 1 > 0)
else:
    required = 0

print("\n--- EVENT FINANCIAL SUMMARY ---")
print("Fixed Cost: Rs.", fixed_cost)
print("Total Event Cost: Rs.", total_cost)
print("Registration Income: Rs.", registration_money)
print("Sponsorship: Rs.", sponsorship)
print("Total Income: Rs.", total_income)
print("Sponsorship Shortfall: Rs.", shortfall)

if contribution > person_cost:
    print("Minimum Participants to Break Even:", required)
else:
    print("Break-even not possible with this registration fee.")