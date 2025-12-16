
p=float(input("enter principal amount : "))
t=float(input("enter time : "))
r=float(input("rate of intrest : "))
a = p * (1 + r/100) ** t
ci = a - p
print("result of compound intrest is : ",ci)
print("principal amount : ",a)

