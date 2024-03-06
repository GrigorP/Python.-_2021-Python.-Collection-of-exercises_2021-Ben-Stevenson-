# Exercise 169. Editing text in a file

def load_function_words(file_path):
    with open(file_path, 'r') as file:
        function_words = [word.strip() for word in file.readlines()]
    return function_words

def replace_function_words(original_text, function_words):
    edited_text = original_text
    for word in function_words:
        edited_text = edited_text.replace(word, '*' * len(word))
    return edited_text

def main():
    # Get file paths from the user
    original_file = input("Enter the path to the original text file: ")
    function_words_file = input("Enter the path to the file containing function words: ")
    new_file = input("Enter the path for the new edited file: ")

    # Load function words
    function_words = load_function_words(function_words_file)

    # Read original text
    with open(original_file, 'r') as file:
        original_text = file.read()

    # Replace function words with asterisks
    edited_text = replace_function_words(original_text, function_words)

    # Save edited text to a new file
    with open(new_file, 'w') as file:
        file.write(edited_text)

    print("Edited file saved successfully.")

if __name__ == "__main__":
    main()