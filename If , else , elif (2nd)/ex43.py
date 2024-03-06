# Exercise 43. Find out a note by frequency

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88


freq = float(input("Enter note frequency (Hz): "))

if freq >= C4 - 1 and freq <= C4 + 1:
    note = "C4"
elif freq >= D4 - 1 and freq <= D4 + 1:
    note = "D4"
elif freq >= E4 - 1 and freq <= E4 + 1:
    note = "E4"
elif freq >= F4 - 1 and freq <= F4 + 1:
    note = "F4"
elif freq >= G4 - 1 and freq <= G4 + 1:
    note = "G4"
elif freq >= A4 - 1 and freq <= A4 + 1:
    note = "A4"
elif freq >= B4 - 1 and freq <= B4 + 1:
    note = "B4"
else:
    note = ""

if note == "":
    print("There is no note with the given frequency.")
else:
    print(f"The entered frequency approximately corresponds to the note {note}")