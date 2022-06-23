my_list = [1, 2, 3, 4, 5]
x = 2
y = 0
for i in range(x):
    try:
        print("{:d}".format(my_list[i]), end="")
        y += 1
    except IndexError:
        break
print("")

