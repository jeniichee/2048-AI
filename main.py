from view import View

class solver2048():
    #tic tac toe representation: list of three tuples w 3 posns

    # number = there is a number there
    # 0 = empty
    # tuples represent rows, with the first tuple being the first row left to right
    #[[0,2,2,2],  
    # [0,0,0,0],
    # [4,2,4,2],
    # [8,0,0,0]]

    # if win, utility = 1
    # if loss, utility = -1

    def utility(state):
        answer = None
        # possible actions: up, down, left, right
        movepossible = False

        #action = up
        # for every possible index
        for index in range(0,4) :
        # this just pulls out a column
            column = []
            for row in range(0,4):
                column.append(state[row][index])
            print('starting column')
            print(column)

            # moves everything up
            #this pulls out every tile in the column (index)
            for tile_index in range(0,4):
                # the tile
                tile = column[tile_index]
        
                # tile is an actual number
                if tile != 0 :
                    # this pulls out all the tiles above the tile
                    # first entry of column = top tiles
                    for t in range (0,tile_index):
                        # if the tile is a 0 then tile can move up
                        if column[t] == 0:
                            column[t] = tile
                                # CHANGE TO T + 1!!!!!
                            column[tile_index] = 0
                            print('intermediate column')
                            print(column)
                            break

            #this pulls out every tile in the column (index)
            for tile_index in range(0,3): 
                tile = column[tile_index]

                next_tile_index = 1 + tile_index
                # Check if the next tile is within the column and has the same value
                if tile != 0 and tile == column[next_tile_index]:
                    # combines values
                    new_value = tile + column[next_tile_index]
                    # updates top tile to have new combined value
                    column[tile_index] = new_value
                    column[next_tile_index] == 0
                    #
                    for next_index in range(next_tile_index, 3):
                        column[next_index] = column[next_index+1]
                        if column[next_index - 1] == 0 :
                            column[next_index - 1] = column[next_index]
                            column[next_index] = 0 
                    column[3] = 0
            print('final column')   
            print(column)

        # down
        # for every possible index
        for index in range(0,4) :
        # this just pulls out a column
            column = []
            for row in range(0,4):
                column.append(state[row][index])
            print('starting column')
            print(column)

            # moves everything down
            #this pulls out every tile in the column (index)
            for tile_index in [3,2,1,0]:
                # the tile
                tile = column[tile_index]
                # tile is an actual number
                if tile != 0 :
                    # this pulls out all the tiles below the tile
                    # first entry of column = top tiles
                    # TILE INDEX + 1
                    for below_tiles in range (3, tile_index, -1):

                        # if the tile is a 0 then tile can move up
                        if column[below_tiles] == 0:
                            column[below_tiles] = tile
                            column[tile_index] = 0
                            print('intermediate')
                            print(column)
                            break

            # this pulls out every tile in the column (index)
            for tile_index in [3, 2, 1]:
                tile = column[tile_index]
                # gets tile below the tile
                previous_tile_index = tile_index - 1
                # Check if the next tile is within the column and has the same value
                if tile != 0 and tile == column[previous_tile_index]:
                    # combines values
                    new_value = tile + column[previous_tile_index]
                    # updates top tile to have new combined value
                    column[tile_index] = new_value
                    column[previous_tile_index] = 0

                    print('another intermediate column')
                    print(column)

                    for i in [3,2,1]:
                        print(previous_tile_index)
                        if i <= previous_tile_index:
                            column[i] = column[i-1]
                            print('updated i')
                            if column[i+1] == 0:
                                print('this happened')
                                column[i+1] = column[i]
                                column[i] = 0
                    column[0] = 0
            print('final column')   
            print(column)

        # action = left 
        # for every possible index
        for index in range(0,4) :
        # this just pulls out a column
            row = []
            for insidevalue in range(0,4):
                row.append(state[index][insidevalue])
            print('starting column')
            print(row)

            # moves everything up
            #this pulls out every tile in the column (index)
            for tile_index in range(0,4):
                # the tile
                tile = row[tile_index]
        
                # tile is an actual number
                if tile != 0 :
                    # this pulls out all the tiles above the tile
                    # first entry of column = top tiles
                    for t in range (0,tile_index):
                        # if the tile is a 0 then tile can move up
                        if row[t] == 0:
                            row[t] = tile
                                # CHANGE TO T + 1!!!!!
                            row[tile_index] = 0
                            print('intermediate column')
                            print(row)
                            break

            #this pulls out every tile in the column (index)
            for tile_index in range(0,3): 
                tile = row[tile_index]

                next_tile_index = 1 + tile_index
                # Check if the next tile is within the column and has the same value
                if tile != 0 and tile == row[next_tile_index]:
                    # combines values
                    new_value = tile + row[next_tile_index]
                    # updates top tile to have new combined value
                    row[tile_index] = new_value
                    #
                    for next_index in range(next_tile_index, 3):
                        row[next_index] = row[next_index+1]
                        row[next_tile_index] == 0
                        print('r 1')

                        if row[next_index - 1] == 0 :
                            print('r2')
                            row[next_index - 1] = row[next_index]
                            row[next_index] = 0 

                    
                        print('intermediate column')
                        print(row)
                    row[3] = 0
                

            print('final column')   
            print(row)
                
        # right
        # for every possible index
        for index in range(0,4) :
            row = []
            for insidevalue in range(0,4):
                 row.append(state[index][insidevalue])
            print('starting column')
            print(row)

            # moves everything up
            #this pulls out every tile in the column (index)
            for tile_index in [3,2,1,0]:
                # the tile
                tile = row[tile_index]
                # tile is an actual number
                if tile != 0 :
                    # this pulls out all the tiles below the tile
                    # first entry of column = top tiles
                    # TILE INDEX + 1
                    for below_tiles in range (tile_index + 1, 4):
                        # if the tile is a 0 then tile can move up
                        if row[below_tiles] == 0:
                            row[below_tiles] = tile
                            row[below_tiles - 1] = 0
                            print('intermediate')
                            print(row)


            # this pulls out every tile in the column (index)
            for tile_index in [3, 2, 1]:
                tile = row[tile_index]
                # gets tile below the tile
                previous_tile_index = tile_index - 1
                # Check if the next tile is within the column and has the same value
                if tile != 0 and tile == row[previous_tile_index]:
                    # combines values
                    new_value = tile + row[previous_tile_index]
                    # updates top tile to have new combined value
                    row[tile_index] = new_value
                    row[previous_tile_index] = 0

                    print('another intermediate column')
                    print(row)

                    for i in [3,2,1]:
                        print(previous_tile_index)
                        if i <= previous_tile_index:
                            row[i] = row[i-1]
                            print('updated i')
                            if row[i+1] == 0:
                                print('this happened')
                                row[i+1] = row[i]
                                row[i] = 0
                    row[0] = 0
            print('final row')   
            print(row)

    
            ## TO DO: update state with new columns
            # state = [index][value][player]
            new_state = []
 
        # check if theres a win
        for row in state:
            for tile in row:
                if tile == 2048:
                    answer = 1
                    break
        return answer
    
    #def value(state):
        # if solver2048.utility(state) == -1 or solver2048.utility(state) == 1:
        #     return solver2048.utility(state)
        # if state[3] == "X":  
        #     return solver2048.maxValue(state)
        # if state[3] == "O":
        #     return solver2048.minValue(state)
    
    #def maxValue(state):
        # maxValue = float('-inf')
        # # an action is changing an n to an x
        # for i in range(0,3):
        #     for j in range(0,3):
        #         if state[i][j] == "n":
        #             newState = [list(row) for row in state]
        #             newState[i][j] = "X"
        #             newState = (tuple(newState[0]), tuple(newState[1]), tuple(newState[2]), "O")

        #             currentValue = ticTacToeSolver.value(newState)

        #             if currentValue > maxValue:
        #                 maxValue = currentValue

        #return maxValue

    #def minValue(state):
        # minValue = float('inf')
        # # an action is changing an n to an O
        # for i in range(0,3):
        #     for j in range(0,3):
        #         if state[i][j] == "n":
        #             newState = [list(row) for row in state]
        #             newState[i][j] = "O"
        #             newState = (tuple(newState[0]), tuple(newState[1]), tuple(newState[2]), "X")

        #             currentValue = ticTacToeSolver.value(newState)

        #             if currentValue < minValue:
        #                 minValue = currentValue
        # return minValue
