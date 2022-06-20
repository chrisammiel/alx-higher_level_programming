def uniq_add(my_list=[]):
    result = reduce(lambda x, y, : x + y, my_list)
    return result
