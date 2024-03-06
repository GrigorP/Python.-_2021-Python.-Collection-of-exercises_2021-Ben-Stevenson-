# Exercise 20. Equation of state of an ideal gas

universal_gas_constant = 8.314  # J/(mol·K)

pressure_pa = float(input("Enter the pressure in pascals: "))
volume_liters = float(input("Enter the volume in liters: "))
temperature_celsius = float(input("Enter the temperature in Celsius: "))

temperature_kelvin = temperature_celsius + 273.15

moles_of_gas = (pressure_pa * volume_liters) / (universal_gas_constant * temperature_kelvin)

print(f"The number of moles of gas is approximately {moles_of_gas:.4f} moles.")