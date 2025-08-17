#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = 0
    for i in range(0, len(my_list)):
        if my_list[i] > max_value:
            max_value = my_list[i]
        elif my_list is None:
            return None
        else:
            max_value = max_value
    return max_value
