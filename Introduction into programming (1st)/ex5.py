# Exercise 5. Hand over bottles

one_and_less = 0.10
more_than_one = 0.25

less = int(input('less: '))
more = int(input('more: '))

print(f'less - ${less * one_and_less:.2f}\nmore - ${more * more_than_one:.2f}')
print(f'all - ${(less * one_and_less) + (more * more_than_one):.2f}')
