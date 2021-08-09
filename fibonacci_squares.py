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

    index_square_tiles = []
    
    def project_up():
        x_values = []
        for tile in tiles:
            x_values.append(tile[0])
        y_values = []
        for tile in tiles:
            y_values.append(tile[1])

        # need top left and top right tile

        left_top_tile = (min(x_values), min(y_values))
        right_top_tile = (max(x_values), min(y_values))

        #the top line of tiles
        top_line = []
        for i in range(left_top_tile[0], right_top_tile[0]+1):
            top_line.append((i, max(y_values)))

        fibo = fib(index)

        # get the tiles of the square at index
        index_square_tiles = []
        for i in range(left_top_tile[0], right_top_tile[0]+1):
            for j in range(max(y_values) + 1, fibo+1):
                index_square_tiles.append((i ,j))
        return index_square_tiles

    def project_right():
        x_values = []
        for tile in tiles:
            x_values.append(tile[0])
        y_values = []
        for tile in tiles:
            y_values.append(tile[1])

        #need me some bottom right and top right tile

        right_top_tile = (max(x_values), min(y_values))
        right_bot_tile = (max(x_values), max(y_values))

        #the right line of tiles
        right_line = []
        for i in range(right_top_tile[1], right_bot_tile[1]+1):
            right_line.append((max(x_values), i))

        fibo = fib(index)

        # get the tiles of the square at index
        index_square_tiles = []

        #use len(right_line)+1 instead maybe
        for i in range(right_top_tile[1], right_bot_tile[1]+1):
            for j in range(max(x_values) + 1, fibo+1):
                index_square_tiles.append((j ,i))
        return index_square_tiles


        ## faulty ##
    

    #### !!! New version of index_square_titles.append() maybe better ####
    def project_left():
        x_values = []
        for tile in tiles:
            x_values.append(tile[0])
        y_values = []
        for tile in tiles:
            y_values.append(tile[1])

        #need me some bottom left and top left tile

        left_top_tile = (min(x_values), min(y_values))
        left_bot_tile = (min(x_values), max(y_values))

        #the left line of tiles
        left_line = []
        for i in range(left_top_tile[1], left_bot_tile[1]+1):
            left_line.append((min(x_values), i))

        fibo = fib(index)

        # get the tiles of the square at index
        index_square_tiles = []

        for j in range(1, fibo+1):
            for i in (left_line):
                index_square_tiles.append((i[0]-j, i[1]))

        return index_square_tiles

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
    elif get_move_directions(index) == "up":
        index_square_tiles = project_up()
    elif get_move_directions(index) == "right":
        index_square_tiles = project_right()
    elif get_move_directions(index) == "left":
        index_square_tiles = project_left()
        #print index_square_tiles
        #> **

    added_tiles = []
    for given_tiles in tiles:
        added_tiles.append(given_tiles)
    for index_tile in index_square_tiles:
        added_tiles.append(index_tile)
    return added_tiles
                

rectangle_3 = [(0,0),(1,0), (0,-1), (0,-2), (1,-1),(1,-2)]
            
#rectangle_4 = [(0,0), (1,0), (0,-1), (0,-2), (1,-1), (1,-2), (-1,0), (-2,0), (-3,0), (-1,-1), (-2,-1), (-3,-1), (-1,-2), (-2,-2), (-3,-3)]
rectangle_4 = get_next_square(rectangle_3, 4)
rectangle_5 = get_next_square(rectangle_4, 5)
rectangle_6 = get_next_square(rectangle_5, 6)


print("Rectangle 4: ")
print(rectangle_4)
print("\n"*2)
print("Rectangle 5: ")
print(rectangle_5)
print("\n"*2)
print("Rectangle 6: ")
print(rectangle_6)
print("\n"*2)



#rectangle 1 = [0, 0]

#rectangle 2 = [(0,0),(1,0)]

#rectangle 3 = [(0,0),(1,0), (0,-1), (0,-2), (1,-1),(1,-2)]

#rectangle 4 = [(0, 0), (1, 0), (0, -1), (0, -2), (1, -1), (1, -2), (-1, -2), (-1, -1), (-1, 0), (-2, -2), (-2, -1), (-2, 0), (-3, -2), (-3, -1), (-3, 0)]

#rectangle 5 = [(0, 0), (1, 0), (0, -1), (0, -2), (1, -1), (1, -2), (-1, -2), (-1, -1), (-1, 0), (-2, -2), (-2, -1), (-2, 0), (-3, -2), (-3, -1), (-3, 0), (-3, 1), (-3, 2), (-3, 3), (-3, 4), (-3, 5), (-2, 1), (-2, 2), (-2, 3), (-2, 4), (-2, 5), (-1, 1), (-1, 2), (-1, 3), (-1, 4), (-1, 5), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]

#rectangle 6 = [(0, 0), (1, 0), (0, -1), (0, -2), (1, -1), (1, -2), (-1, -2), (-1, -1), (-1, 0), (-2, -2), (-2, -1), (-2, 0), (-3, -2), (-3, -1), (-3, 0), (-3, 1), (-3, 2), (-3, 3), (-3, 4), (-3, 5), (-2, 1), (-2, 2), (-2, 3), (-2, 4), (-2, 5), (-1, 1), (-1, 2), (-1, 3), (-1, 4), (-1, 5), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, -2), (3, -2), (4, -2), (5, -2), (6, -2), (7, -2), (8, -2), (2, -1), (3, -1), (4, -1), (5, -1), (6, -1), (7, -1), (8, -1), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]




# rectangle should be a list of touples (coordinates) starting point(0,0)

# index 2 = right ; index 3 = up ; index 4 = left index 5 = down





# rectangle 4 expected !!FAULTY!! = [(0, 0), (1, 0), (0, -1), (0, -2), (1, -1), (1, -2), (-1, 0), (-2, 0), (-3, 0) (-1, -1) (-2, -1) (-3, -1) (-1, -2) (-2, -2)]
# rectangle 4 actual !! RIGHT I THINK !!   = [(0, 0), (1, 0), (0, -1), (0, -2), (1, -1), (1, -2), (-1, -2), (-1, -1), (-1, 0), (-2, -2), (-2, -1), (-2, 0), (-3, -2), (-3, -1), (-3, 0)]

#                      










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
