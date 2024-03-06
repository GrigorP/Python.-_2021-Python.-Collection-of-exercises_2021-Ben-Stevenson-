# Exercise 56. Determining frequency

wave = int(input("Input here a wave frequency: "))

if wave < 3 * (10**9):
    print("Radio waves.")
elif 3 * (10**9) <= wave < 3 * (10**12):
    print("Microwave.")
elif 3 * (10**12) <= wave < 4.3 * (10**14):
    print("Infrared radiation.")
elif 4.3 * (10**14) <= wave < 7.5 * (10**14):
    print("Visible radiation.")
elif 7.5 * (10**14) <= wave < 3 * (10**17):
    print("Ultraviolet radiation.")
elif 3 * (10**17) <= wave < 3 * (10**19):
    print("X-ray radiation.")
else:
    print("Gamma radiation.")