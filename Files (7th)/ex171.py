# Exercise 171: Fixed Length Strings

MAX_LINE_WIDTH = 50

def format_text(text):
    formatted_text = ""
    lines = text.splitlines()

    current_line = ""
    for line in lines:
        if line.strip() == "":
            if current_line:
                formatted_text += current_line + "\n"
                current_line = ""
            formatted_text += "\n"  # Add an extra newline for paragraph separation
        else:
            words = line.split()
            for word in words:
                if len(current_line) + len(word) <= MAX_LINE_WIDTH:
                    current_line += word + " "
                else:
                    formatted_text += current_line.strip() + "\n"
                    current_line = word + " "
            if current_line:
                formatted_text += current_line.strip() + "\n"
                current_line = ""

    if current_line:
        formatted_text += current_line.strip() + "\n"

    return formatted_text

def main():
    file_path = input("Enter the path to the file: ")

    try:
        with open(file_path, 'r') as file:
            text = file.read()

        formatted_text = format_text(text)
        print(formatted_text)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: Unable to open file '{file_path}' due to permissions.")

if __name__ == "__main__":
    main()
