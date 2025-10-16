s=int(input("Enter the starting number:"))
e=int(input("Enter the ending number:"))

odd=0
even=0

for i in range(s,e+1):
    if i%2==0:
        even+=i
    else:
        odd+=i
print("Odd sum:",odd)
print("Even sum:",even)
