a = {1,2,3,4,5}
b = {5,6,7,8,9,3,2}
print("a= ",a)
print("b= ",b)
a.add(88)
b.update([78,90])
print("After adding elements a: ",a)
print("After updating sets b: ",b)
a.remove(88)
b.discard(78)
print("After removing 88 from a: ",a)
print("After discarding 78 from b: ",b)

print("Union of a and b: ",a.union(b))
print("Intersection of a and b: ",a.intersection(b))
print("a-b : ",a-b)