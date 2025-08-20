import os
  
webaddresses=[]
line = input('Enter web address like "www.python.org" or press ENTER to stop: ')
while line != '':
    webaddresses.append(line)
    line = input('Enter web address like "www.python.org" or press ENTER to stop: ')
    
print(webaddresses)
dirname = os.getcwd()
filename = input("Enter the file name (without directory): ")
filepath = os.path.join(dirname,filename)
file = open(filepath,'w+')
for webaddress in webaddresses:
    file.write(webaddress+"\n")
file.close()

filename =input('Enter filename with web addresses to read: ')
while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename =input('Enter filename to read: ')
webaddresses=[]
with open(filename,'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n",''))
for line in webaddresses:
    if line.endswith('.pl'):
        print(line,'is a polish web page')
    else:
        print(line, 'is not a polish web page')


filename =input('Enter filename with web addresses to read: ')
while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename =input('Enter filename to read: ')
webaddresses=[]
with open(filename,'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n",''))
dirname = os.path.dirname(filename)
websPathPL = os.path.join(dirname,'webs_pl.txt')
websPathOther = os.path.join(dirname,'webs_other.txt')
filePL = open(websPathPL,'w')
fileOther = open(websPathOther,'w')
for line in webaddresses:
    if line.endswith('.pl'):
        filePL.write(line+"\n")
    else:
        fileOther.write(line+"\n")
filePL.close()
fileOther.close()
