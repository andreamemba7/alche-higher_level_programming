#!/usr/bin/python3
def uppercase(str):
    for char in str:
        old_ord = ord(char)
        if old_ord > 89 and old_ord < 123:
            new_ord = old_ord - 32
            new_char = chr(new_ord)
            print("{}".format(new_char), end="")
        else:
            print("{}".format(char), end="")
    return
