#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        a = my_list[idx]
        mylist.remove(a)
        b = my_list
        return b
