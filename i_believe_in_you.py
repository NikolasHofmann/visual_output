####################### I believe in you! #######################

import sys
from time import sleep

message = input("Tell me something, and I will repeat it back to you: ")
print("\n\n\n\n\n\n")

for i in range(1, 1000):
    for char in message:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()


    


