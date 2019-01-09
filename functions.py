food = ["Adobo", "Sinigang", "Tocino", "Galinggong", 3, 100, 2, 9.22]

str_items =[]
num_items = []

for i in food:
    if isinstance(i, float) or isinstance(i, int):
        num_items.append(i)
    elif isinstance(i, str):
        str_items.append(i)
    else:
        pass

print(str_items)
print(num_items)

def parse_lists(some_list):
    str_list_items = []
    num_list_items = []
    # new list
    for i in food:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items.append(i)
        else:
            pass

    return num_list_items, str_list_items #back

print(parse_lists(food))

utang = [123123, 123123123,123123123, "Jose", "Rizal"]
sum([123, 323, 423])

def my_sum(my_utang_list):
    total = 0
    for i in my_utang_list:
        if isinstance(i, float) or isinstance(i, int):
            total += i
    return total

sum(utang)

