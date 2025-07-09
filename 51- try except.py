#ZADANIE 1

  
line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
file = open(filepath,'w+')
file.write(line)
file.close()

#ZADANIE 2

  
line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    file.close()
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')

#ZADANIE 3

  
line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    file.close()
except FileNotFoundError as e:
    print('Error opening file',filepath,e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')


#ZADANIE 4

  
line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    value = int(line)
    file.close()
    print('The value saved in file is',value)
except FileNotFoundError as e:
    print('Error opening file',filepath,e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')

#ZADANIE 5

  
line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    file.close()
    value = int(line)
    print('The value saved in file is',value)
except FileNotFoundError as e:
    print('Error opening file',filepath,e)
except ValueError as e:
    print('The value entered cannot be converted to a number',line,e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')
else:
    print('Actions completed successfully')


