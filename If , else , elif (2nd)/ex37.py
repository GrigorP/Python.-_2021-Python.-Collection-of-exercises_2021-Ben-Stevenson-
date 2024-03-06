# Exercise 37. Vowels and consonants

letter = input('Input your letter: ')

if letter.lower() == 'y':
    print('This letter can be vowel and consonant. ')
elif letter.lower() in 'aeiou':
    print('Your letter is vowel.')
else:
    print('Your letter consonant. ')