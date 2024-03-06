# Exercise 108. Translating measures

def convert_to_minimal_measurements(units, unit_type):
    # Define conversion ratios
    tablespoons_per_glass = 16
    teaspoons_per_tablespoon = 3

    # Convert to teaspoons
    if unit_type == "glass":
        teaspoons = units * tablespoons_per_glass * teaspoons_per_tablespoon
    elif unit_type == "tablespoon":
        teaspoons = units * teaspoons_per_tablespoon
    elif unit_type == "teaspoon":
        teaspoons = units
    else:
        return "Invalid unit type"

    # Calculate the number of cups, tablespoons, and teaspoons
    cups = teaspoons // (teaspoons_per_tablespoon * tablespoons_per_glass)
    remaining_teaspoons = teaspoons % (teaspoons_per_tablespoon * tablespoons_per_glass)
    tablespoons = remaining_teaspoons // teaspoons_per_tablespoon
    remaining_teaspoons %= teaspoons_per_tablespoon

    # Build the result string
    result_string = ""
    if cups > 0:
        result_string += f"{cups} cup{'s' if cups > 1 else ''}, "
    if tablespoons > 0:
        result_string += f"{tablespoons} tablespoon{'s' if tablespoons > 1 else ''}, "
    if remaining_teaspoons > 0:
        result_string += f"{remaining_teaspoons} teaspoon{'s' if remaining_teaspoons > 1 else ''}"

    return result_string.strip(", ")

volume = int(input("Input here volume: "))
unit_type = input("Input here unit_type(glass , tablespoon , teaspoon): ")
result = convert_to_minimal_measurements(volume, unit_type)
print(result)