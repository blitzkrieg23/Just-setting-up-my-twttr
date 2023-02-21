x = input("Enter words: ")
no_vowel = ""
for i in x:
    if i not in "aeiouAEIOU":
       no_vowel += i
print("",no_vowel)