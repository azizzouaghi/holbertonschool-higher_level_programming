#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10
if num > 5:
    print("Last digit of {:d} is {:d}".format(number, num), "and is greater than 5")
elif num == 0:
    print("Last digit of {:d} is {:d}".format(number, num), "and is 0")
elif number < 0:
    num = (-number) % 10
    num = num * -1
    print("Last digit of {:d} is {:d}".format(number, num), "and is less than 6 and not 0")
