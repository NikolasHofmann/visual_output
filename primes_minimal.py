import sys
from termcolor import colored, cprint
from time import sleep, strftime

def is_prime(number):
    if number == 1:
        return True
    elif number == 2:
        return True
    elif number == 3:
        return True
    else:    
        for i in range(2, number):
            if number % i == 0:
                # not a prime number
                return False
            else:
                # is prime number
                continue
        return True

def write_slowly(string):
    for char in string:
        sleep(0.000000000001)
        sys.stdout.write(char)
        sys.stdout.flush()
               


for k in range(1,1000000):
    if is_prime(k):
        text = colored(str(k) ,"red") + " "
        write_slowly(text)
    else:
        text = colored(str(k) ,"green") + " "
        write_slowly(text)

