# Exercise 63. Average value

num = int(input("Input number: "))
nums = []

if num != 0:
    while num:
        nums += [num]
        num = int(input("Input number (0 for close): "))
    print(f"The average value of your entered numbers - {sum(nums) // len(nums)}")
else:
    print("First number must be > 0.")