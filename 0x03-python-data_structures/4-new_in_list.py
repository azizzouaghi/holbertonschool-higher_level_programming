#!/usr/bin/python3
#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx is None:
        return None
    newList = my_list[:]
    if idx >= 0 and idx < len(newList):
        newList[idx] = element
    return newList
