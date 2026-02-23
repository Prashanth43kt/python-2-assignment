n=int(input("number:"))
sum=0
#input
n1=int(input("enter the num1:"))
sum=sum+n1
max=n1
min=n1
#take other number
for i in range(2,n+1):
    n1=int(input())
    sum=sum+n1
    if n1>max:
        max=n1
    if n1<min:
        min=n1
avg=sum/n
print("tot:",sum)
print("avg:",avg)
print("min:",min)
print("max:",max)
