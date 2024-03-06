# Exercise 170. Missing comments

import sys

def find_uncommented_functions(file_path):
    uncommented_functions = []

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            function_name = None
            for line_num, line in enumerate(lines):
                if line.startswith('def '):
                    function_name = line.split()[1].split('(')[0]
                elif function_name and not line.strip().startswith('#') and line.strip():
                    uncommented_functions.append((function_name, file_path, line_num + 1))
                    function_name = None

    except FileNotFoundError:
        print(f"Warning: File '{file_path}' not found.")
    except PermissionError:
        print(f"Warning: Unable to open file '{file_path}' due to permissions.")

    return uncommented_functions

def main():
    if len(sys.argv) < 2:
        print("Usage: python uncommented_functions.py <file1.py> <file2.py> ...")
        sys.exit(1)

    file_paths = sys.argv[1:]

    uncommented_functions = []
    for file_path in file_paths:
        uncommented_functions.extend(find_uncommented_functions(file_path))

    if uncommented_functions:
        print("Uncommented functions:")
        for function_name, file_name, line_num in uncommented_functions:
            print(f"Function: {function_name}, File: {file_name}, Line: {line_num}")
    else:
        print("No uncommented functions found.")

if __name__ == "__main__":
    main()