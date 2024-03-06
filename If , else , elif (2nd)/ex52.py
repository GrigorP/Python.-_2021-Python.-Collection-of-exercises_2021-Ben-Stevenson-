# Exercise 52. Letter grades to numeric grades

dct = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0,
}

grade = input('Input grad in letter: ')

if grade.capitalize() in dct:
    print(f'This grade in letter - {grade} in numbers is - {dct[grade.capitalize()]}')
else:
    print('Something wrong :( ')