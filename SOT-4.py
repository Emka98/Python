vowels = "aeiouyóą"
digits = "0123456789"
Consonants = "qwrtdfghjklzxcvn"

character = input("Enter any character: ")

if len(character) != 1:
    print("more than one character entered: ")
elif character in vowels:
    print("It's vowels")
elif character in digits:
    print("It's digits")
elif character in consonants:
    print("It's consonants")
else:
    print("It's consonants a other character")

