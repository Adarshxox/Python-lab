# create a function to check  entered character is vowel or consonants

def vowels_or_conso(x):
    
    return("Vowels" if x in "AEIOUaeiou" else "Consonants")

n = input("Enter the character :")

print(vowels_or_conso(n))