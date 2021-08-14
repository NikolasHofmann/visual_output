from random import randint




# initialize prob_counter

def rising_increment(prob_counter, increment):
    return prob_counter*increment


probability = 1000
increment = 1.1
prob_counter = float(1)

print(type(probability))
print(type(increment))
print(type(prob_counter))

def rising_probability(probability, increment, prob_counter):
    """probability = 1000 means 1/1000 chance ### increment is how fast probability goes up, for example 1.01, 
    prob_counter is there to export the incrementet probability"""
    prob_counter = rising_increment(prob_counter, increment)
    rounded_number = round(prob_counter)
    if randint(rounded_number, probability) >= probability:
        lala = True
    else:
        lala = False
    if rounded_number < probability:
        prob_counter = rising_increment(prob_counter, increment)
    
    if lala == True:
        # in this case we do distort
        return(1, prob_counter)
    else:
        # in this case we contine with writing the next char
        return(0, prob_counter)

for i in range(1,1000):
    prob_counter = rising_probability(1000, 1.1, prob_counter)
    print(rising_probability(1000, 1.1, prob_counter))




