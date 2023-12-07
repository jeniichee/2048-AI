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

    #  have an evaluation function -- how you assess intermediate states
    # almost laways never get an actual non zero utility state -- evertyhing is evalutaed using the 
    # evaluation function


    # is the evluation function im picking good -- giving right numbers/selecting right actions
    # generate a whole bunch of 

    # 1 - write eval function
    # 2- test with v limited settings --> does the result state i want exist two steps away

    # i.e. goal build 64 tile and have a state 3-5 steps away from building 64 

    def moveUp(state):
        newStateColumns = []
        moveMade = False
        #action = up
        # for every possible index
        for index in range(0,4) :
        # this just pulls out a column
            column = []
            for row in range(0,4):
                column.append(state[row][index])
            #print('starting column')
            #print(column)

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
                            moveMade = True
                           # print('intermediate column')
                          #  print(column)
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
            newStateColumns.append(column)
            #print('final column')   
            #print(column)

        col0 = newStateColumns[0]
        col1 = newStateColumns[1]
        col2 = newStateColumns[2]
        col3 = newStateColumns[3]

        newState = [list(t) for t in zip(col0, col1, col2, col3)]
        if moveMade == False:
            return 0
        else: 
         return newState
    
    def moveDown(state):
        newStateColumns = []
        moveMade = False
        # down
        # for every possible index
        for index in range(0,4) :
        # this just pulls out a column
            column = []
            for row in range(0,4):
                column.append(state[row][index])
           # print('starting column')
           # print(column)

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
                           # print('intermediate')
                          #  print(column)
                            moveMade = True
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

                  #  print('another intermediate column')
                  # print(column)

                    for i in [3,2,1]:
                        if i <= previous_tile_index:
                            column[i] = column[i-1]
                            if column[i+1] == 0:
                               # print('this happened')
                                column[i+1] = column[i]
                                column[i] = 0
                    column[0] = 0
            newStateColumns.append(column)
           # print('final column')   
           # print(column)

        col0 = newStateColumns[0]
        col1 = newStateColumns[1]
        col2 = newStateColumns[2]
        col3 = newStateColumns[3]
        newState = [list(t) for t in zip(col0, col1, col2, col3)]
        
        if moveMade == False:
            return 0
        else: 
         return newState

    
    def moveLeft(state):
        newState = []
        moveMade = False
        # action = left 
        # for every possible index
        for index in range(0,4) :
        # this just pulls out a column
            row = []
            for insidevalue in range(0,4):
                row.append(state[index][insidevalue])
           # print('starting column')
           # print(row)

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
                                # CHANGE TO T + 1?
                            row[tile_index] = 0
                            moveMade = True
                           # print('intermediate column')
                           # print(row)
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
                        #print('r 1')

                        if row[next_index - 1] == 0 :
                            row[next_index - 1] = row[next_index]
                            row[next_index] = 0 

                        #print('intermediate column')
                        #print(row)
                    row[3] = 0
            newState.append(row)
                

            #print('final column')   
            #print(row)

        if moveMade == False:
            return 0
        else: 
         return newState


    def moveRight(state):
        newState = []
        moveMade = False
        # right
        # for every possible index
        for index in range(0,4) :
            row = []
            for insidevalue in range(0,4):
                 row.append(state[index][insidevalue])
           # print('starting column')
            #print(row)

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
                            moveMade = True
                            #print('intermediate')
                            #print(row)


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

                    #print('another intermediate column')
                    #print(row)

                    for i in [3,2,1]:
                       # print(previous_tile_index)
                        if i <= previous_tile_index:
                            row[i] = row[i-1]
                            #print('updated i')
                            if row[i+1] == 0:
                                #print('this happened')
                                row[i+1] = row[i]
                                row[i] = 0
                    row[0] = 0
            newState.append(row)

            #print('final row')   
            #print(row)
        if moveMade == False:
            return 0
        else: 
         return newState

    def utility(state):
        answer = 0
        # possible actions: up, down, left, right
        upMove = solver2048.moveUp(state)
        print('up')
        print(upMove)
        downMove = solver2048.moveDown(state)
        print('downMove')
        print(downMove)
        leftMove = solver2048.moveLeft(state)
        print('left')
        print(leftMove)
        rightMove = solver2048.moveRight(state)
        print('right')
        print(rightMove)

        if upMove == 0 and downMove == 0 and leftMove == 0 and rightMove == 0:
            answer = -1
             
 
        # check if theres a win
        for row in state:
            for tile in row:
                if tile == 2048:
                    answer = 1
                    break
        print(answer)        
        return answer

    def evaluationFunction(state, action):
        """ 
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        if action == "Up":
            successorGameState = solver2048.moveUp(state)
        
        if action == "Down":
            successorGameState = solver2048.moveDown(state)
        
        if action == "Left":
            successorGameState = solver2048.moveLeft(state)
        
        if action == "Right":
            successorGameState = solver2048.moveRight(state)

        # finds current score + next score
        currentScore = 0
        for r in state:
            for i in r:
                currentScore+=i 
        
        nextScore = 0
        for r in successorGameState:
            for i in r:
                currentScore+=i 

        
        # how many squares were merged
        
        currentEmptySquares = 0
        for r in state:
            for i in r:
                if i == 0:
                    currentScore+=1
        
        nextEmptySquares = 0
        for r in successorGameState:
            for i in r:
                if i == 0:
                    currentScore+=1
        
        # num squares merged = currentEmptySquares - nextEmptySquares
        numMerged = currentEmptySquares - nextEmptySquares


        

        # newPos = successorGameState.getPacmanPosition()
        # newFood = successorGameState.getFood()
        # newGhostStates = successorGameState.getGhostStates()
        # newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        # "*** YOUR CODE HERE ***"
        
        # newFoodList = newFood.asList()

        # # consider good distance to food -- min bc you want to be close to the food
        # foodDistances = []
        # for food in newFoodList:
        #     distance = util.manhattanDistance(newPos, food)

        #     if distance > 0:
        #         foodDistances.append(distance)
    
        # minimumFood = 1
        # if not len(foodDistances) == 0:
        #     minimumFood = min(foodDistances)


        # # consider distance from ghost -- max bc you want to be far from the ghost
        # ghostDistances = [float('inf')]
        # for ghost in newGhostStates:
        #     distance = util.manhattanDistance(newPos, ghost.getPosition())
            
        #     if distance > 0:
        #         ghostDistances.append(distance)
        
        # maxGhost = max(ghostDistances)

        # return successorGameState.getScore() + 1/minimumFood + 1/maxGhost


    # def eval function
    # take in state or state action pair
    # call evaluation function when you cut off dls --> when you 

    # EVALUATION FUNCTION IS RUN ON TERMINAL STATE/WHEN DLS IS CUT OFF
    
    #def value(state):
        # win or loss
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

    #def expvalue(state):
        # minValue = float('inf')
        # 
        # # an action is placing a 2 or 4 on any empty tile







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
