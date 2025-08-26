v1= {1,3,5,7,9}
v2= {1,4,7,11,15}
v3= {1,2,3,4,5,6,7,8,9,20}

print(f"The common part of the sets: v1 and v2 -> {v1 & v2}")
print(f"The difference of the set v3 and the sum of the sets v1+v2 -> {v3 - (v1 | v2)}")
print(f"the sum of all sets v1, v2, and v3 -> {v1 | v2 |v3}")

# way 2 
print("\nWay 2:\n")

print(f"The common part of the sets: v1 and v2 -> {v1.intersection(v2)}")
print(f"The difference of the set v3 and the sum of the sets v1+v2 -> {v3.difference(v1.union(v2))}")
print(f"the sum of all sets v1, v2, and v3 -> {v1.union(v2).union(v3)}")






