# Exercise 161. What is the chemical element?

def read_element_data(file_path):
    elements = {}

    with open(file_path, 'r') as file:
        for line in file:
            symbol, name, protons = line.strip().split(',')
            elements[symbol] = {'name': name, 'protons': int(protons)}

    return elements

def main():
    file_path = 'chemical_elements.txt'  
    elements = read_element_data(file_path)

    while True:
        user_input = input("Enter an element symbol, element name, or number of protons (leave blank to exit): ").strip()
        if not user_input:
            break

        if user_input.isdigit():
            protons = int(user_input)
            for symbol, data in elements.items():
                if data['protons'] == protons:
                    print(f"Element designation: {symbol}, Name: {data['name']}")
                    break
            else:
                print("No element found with the entered number of protons.")
        else:
            if user_input in elements:
                print(f"Number of protons for {user_input}: {elements[user_input]['protons']}")
            else:
                for symbol, data in elements.items():
                    if data['name'].lower() == user_input.lower():
                        print(f"Number of protons for {user_input}: {data['protons']}")
                        break
                else:
                    print("No element found with the entered symbol or name.")

if __name__ == "__main__":
    main()