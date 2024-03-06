# Exercise 150. Displaying the end of the file

def tile(file_name):
    file = open(file_name , "r")
    lines = file.readlines()[-10:]
    for line in lines:
        print(line , end = "")
    file.close()

file_name = input("Input file name: ")
tile(file_name)