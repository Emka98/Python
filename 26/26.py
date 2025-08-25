v=[1,2,4,3,6,8,7,7,8,3,4,5,6,7,1,3,9,1,0,4,2,3,6,9]
max = []

print("It's all 3 elements sqouents:")

for i in range(len(v)):
    count = 0
    reps = 0
    for j in range(i, len(v)-1):
        if v[j] < v[j+1]: 
            count += 1
        else: 
            break
    if count >= 2:
        tmp = v[i:i+count+1]
        if len(tmp) == 3: 
            print(tmp)
        if  len(tmp) > len(max): 
            max = tmp 
   
print(f"\nIt's the longest elements sqouents: {max}\n")

for i in range(10):
    print(f"Number: {i} repeated:{v.count(i)}")