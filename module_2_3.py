my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_len = len(my_list)
# print(list_len)
a = 0
ind = a
while ind + 1 <= list_len:
    if my_list[ind] > 0:
        print(my_list[ind])
        ind = ind + 1
        if my_list[ind] == 0:
            ind = ind + 1
        continue
    else:
        break
