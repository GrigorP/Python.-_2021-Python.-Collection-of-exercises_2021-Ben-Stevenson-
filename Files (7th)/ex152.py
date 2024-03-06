# Exercise 152. Numbering lines in a file

file_name = input("Input file name: ")
with open(file_name, "r") as file:
    lines = file.readlines()
    new_file = open("for_ex2.txt" , "a")
    for i in range(1 , len(lines)):
        new_file.write(f"{i , lines[i].strip()}")
file.close()
new_file.close()