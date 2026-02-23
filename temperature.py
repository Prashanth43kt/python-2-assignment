
while True:
    print("1.celsius to fahrenhit")
    print("2.fahrenhit to celsius")
    print("3.celsius to kelvin")
    print("4. kelvin to celsius")
    print("5.fahrenhit to kelvin")
    print("6.kelvin to fahrenhit")
    print("7.exit")
    #input
    option=int(input("enter the choice:"))

    if option==1:
        c=float(input("enter temperature in c:"))
        f=(c*9/5)+32
        print("fah:",f)
    elif option==2:
        f=float(input("enter temperature in f:"))
        c=(f-32)*5/9
        print("cel:",c)
    elif option==3:
        c=float(input("enter temperature in c:"))
        k=c+273.15
        print("kel:",k)
    elif option==4:
        k=float(input("enter temperature in k:"))
        c=k-273.15
        print("cel:",c)
    elif option==5:
        f=float(input("enter temperature in f:"))
        c=(f-32)*5/9+273.15
        print("kel:",k)
    elif option==6:
        k=float(input("enter temperature in f:"))
        f=(k-273.15)*9/5+32
        print("fah:",f)
    elif option==7:
        print("exit")
        break
    else:
        print("invalid")