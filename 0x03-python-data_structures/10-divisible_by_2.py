#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_list.copy()
    for i in my_list:
        if i % 2 == 0:
            return True
        else:
            return False
