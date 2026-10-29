routes=int(input("enter the number of routes:"))

for i in range(routes):
    print("\nRoute" ,i+1)


    passengers=int(input("enter the passengers demand:"))
    capacity=int(input("enter the capacity of bus:"))

    busses=(passengers+capacity-1)//capacity

    avialabe_capacity=busses*capacity
    unserved=max(0,passengers-avialabe_capacity)

    print("Passengers:" , passengers)
    print("Bus capacity:", capacity)
    print("busses needed:", busses)
    print("unserved busses:",unserved)