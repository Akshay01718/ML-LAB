def union(list1,list2):
    return list(set(list1) | set(list2))

def intersection(list1,list2):
    return list(set(list1) & set(list2))

list1=list(map(int,input("Enter the elements of list 1:").split()))
list2=list(map(int,input("Enter the elements of list 2:").split()))

print("List 1:",list1)
print("List 2:",list2)
print("Union:",union(list1,list2))
print("Intersection:",intersection(list1,list2))


