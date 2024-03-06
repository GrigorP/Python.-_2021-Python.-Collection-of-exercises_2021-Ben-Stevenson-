# Exercise 57. Phone bill

tax = 15.44

time = int(input("Input here time of your phone conversation: "))
number_of_SMS = int(input("Input here number of SMS: "))

if time >= 50:
    time -= 50

if number_of_SMS >= 50:
    number_of_SMS -= 50

print(f"Extra time -> {time}")
print(f"Extra num of sms -> {number_of_SMS}")
if time:
    tax += time * 0.25

if number_of_SMS:
    tax += number_of_SMS * 0.15

print(f"All money -> {tax + (tax * 5 // 100)}")