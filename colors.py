l1=set()
l2=set()
n1=int(input("enter the number of color in list1:"))
print("enter the color to list:")
for x in range(n1):
    color=input()
    l1.add(color)
n2=int(input("enter the number of color in list2:"))
print("enter the color to list:")
for x in range(n2):
    color=input()
    l2.add(color)
diff=l1.difference(l2)
print("colorin list1 not in list2",diff)
