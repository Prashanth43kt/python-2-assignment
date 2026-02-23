#input
p=int(input("enter number:"))
if p<2:
    print(p,"is not prime")
elif p==2:
    print("is prime")
else:
    is_prime=True
    for i in range(2,p):
        if p%i==0:
            is_prime=False
            break
    if is_prime:
        print(p,"is prime")
    else:
        print(p,"not prime")

#part2
#input range
first=int(input("enter range:"))
end=int(input("enter range:"))
print("prime num:")

for p in range(first,end+1):
    if p<2:
        continue
    prime=True
    
    for i in range(2,p):
        if p%i==0:
            prime=False
            break
    if prime:
        print(p)