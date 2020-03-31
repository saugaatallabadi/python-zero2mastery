def highest_even(li):
    even_li = []
    for item in li:
        if item % 2 == 0:
            even_li.append(item)
    return max(even_li)


print(highest_even([10, 2, 3, 4, 8, 11, 14]))
