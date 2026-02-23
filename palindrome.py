val=input("enter number:")
length=len(val)
rev=""
for i in range(length -1,-1,-1):
    rev=rev+val[i]
print("original:",val)
print("rev:",rev)

if val==rev:
    print("res:is palindrome")
else:
    print("not a palindrome")