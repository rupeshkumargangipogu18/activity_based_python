balance=1000
withdrawl_limit=500
deposit=0
withdrawls=0

n=int(input("enter the number of transactions:"))

for i in range(n):
    print("\n1.deposit")
    print("2.withdraw")


    choice=int(input("enter your choice:"))
    amount=float(input("enter your amount"))

    if amount<0:
        print("invalid transcation!")

    elif choice ==1:
        balance=balance+amount
        deposit=deposit+amount
        print("Deposit succesful!")

    elif choice ==2:
        if amount> withdrawl_limit:
            print("withdrawl_limit exceeded!")
        elif amount > balance:
            print("insufficient balance!")
        else:
            balance=balance-amount
            withdrawls=withdrawls+amount
            print("Withdrawl successsful")

    else:
        print("invalid choice!")

print("\n====transaction summary===")
print("Total deposits:", deposit)
print("Total withdrawls:" ,withdrawls)
print("Final balance:" , balance)