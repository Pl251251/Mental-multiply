import random
import time


def multiply(x, y):
    a = random.randint(x, y)
    b = random.randint(x, y)
    c = a * b
    prod = input(str(a) + " x " + str(b) + "=   ")
    if c == int(prod):
        print("correct")
    else:
        print("YOU FAILURE")
def time1(y,z):
    start = time.time()
    for x in range(10):
        multiply(y, z)
    end = time.time()
    total_time = end - start
    print("\n" + str(total_time))

while (1 == 1):
    choose = input("pick level 1-6:  ")
    if int(choose) == 1:
        time1(1, 9)
    elif int(choose) == 2:
        time1(10, 99)
    elif int(choose) == 3:
        time1(100, 999)
    elif int(choose) == 4:
        time1(1000, 9999)
    elif int(choose) == 5:
        time1(10000, 99999)
    elif int(choose) == 6:
        time1(100000,999999)
