my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = 0
new_my_list = []
end = len(my_list)
while x in range(end):
    if my_list[x] >= 0:
        if my_list[x] > 0:
            print(my_list[x])
        x += 1
    else:
        break
