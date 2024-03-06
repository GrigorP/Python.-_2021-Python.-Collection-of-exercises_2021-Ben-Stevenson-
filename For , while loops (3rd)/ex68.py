# Exercise 68. Average score

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

grade = input("Input here a grade (A+ - F): ")

while grade:
    if grade.capitalize() in dct:
        values = [dct[grade.capitalize()]]
    grade = input("Input here a grade (A+ - F , blank for close): ")

result = sum(values) / len(values)

print(f"{result:.2}")