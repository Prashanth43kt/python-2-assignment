#input
num=int(input("enter num:"))
end=int(input("enter range(end):"))

print("\n table of",num)

for i in range(1,end+1):
    print(num,"x",i,"=",num*i)