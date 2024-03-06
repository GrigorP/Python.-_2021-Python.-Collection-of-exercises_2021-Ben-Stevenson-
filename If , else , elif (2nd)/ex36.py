# Exercise 36. Dog age

person_age = int(input('Input person age: '))

dog_age = 0

if person_age < 0:
    print('Your number should be positive. ')
else:
    if person_age > 2:
        dog_age += 2 * 10.5
        dog_age += (person_age - 2) * 4
    else:
        dog_age += person_age * 10.5
    print(f'The {person_age} human years equals {dog_age} dog years')
    