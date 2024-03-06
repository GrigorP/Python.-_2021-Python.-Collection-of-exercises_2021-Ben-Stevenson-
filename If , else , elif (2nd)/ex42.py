# Exercise 42. Find out the frequency by note

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88


name = input("Enter the note name as a letter and number(for example C4): ")

note = name[0]
octave = int(name[1])

if note == "C":
    freq = C4
elif note == "D":
    freq = D4
elif note == "E":
    freq = E4
elif note == "F":
    freq = F4
elif note == "G":
    freq = G4
elif note == "A":
    freq = A4
elif note == "B":
    freq = B4

freq = freq / 2 ** (4 - octave)

print(f"Note frequency {name} equal to {freq}")
