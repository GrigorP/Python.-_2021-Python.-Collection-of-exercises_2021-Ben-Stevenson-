# Exercise 76. Multiword palindromes

multiword = input("Input here multiword: ")

cleaned_multiword = "".join(i for i in multiword if i.isalnum())

if cleaned_multiword == cleaned_multiword[::-1]:
    print("True")
else:
    print("False")

