####################### I believe in you! #######################
from random import randint
import sys
from time import sleep
from termcolor import colored


import string
import random


alphabet = list(string.ascii_lowercase)
symbols = list(string.punctuation)
sign_number = list(string.punctuation) + ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def make_random_letter():
    letter = alphabet[random.randint(0, 25)]
    return letter

def make_random_sign():
    sign = symbols[random.randint(0, 31)]
    return str(sign)

def make_random_sign_number():
    sign = sign_number[random.randint(0, 41)]
    return str(sign)


def make_random_sign_numbers_string(length):
    length = int(length)
    sign_string_list = []
    for i in range(0, length):
        sign_string_list.append(make_random_sign_number())
    sign_string = ""
    for sign in sign_string_list:
        sign_string += str(sign)
    return str(sign_string)
    

    

# It does what it should... prduce random string mixed of letters and sings/numberss
def produce_random_text(leng):
    for j in range(1,leng):
        name_length = random.randint(1,leng)
        name = []
        while len(name) <= name_length:
            sym_quantity = random.randint(1, round(leng/3))
            sym_count = 0
            while sym_count <= sym_quantity and len(name) <= name_length:
                dice = random.randint(1, 11)
                if dice in range(1, sym_quantity + 1):
                    name.append(make_random_sign())
                    sym_count += 1
                else:
                    name.append(make_random_letter())
            if len(name) <= 8:
                name.append(make_random_letter())    
        name_str = ""
        for letter in name:
            name_str += letter
        return(str(name_str))


prob_counter = float(1)

def rising_probability(prob_counter, probability, increment):
    """probability = 1000 means 1/1000 chance ### increment is how fast probability goes up, for example 1.01, 
    prob_counter is there to export the incrementet probability"""
    prob_counter = float(1)
    rounded_number = round(prob_counter)
    if randint(rounded_number, probability) >= probability:
        lala = True
    else:
        lala = False
    if rounded_number < probability:
        prob_counter = prob_counter*increment
    
    if lala == True:
        # in this case we do distort
        return(1, prob_counter)
    else:
        # in this case we contine with writing the next char
        return(0, prob_counter)




message = input("Tell me something, and I shall repeat it back to you: ")
print("\n\n\n\n\n\n")

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

sign_string_length = float(1)
output_speed = float(0.1)
# do it very often
for i in range(1, 1000000):
    for char in message:
        #start distorting after x iterations
        if i >= 10:
            result = rising_probability(prob_counter, probability=10, increment=1.01)
            if result[0] == 0:
            #in this case we dont distort
                prob_counter = result[1]
            else:
            #distort
                #random_text = str(produce_random_text(randint(1, round(len(message)/2))))
                random_text = make_random_sign_numbers_string(randint(1, round(sign_string_length)))
                sign_string_length = sign_string_length*1.01
                #now do the same slow flush out for the random text
                #print(random_text, end="")
                for char2 in random_text:
                    output_speed = output_speed
                    sleep(output_speed)
                    colored_char2 = ('\033[32m' + '\033[2m' + char2)
                    sys.stdout.write(colored_char2)
                    sys.stdout.flush()
                prob_counter = result[1]
        
        #flushing out the message char by char
        sleep(output_speed)
        output_speed = output_speed*0.999
        colored_char = ('\033[0m' + '\033[31m' + '\033[1m' + char) 
        sys.stdout.write(colored_char)
        sys.stdout.flush()

# stutter einbauen
# message output in other color
# distortion length increment slowdown
# make colored red more shiny
# make red characters bigger with time
# transition to another message in a different color?
# two messages between the green at the same time?
# printing message vertically and huge by coloring the green symbols differently 

### BUILD FLEXIBLE APPLICATION WITH ALL THESE FUNCTIONALITIES ###


# red alternative=








# print (fg.BLUE, style.BRIGHT , "Show me your color" , style.RESET_ALL) 

# class fg:
#     BLACK   = '\033[30m'
#     RED     = '\033[31m'
#     GREEN   = '\033[32m'
#     YELLOW  = '\033[33m'
#     BLUE    = '\033[34m'
#     MAGENTA = '\033[35m'
#     CYAN    = '\033[36m'
#     WHITE   = '\033[37m'
#     RESET   = '\033[39m'

# class bg:
#     BLACK   = '\033[40m'
#     RED     = '\033[41m'
#     GREEN   = '\033[42m'
#     YELLOW  = '\033[43m'
#     BLUE    = '\033[44m'
#     MAGENTA = '\033[45m'
#     CYAN    = '\033[46m'
#     WHITE   = '\033[47m'
#     RESET   = '\033[49m'

# class style:
#     BRIGHT    = '\033[1m'
#     DIM       = '\033[2m'
#     NORMAL    = '\033[22m'
#     RESET_ALL = '\033[0m'



# def distort(speed):
#     if speed == "slow":
#         print("distort")
        #low, slowly incrementing chance:
        #   low starting leng = 1
        #   rounded_leng = int(rounded(leng))
        #   produce_random_text(rounded_leng)
        #   leng = _leng*1.001
    


