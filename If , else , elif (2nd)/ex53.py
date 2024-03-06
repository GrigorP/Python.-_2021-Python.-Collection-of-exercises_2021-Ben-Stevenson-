# Exercise 53. Numerical grades - into letters

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

grade = float(input('Input grade in number: '))
reveresed_dct = dict(map(reversed , dct.items()))

if grade in dct.values():
    print(f'Grade in numbers - {grade} in letters is - {reveresed_dct.get(grade)}')
else:
    print('Something wrong :( ')