# write a program to read the user input

input = "pneumonoultramicroscopiesilicovolcano"

# display the count of vowels

# display the consonant count

vowels = "aeiouAEIOU"

vowel_count = sum(1 for i in input if i in vowels)

consonant_count = sum(1 for i in input if i.isalpha() and i not in vowels)

print("Vowel count:", vowel_count)

print("Consonant count:", consonant_count)
