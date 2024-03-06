# Exercise 61. Valid license plate number?

car_plate_numbers = input("Input here your car plate numbers(111AAA - 9999ZZZ): ")

if len(car_plate_numbers) == 7:
    numbers = car_plate_numbers[:4]
    if numbers.isdigit():
        print(f"Your license plates belong to the new format.")
    else:
        print("First 3-4 characters must be integers(numbers).")
elif len(car_plate_numbers) == 6:
    numbers = car_plate_numbers[:3]
    if numbers.isdigit():
        print(f"Your license plates belong to the old format.")
    else:
        print("First 3-4 characters must be integers(numbers).")
else:
    print("Your car license plate must contain 6-7 characters.")