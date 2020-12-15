#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx is None:
        return None
    newlist = my_list[:]
    if idx >= 0 and idx < len(newlist):
        newlist[idx] = element
    return newlist
