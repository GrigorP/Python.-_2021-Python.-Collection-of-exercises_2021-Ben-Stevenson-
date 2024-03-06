# Exercise 134. All sublists of a given list

def all_sublists(lst):
    sublists = [[]]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublists.append(lst[i:j])
    return sublists

source_lists = [[1, 2, 3], [4, 5], [6], []]

for lst in source_lists:
    print("Source list:", lst)
    print("Sublists:", all_sublists(lst))
    print()