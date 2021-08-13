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

import sys
from time import sleep

message = input("Tell me something, and I will repeat it back to you: ")
print("\n\n\n\n\n\n")

for i in range(1, 1000):
    for char in message:
        sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()


    


