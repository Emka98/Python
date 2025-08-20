chars = 0
while True:
    tmp = input("Enter any character if you want to end the input with x. \n")
    if tmp == "x":
        print(f"you entered {chars} characters")
        break 
    elif tmp != "":
        chars += len(tmp.split(" "))   
        
    
    







