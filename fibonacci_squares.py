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



def get_sizes(fib_index):
    """We need to get the position and the size for every fib index as a list"""
    fib_sizes = []
    for fib in get_fibs(fib_index):
        fib_sizes.append((fib*10,fib*10))
    return fib_sizes

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

    

def get_next_square(tiles, index):

    #def project: if directions = down: project_down(self) etc

    
    
    def project_down():
        #find left and right bottom tile
        x_values = []
        for tile in tiles:
            x_values.append(tile[0])
        y_values = []
        for tile in tiles:
            y_values.append(tile[1])

        left_bot_tile = (min(x_values), max(y_values))
        right_bot_tile = (max(x_values), max(y_values))

        #the bottom line of tiles
        bottom_line = []
        for i in range(left_bot_tile[0], right_bot_tile[0]+1):
            bottom_line.append((i, max(y_values)))

        fibo = fib(index)

        # get the tiles of the square at index
        index_square_tiles = []
        for i in range(left_bot_tile[0], right_bot_tile[0]+1):
            for j in range(max(y_values) + 1, fibo+1):
                index_square_tiles.append((i ,j))
        return index_square_tiles
    
    if get_move_directions(index) == "down":
        index_square_tiles = project_down()
        #print index_square_tiles
        #> **

    added_tiles = []
    for given_tiles in tiles:
        added_tiles.append(given_tiles)
    for index_tile in index_square_tiles:
        added_tiles.append(index_tile)
    return added_tiles
                


rectangle_4 = [(0,0), (1,0), (0,-1), (0,-2), (1,-1), (1,-2), (-1,0), (-2,0), (-3,0), (-1,-1), (-2,-1), (-3,-1), (-1,-2), (-2,-2), (-3,-3)]

rectangle_5 = get_next_square(rectangle_4, 5)

print(rectangle_5)

# [0, 0]

# [(0,0),(1,0)]

# [(0,0),(1,0), (0,-1), (0,-2), (1,-1),(1,-2)]

# [(0,0),(1,0), (0,-1), (0,-2), (1,-1),(1,-2), (-1,0), (-2,0), (-3,0) (-1,-1) (-2,-1) (-3,-1) (-1,-2) (-2,-2) (-3,-3)]

# [(0,0), (1,0), (0,-1), (0,-2), (1,-1), (1,-2), (-1,0), (-2,0), (-3,0), (-1,-1), (-2,-1), (-3,-1), (-1,-2), (-2,-2), (-3,-3), 
# (-3,1), (-3,2), (-3,3), (-3,4), (-3,5), (-2,1), (-2,2), (-2,3), (-2,4), (-2,5), (-1,1), (-1,2), (-1,3), (-1,4), (-1,5), 
# (0,1), (0,2), (0,3), (0,4), (0,5), (1,1), (1,2), (1,3), (1,4), (1,5)]

#rectangle_4_tiles = [(0,0),(1,0), (0,-1), (0,-2), (1,-1),(1,-2), (-1,0), (-2,0), (-3,0), (-1,-1), (-2,-1), (-3,-1), (-1,-2), (-2,-2), (-3,-3)]

#rectangle_5_tiles = [(0,0), (1,0), (0,-1), (0,-2), (1,-1), (1,-2), (-1,0), (-2,0), (-3,0), (-1,-1), (-2,-1), (-3,-1), (-1,-2), (-2,-2), (-3,-3), 
#(-3,1), (-3,2), (-3,3), (-3,4), (-3,5), (-2,1), (-2,2), (-2,3), (-2,4), (-2,5), (-1,1), (-1,2), (-1,3), (-1,4), (-1,5), (0,1), (0,2), (0,3), (0,4), (0,5), (1,1), (1,2), (1,3), (1,4), (1,5)]



# rectangle should be a list of touples (coordinates) starting point(0,0)

# index 2 = right ; index 3 = up ; index 4 = left index 5 = down










# now works for rectangle 5

#    
#exptected
                                                                                                                                                                                          
