# Exercise 151. Concatenating files

def cat(file_name1 , file_name2):
    file1 = open(file_name1 , "r")
    file2 = open(file_name2 , "r")
    lines1 = [line.strip() for line in file1.readlines()]
    lines2 = [line.strip() for line in file2.readlines()]
    print(lines1 + lines2)
    file1.close()
    file2.close()

file_name1 = input("Input first file name: ")
file_name2 = input("Input second file name: ")
cat(file_name1 , file_name2)