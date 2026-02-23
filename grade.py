#input
sub1=int(input("enter the marks sub1:"))
sub2=int(input("enter the marks sub2:"))
sub3=int(input("enter the marks sub3:"))
sub4=int(input("enter the marks sub4:"))
sub5=int(input("enter the marks sub5:"))
# Display marks
print("\nMarks obtained:")
print("sub1:", sub1)
print("sub2:", sub2)
print("Sub3:", sub3)
print("Sub4:", sub4)
print("Sub5:",sub5)
# total and percentage
total= sub1 + sub2 + sub3 + sub4 + sub5
per=(total / 500) * 100

#result
if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40:
    result="pass"
else:
    result="fail"

#grade
if per>=90:
    grade="A+(outstanding)"
elif per>=80:
    grade= "A (Excellent)"
elif per>=70:
    grade= "B (Good)"
elif per>=60:
      grade="C (Average)"
elif per>=50:
      grade= "D (Pass)"
else:
     grade=" F (Fail) "
print("total Marks:", total, "/ 500")
print("per:", round(per, 2), "%")
print("Grade:", grade)
print("Result:", result)