#!/usr/bin/python3
def new_in_list(list, idx, element):
    if idx is None:
        return None
    myList = list[:]
    if idx >= 0 and idx < len(myList):
        myList[idx] = element
    return myList
