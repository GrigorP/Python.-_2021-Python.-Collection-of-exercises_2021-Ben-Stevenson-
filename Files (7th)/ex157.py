# Exercise 157. Letter and number grades

def from_Let_to_num(dct: dict , grade: str):
    grades = []
    while grade:
        grades.append(grade)
        grade = input("Input grade(F - A+): ")
    sum_of_grades = 0
    for i in range(len(grades)):
        if grades[i].capitalize() in dct:
            sum_of_grades += dct[grades[i].capitalize()]
        else:
            print("Something wrong.")
    return sum_of_grades

def from_Num_to_let(dct: dict , grade: str):
    reveresed_dct = dict(map(reversed , dct.items()))
    grades = []
    while grade:
        grades.append(float(grade))
        grade = input("Input grade(0 - 4.0): ")
    let_grades = []
    for i in grades:
        if i != 4.0:
            if i in reveresed_dct:
                let_grades.append(reveresed_dct[i])
            else:
                print("Something wrong.")
        else:
            let_grades += ["A" , "A+"]
    return let_grades



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

grade = input("Input grade (0 - 4.0 or F - A+): ")

if grade[0].isalpha():
    if len(grade) == 2:
        if grade[1] == "+" or grade[1] == "-":
            print(from_Let_to_num(dct , grade))
        else:
            print("Wrong symbol")
    else:
        print(from_Let_to_num(dct , grade))
elif str(int(grade)).isdigit():
    print(from_Num_to_let(dct , grade))
