#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        idx = my_list.index(i)
        if idx < 0:
            return none
        elif idx > len(my_list):
            return none
        else:
            print("{:d}".format(my_list[i]))
