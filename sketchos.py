"""
lala = {1: "Simon", 7: "tobias", 3: "vanessa", 1: "julian"}

print(str(lala))

print(set(lala))

print(lala)

# # # 6-11 # # #

cities = {
    "barcelona": {
        "country": "spain",
        "population": "1620000",
        "fact": "a very cool city!"
    },
    "stuttgart": {
        "country": "germany",
        "populaton": "634830",
        "fact": "they have a football team"
    },
    "paris": {
        "country": "france",
        "population": "2161000",
        "fact": "great croissants!"
    }
}

print("\n\n\n")

for key, value in cities.items():
    print("City name: " + key.title()+"\n")
    for info, answer in value.items():
        print("\t" + info.title() + ": " + answer.title())
    
    print("\n\n")

# # # 6-12 # # #
"""
####################### I believe in you! #######################
from random import randint
import sys
from time import sleep


import string
import random


alphabet = list(string.ascii_lowercase)
symbols = list(string.punctuation)

def make_random_letter():
    letter = alphabet[random.randint(0, 25)]
    return letter

def make_random_sign():
    sign = symbols[random.randint(0, 25)]
    return sign


# It does what it should...
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


message = input("Tell me something, and I shall repeat it back to you: ")
print("\n\n\n\n\n\n")


prob_counter = float(1)

def rising_probability(probability, increment, prob_counter):
    """probability = 1000 means 1/1000 chance ### increment is how fast probability goes up, for example 1.01, 
    prob_counter is there to export the incrementet probability"""
    prob_counter = float(1)
    rounded_number = rounded(prob_counter)
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


    

def distort(speed):
    if speed == "slow":
        print("distort")
        #low, slowly incrementing chance:
        #   low starting leng = 1
        #   rounded_leng = int(rounded(leng))
        #   produce_random_text(rounded_leng)
        #   leng = _leng*1.001


output_speed = float(0.1)
# do it very often
for i in range(1, 100):
    for char in message:
        if i >= 50:
            distort(speed)
    
    sleep(output_speed)
    output_speed = output_speed*0.99
    sys.stdout.write(char)
    sys.stdout.flush()


    


