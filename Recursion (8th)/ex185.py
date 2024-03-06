# Exercise 185. Decoding based on run lengths

def decoding(lst):
    if len(lst) == 0:
        return []
    else:
        count_of_symbol = 0
        decoded_lst = [lst[0]]
        symbol = lst[0]
        while symbol == lst[0]:
            count_of_symbol += 1
            lst = lst[1:]
            if len(lst) == 0:
                break
        decoded_lst.append(count_of_symbol)
        return decoded_lst + decoding(lst)

lst = ["A" , "A" , "A" , "B" , "B" , "C" , "C" , "A" , "A"]
print(decoding(lst))