#[(0, 0), (1, 0), (0, -1), (0, -2), (1, -1), (1, -2), (-1, 0), (-2, 0), (-3 ,0), (-1 ,-1), (-2 ,-1), (-3, -1), (-1, -2), (-2, -2), (-3, -3), (-3, 1), (-3, 2), (-3, 3), (-3, 4), (-3, 5), (-2, 1), (-2, 2), (-2, 3), (-2, 4), (-2, 5), (-1, 1), (-1, 2), (-1, 3), (-1, 4), (-1, 5), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]
                                                                                                                                                                                
                                                                                                                                                                                 
#actual
#[(0, 0), (1, 0), (0, -1), (0, -2), (1, -1), (1, -2), (-1, 0), (-2, 0), (-3, 0), (-1, -1), (-2, -1), (-3, -1), (-1, -2), (-2, -2), (-3, -3), (-3, 1), (-3, 2), (-3, 3), (-3, 4), (-3, 5), (-2, 1), (-2, 2), (-2, 3), (-2, 4), (-2, 5), (-1, 1), (-1, 2), (-1, 3), (-1, 4), (-1, 5), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]





#[(0, 0), (1, 0), (0, -1), (0, -2), (1, -1), (1, -2), (-1, 0), (-2, 0), (-3, 0), (-1, -1), (-2, -1), (-3, -1), (-1, -2), (-2, -2), (-3, -3), (-3, 1), (-3, 2), (-3, 3), (-3, 4), (-3, 5), (-2, 1), (-2, 2), (-2, 3), (-2, 4), (-2, 5), (-1, 1), (-1, 2), (-1, 3), (-1, 4), (-1, 5), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
                                                                                                                                                                                                                                                                                                                            # x not far enougb by 1...





                                                                                                                                                                                #y value goes not far enough

##[(0, 0), (1, 0), (0, -1), (0, -2), (1, -1), (1, -2), (-1, 0), (-2, 0), (-3, 0), (-1, -1), (-2, -1), (-3, -1), (-1, -2), (-2, -2), (-3, -3), (-3, 1), (-3, 2), (-3, 3), (-3, 4),          (-2, 1), (-2, 2), (-2, 3), (-2, 4),          (-1, 1), (-1, 2), (-1, 3), (-1, 4),          (0, 1), (0, 2), (0, 3), (0, 4)]






#fixed#
#actual
#[(0, 0), (1, 0), (0, -1), (0, -2), (1, -1), (1, -2), (-1, 0), (-2, 0), (-3, 0), (-1, -1), (-2, -1), (-3, -1), (-1, -2), (-2, -2), (-3, -3), (-3, 1), (-3, 2), (-3, 3), (-3, 4), (-3, 5), (-3, 6), (-3, 7), (-2, 1), (-2, 2), (-2, 3), (-2, 4), (-2, 5), (-2, 6), (-2, 7), (-1, 1), (-1, 2), (-1, 3), (-1, 4), (-1, 5), (-1, 6), (-1, 7), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]

#index_square_tiles **  is wrong
#                                                                                                                                           [(-3, 1), (-3, 2), (-3, 3), (-3, 4), (-3, 5), (-3, 6), (-3, 7), (-2, 1), (-2, 2), (-2, 3), (-2, 4), (-2, 5), (-2, 6), (-2, 7), (-1, 1), (-1, 2), (-1, 3), (-1, 4), (-1, 5), (-1, 6), (-1, 7), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]

                                                                                                                                                                                            # the y axis of index_square_tiles counts 2 values too far
#get_fibs is counting too far







                



        


    





"""
            # position_change
            if direction == "right":
                #we go to the right bottom corner
                position_change = (fib(index + 1) - fib(index) ,-fib(index))
            if direction == "up":
                #we go to the top right corner
                position_change = (-fib(index),-fib(index + 1) + fib(index))
            if direction == "left":
                #we go to the top left corner
                position_change = (0, 0)
            if direction == "down":
                #we go to the left bottom corner
                position_change = (0, fib(index - 1) + fib(index))
"""
    
    
    
"""
def get_positions(index):
    #get a list of the positions of the top right corner for every rect
    positions = [start_position, (810, 800), (800, 820)]
    if index > 3:
        for i in range(4, index):
            positions.append(positions[i - 1] + get_movement(index))
    return positions

"""



####### dont forget to set the starting rects ###########




    







#done = False
#while not done:
#    number = input()
#    if number == "quit":
#        done = True
#    else:
#        print(give_fib(number))
