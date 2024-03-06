# Exercise 149. Displaying the beginning of the file

def head(file_name):
    file = open(file_name , "r")
    lines = file.readlines()[:10]
    for line in lines:
        print(line , end = "")
    file.close()

file_name = input("Input file name: ")
head(file_name)
