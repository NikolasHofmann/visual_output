import pygame
from random import randint

def get_fibs(fib_index):
    """outputs the fibonacci at position """
    if fib_index == 1:
        return [1]
    if fib_index == 2:
        return [1]
    if fib_index == 3:
        return [2]
    else:
        fib_numbers = [1, 1, 2]
        fib_index = int(fib_index)
        if fib_index > 2:
            done = False
            while not done:
                if len(fib_numbers) < fib_index:
                    fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
                else:
                    done = True
        return fib_numbers


def fib(index):
    fib_list = get_fibs(index)
    return fib_list[-1]


# print(get_sizes(5)) returns [(10, 10), (10, 10), (20, 20), (30, 30), (50, 50), (80, 80)]




def get_move_directions(index):
    """get move directions for every index"""
    if index % 4 == 1: 
        return "down"
    elif index % 4 == 2:
        return "right"
    elif index % 4 == 3:
        return "up"
    elif index % 4 == 0:
        return "left"
        

# for index in fibonacci

def transposition_left_to_next_left(index):
    if get_move_directions(index) == "down":
        #print("transposing by: ", end="")
        #print((0, fib(index-1)))
        transposition = (0, fib(index-1))


    elif get_move_directions(index) == "right":
        #print("transposing by: ", end="")
        #print((fib(index-1), -fib(index-2)))
        transposition = (fib(index-1), -fib(index-2))


    elif get_move_directions(index) == "up":
        #print("transposing by: ", end="")
        #print((-fib(index-2), -fib(index)))
        transposition = (-fib(index-2), -fib(index))
        


    elif get_move_directions(index) == "left":
        #print("transposing by: ", end="")
        #print((-(fib(index-1)+fib(index-2)), 0))
        transposition = (-(fib(index-1)+fib(index-2)), 0)
        #print("transposition = ", end="")
        #print(transposition)


    return transposition

def get_top_left(index):
    if index == 1:
        return (0, 0)
    elif index == 2:
        return (1, 0)
    elif index == 3:
        return (0, -2)
    else:
        i = 4
        final_left = (0, -2)
        x = final_left[0]
        y = final_left[1]
        while index >= i:
            x += transposition_left_to_next_left(i)[0]
            y += transposition_left_to_next_left(i)[1]
            i += 1
    return (x, y)



def make_square(index):
    square = []
    for i in range(0 ,fib(index)):
        for j in range(0,fib(index)):
            square.append((get_top_left(index)[0] + i,get_top_left(index)[1] + j))
    return square




def make_rect(index, screen):
    left = get_top_left(index)[0] + screen[0]/2
    right = get_top_left(index)[1] + screen[1]/2
    width = fib(index)
    heigth = width
    
    rectangle = pygame.Rect(left, right, width, heigth)
    return rectangle


def make_rects_random(index, screen, x, y):
    left = get_top_left(index)[0] + screen[0]-x
    right = get_top_left(index)[1] + screen[1]-y
    width = fib(index)
    heigth = width
    
    rectangle = pygame.Rect(left, right, width, heigth)
    return rectangle






        