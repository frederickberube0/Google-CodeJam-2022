def calc(list_of_dices):
    lst = sorted(list_of_dices)

    cur_min = 0
    len_of_straight = 0
    for i in range(len(lst)):
        if lst[i] >= cur_min:
            cur_min = lst[i]
            len_of_straight += 1
    return len_of_straight

print(calc([6,10,12,8]))
print(calc([5,4,5,4,4,4]))
print(calc([10,10,7,6,7,4,4,5,7,4]))
