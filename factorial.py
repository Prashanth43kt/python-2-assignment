#input
p=int(input("number:"))
#negative no
if p<0:
    print("invalid not defined:")
elif p==0:
    print("0!==1")
    #n!=n*(n-1)*(n-2)
else:
    fact=1
    print("\n calculation:")
    for i in range(p,0,-1):
        fact=fact*i
        if i>1:
           print(i,"x",end="")
        else:
            print(i,"=",fact)
