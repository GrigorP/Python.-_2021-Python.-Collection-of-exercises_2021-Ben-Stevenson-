# Exercise 66. No cents

from math import floor

num = input("Input price (in cents): ")
nums = []

while num:
    nums += [float(num)]
    num = input("Input price(in cents : blank for close): ")

print(sum(nums))

if sum(nums) % 5 < 2.5:
    result = floor(sum(nums) % 5) 
else:
    result = round(sum(nums) % 5 , 1)

print(result)