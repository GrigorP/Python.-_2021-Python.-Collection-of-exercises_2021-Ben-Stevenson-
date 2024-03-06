# Exercise 184. Aligning the list

def flatten_list(data):
    if not data:
        return []

    if isinstance(data[0], list):
        l1 = flatten_list(data[0])
        l2 = flatten_list(data[1:])
        return l1 + l2
    else:
        l1 = [data[0]]
        l2 = flatten_list(data[1:])
        return l1 + l2

# Example usage:
data = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
flattened_data = flatten_list(data)
print(flattened_data)