#List = [1,2,4,1,5,6]
#Swap the List means Last Element will be First and First Element Will be Last
# [6,2,4,1,5,1]


list  = [1,2,4,1,5,6]

size = len(list)

temp = list[0]
list[0] = list[size-1]
list[size-1] = temp

print(list)
