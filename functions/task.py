#  Write a function count_vowels_consonants(string) to count the vowels and consonants in a string.

def vowcon(stri):
    
    vount = 0

    count = 0
    
    for i in stri:

        if i in "aeiou":

            vount += 1

        else:

            count += 1

    print(f"Vowels in string {vount}")

    print(f"Consenents  in string {count}")

vowcon("apple")