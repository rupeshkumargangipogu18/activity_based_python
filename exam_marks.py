n=int(input("enter the number of subjects:"))

total=0
failed=0

for i in range(1,n+1):
    marks=int(input("enter the marks:"))


    if marks <0 and marks>100:
        print("invalid marks!")
        failed=failed+1
        continue

    if marks<35 and marks >=30:
        marks=35
        print("Gracee marks are applied!")
    print("final marks !" , marks)

    if marks < 35 :
        print("failed")
        failed=failed+1
    else:
        print("pass")

    total=total+marks

print("\n total marks:" , total ,"/",n*100)
percentage=(total/(n*100))*100
print(percentage, round(percentage, 2) ,"%")


if failed >0:
    print("final result:Fail")
else:
    print("final result:Pass")


if percentage >=75:
    print("Distinction")
elif percentage >=60:
    print("first class")
elif percentage >=50:
    print("second class")
else:
    print("third class")