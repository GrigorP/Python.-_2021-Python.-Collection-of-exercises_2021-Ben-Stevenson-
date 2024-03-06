# Exercise 158. Deleting comments

def deleting_comms(filename1 , filename2):
    file1 = open(filename1 , "r")
    file2 = open(filename2 , "a")
    lines = file1.readlines()
    for line in lines:
        if "#" in line:
            if line[:line.index("#")] != "":
                file2.write(line[:line.index("#")])
                file2.write("\n")

filename1 = input("Input file name: ")
filename2 = input("Input file name: ")

deleting_comms(filename1 , filename2)