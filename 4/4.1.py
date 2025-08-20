char = (input("Eneter one letter or intiger: "))
volvesEng = ['A', 'E', 'I', 'O', 'U', 'Y']
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 
              'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

try:
    int(char)
    print(f"You entered number {char}")
except:
    if len(list(char)) == 1:
        if char.capitalize() in volvesEng:
            print("Entered letter is volve")
        elif char.capitalize() in consonants:
            print("Entered letter is consonants")       
        else:
            print("Entered char isn`t letter or intiger")
    else:
        print("Entered more than one char")