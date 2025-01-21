i =0
list = []
while i < 3:
    a =int(input("Enter positive integer number "))
    if a >0:
        list.append(a)
        i += 1
    else:
        print("Number shoud be positive")
        
maxnumber = max(list)
list.sort()
list.pop()  

for i in range(0,maxnumber):
    print(sum(list))



    
    
    
    
    
    
    
    

        
