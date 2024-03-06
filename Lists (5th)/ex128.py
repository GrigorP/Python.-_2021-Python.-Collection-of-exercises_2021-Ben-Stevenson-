# Exercise 128. Count elements in a list

def countRange(lst: list , min_num: int , max_num: int):
    nums = []
    for i in lst:
        if min_num <= i < max_num:
            nums.append(i)
    for i in nums:
        print(i , "-" , nums.count(i))

min_num = int(input("Input minimum number: "))
max_num = int(input("Input maximum number: "))

num = input("Input number: ")
lst = []

while num:
    lst.append(int(num))
    num = input("Input number (blank for close): ")

countRange(lst , min_num , max_num)