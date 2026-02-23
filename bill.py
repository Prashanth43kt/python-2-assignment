#input
bill=float(input("enter the bill:"))
people=int(input("enter people:"))
tax=float(input("enter the tax:"))
tip=float(input("enter the tip:"))

#total
subtotal=bill
#tax
taxmoney=(subtotal*tax)/100
bill_after_tax=subtotal+taxmoney
#tip
tipmoney=(bill_after_tax+tip)/100
total=bill_after_tax+tipmoney
money_per_person=total/people

#display
print("subtotal:",subtotal)
print("tax:",taxmoney)
print("tip:",tipmoney)
print("total:",total)
print("person:",money_per_person)