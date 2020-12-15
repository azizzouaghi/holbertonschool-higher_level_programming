#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx is None:
        return None
    i = my_list[:]
    if idx >= 0 and idx < len(i):
        i[idx] = element
        return i
