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

chance = 1
p = 100
k = float(1)
# do it very often
for i in range(1, 100000000000000):
    for char in message:
        if i >= 50:
            if randint(1, p) == chance: 
                random_text = produce_random_text(p)
                for char2 in random_text:
                    sleep(k)
                    sys.stdout.write(char2)
                    sys.stdout.flush()
                    k = k*1/2
            if p > 2:
                p -= 1

        sleep(k)
        sys.stdout.write(char)
        sys.stdout.flush()
        k = k*1/2


    


