# Exercise 124. Line of Best Fit

def calculate_line_of_best_fit(points):
    n = len(points)
    sum_x = sum(point[0] for point in points)
    sum_y = sum(point[1] for point in points)
    sum_xy = sum(point[0] * point[1] for point in points)
    sum_x_squared = sum(point[0] ** 2 for point in points)

    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    b = (sum_y - m * sum_x) / n

    return m, b

def main():
    points = []
    while True:
        x_input = input("Enter the x coordinate (blank to quit): ")
        if x_input == "":
            break
        y_input = input("Enter the y coordinate: ")
        try:
            x = float(x_input)
            y = float(y_input)
            points.append((x, y))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if len(points) < 2:
        print("At least two points are required.")
        return

    m, b = calculate_line_of_best_fit(points)
    print(f"The line of best fit is: y = {m:.2f}x + {b:.2f}")

if __name__ == "__main__":
    main()