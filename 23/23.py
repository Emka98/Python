list = []

while len(list) < 10:
   tmp = float(input("Enter any number: "))
   if not(tmp in list): 
        list.append(tmp)

#we can use set because it does not allow duplicate values
list = set()
while len(list) < 10:
    list.add(float(input("Enter any number: ")))