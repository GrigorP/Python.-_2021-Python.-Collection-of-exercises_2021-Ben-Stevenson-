# Exercise 93. Centering a String

def center_string_in_window(s, w):
    if len(s) >= w:
        return s
    else:
        leading_spaces = (w - len(s)) // 2
        centered_string = ' ' * leading_spaces + s
        return centered_string

def main(your_string):
    window_widths = [20, 30, 15]

    for width in window_widths:
        print(f"\nWindow Width: {width}")
        centered_result = center_string_in_window(your_string, width)
        print(centered_result)

your_string = input("Input here string: ")

if __name__ == "__main__":
    main(your_string)