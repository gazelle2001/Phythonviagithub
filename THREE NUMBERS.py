#write a python program to find smallest number among three.

a=int(input("enter the value for a:"))
b=int(input("enter the value for b:"))
c=int(input("enter the value for c:"))
if a <= b and a <=c:
    print ("a is smallest")
elif b <=a and b<=c:
    print("b is smallest")
elif c <=a and c<=b:
    print ("c is smallest")