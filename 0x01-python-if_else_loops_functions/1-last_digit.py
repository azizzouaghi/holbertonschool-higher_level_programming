#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = number % 10
strr = 'Last digit of {:d} is {:d}'
if mod > 5:
    print(strr.format(number, mod), "and is greater than 5")
elif mod == 0:
    print(strr.format(number, mod), "and is 0")
elif number < 0:
    mod = (-number) % 10
    mod = mod * -1
    print(strr.format(number, mod), "and is less than 6 and not 0")
