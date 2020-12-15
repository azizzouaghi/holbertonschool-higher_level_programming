#!/usr/bin/python3
def no_c(str):
    NOC = ""
    for i in str:
        if i != 'C' and i != 'c':
            NOC += i
    return NOC
