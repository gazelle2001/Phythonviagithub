# Count Number of even and Odd Elements[18,22,25,11,3,17,18,28,77,67,78,11,9,77,12,88]

numbers=[18,22,25,11,3,17,18,28,77,67,78,11,9,77,12,88]
evenNo=[]
oddNo=[]
for i in numbers:
    if i%2==0:
        evenNo.append(i)
    else:
        oddNo.append(i)
print("the even numbers are"+str(evenNo))
print("the odd numbers are"+str(oddNo))