#  Write a function count_vowels_consonants(string) to count the vowels and consonants in a string.

def count_vowels_consonants(string):

    vo_count = 0

    co_count = 0

    for i in string:

        if i in "aeiou":

            vo_count += 1

        else:

            co_count += 1

    print(f"Vowels in string {vo_count}")

    print(f"Consenents  in string {co_count}")

count_vowels_consonants("hellopython")