#traffic penality calculator
n=int(input("enter the number of violations:"))

total_fine=0
serious_count=0

for i in range(n):
    print("\nviolations" ,i+1)

    veichel=input("enter the type of veichel (bike/car):").lower()
    offence=input("enter the offence (speeding/no helmet/drunk and drive):").lower()
    repeat=input("Is it repeat offence?(yes/no):").lower()


    if offence == "speeding":
        fine = 1000
    elif offence == "nohelmet" and vehicle == "bike":
        fine = 500
    elif offence == "drinkdriving":
        fine = 10000
        serious_count += 1
    else:
        fine = 0
        print("Invalid offence or vehicle combination")

    if repeat == "yes" and fine > 0:
        fine = fine * 2

    total_fine = total_fine + fine

    print("Fine for this violation: Rs.", fine)


print("\nTotal Penalty: Rs.", total_fine)

if serious_count > 0:
    print("Warning: Possible driver disqualification. Check applicable law.")
else:
    print("No disqualification condition detected by this program.")
