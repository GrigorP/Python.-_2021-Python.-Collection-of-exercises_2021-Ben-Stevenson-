# Exercise 54. Performance appraisal

dct = {
    0.0: 'low level',
    0.4: 'satisfactory level',
    0.6: 'high level'
}

rating = float(input('Input pls the rating of employee: '))

if rating in dct.keys():
    print(f'Increase in employee salary - ${rating * 2400}.')
else:
    print('Something wrong :(. ')