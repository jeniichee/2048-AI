import unittest;
import random;
import copy;

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
        score = 0 
        # action = up
        # for every possible index

        for index in range(0,4) :
        # this just pulls out a column
            column = []
            for row in range(0,4):
                column.append(state[row][index])

            # moves everything up
            # this pulls out every tile in the column (index)
            for tile_index in range(0,4):
                # the tile
                tile = column[tile_index]
    
                # tile is an actual number
                if not  column[tile_index] == 0 :
  
                    # this pulls out all the tiles above the tile
                    # first entry of column = top tiles
                    for t in range (0,tile_index):
                        # if the tile is a 0 then tile can move up
                        if column[t] == 0:
                            column[t] = tile
                                # CHANGE TO T + 1!!!!!
                            column[tile_index] = 0
                            moveMade = True
                            break

            # this pulls out every tile in the column (index)
            for tile_index in range(0,3): 
                tile = column[tile_index]

                next_tile_index = 1 + tile_index
                # Check if the next tile is within the column and has the same value
                if tile != 0 and tile == column[next_tile_index]:
                    # combines values
                    new_value = tile + column[next_tile_index]
                    score += new_value
                    moveMade = True
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
      

        col0 = newStateColumns[0]
        col1 = newStateColumns[1]
        col2 = newStateColumns[2]
        col3 = newStateColumns[3]

        newState = [list(t) for t in zip(col0, col1, col2, col3)]
        if moveMade == False:
            return 0
        else: 
         return newState, score
    
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
                            moveMade = True
                            column[below_tiles] = tile
                            column[tile_index] = 0

                            break

            # this pulls out every tile in the column (index)
            for tile_index in [3, 2, 1]:
                tile = column[tile_index]
                # gets tile below the tile
                previous_tile_index = tile_index - 1
                # Check if the next tile is within the column and has the same value
                if tile != 0 and tile == column[previous_tile_index]:
                    moveMade = True
                    # combines values
                    new_value = tile + column[previous_tile_index]
                    score += new_value
                    # updates top tile to have new combined value
                    column[tile_index] = new_value
                    column[previous_tile_index] = 0

                    for i in [3,2,1]:
                        if i <= previous_tile_index:
                            column[i] = column[i-1]
                            if column[i+1] == 0:
                                column[i+1] = column[i]
                                column[i] = 0
                    column[0] = 0
            newStateColumns.append(column)

        col0 = newStateColumns[0]
        col1 = newStateColumns[1]
        col2 = newStateColumns[2]
        col3 = newStateColumns[3]
        newState = [list(t) for t in zip(col0, col1, col2, col3)]
        
        if moveMade == False:
            return 0
        else: 
         return newState, score
    
    def moveLeft(state):
        newState = []
        moveMade = False
        score = 0 
        # action = left 
        # for every possible index
        for index in range(0,4) :
        # this just pulls out a column
            row = []
            for insidevalue in range(0,4):
                row.append(state[index][insidevalue])


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
                            break

            #this pulls out every tile in the column (index)
            for tile_index in range(0,3): 
                tile = row[tile_index]

                next_tile_index = 1 + tile_index
                # Check if the next tile is within the column and has the same value
                if tile != 0 and tile == row[next_tile_index]:
                    # combines values
                    moveMade = True
                    new_value = tile + row[next_tile_index]
                    score += new_value
                    # updates top tile to have new combined value
                    row[tile_index] = new_value
                    #
                    for next_index in range(next_tile_index, 3):
                        row[next_index] = row[next_index+1]
                        row[next_tile_index] == 0

                        if row[next_index - 1] == 0 :
                            row[next_index - 1] = row[next_index]
                            row[next_index] = 0 
                    row[3] = 0
            newState.append(row)
                

        if moveMade == False:
            return 0
        else: 
         return newState, score

    def moveRight(state):
        newState = []
        moveMade = False
        score = 0 
        # right
        # for every possible index
        for index in range(0,4) :
            row = []
            for insidevalue in range(0,4):
                 row.append(state[index][insidevalue])


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

            # this pulls out every tile in the column (index)
            for tile_index in [3, 2, 1]:
                tile = row[tile_index]
                # gets tile below the tile
                previous_tile_index = tile_index - 1
                # Check if the next tile is within the column and has the same value
                if tile != 0 and tile == row[previous_tile_index]:
                    # combines values
                    moveMade = True
                    new_value = tile + row[previous_tile_index]
                    score += new_value
                    # updates top tile to have new combined value
                    row[tile_index] = new_value
                    row[previous_tile_index] = 0



                    for i in [3,2,1]:
                        if i <= previous_tile_index:
                            row[i] = row[i-1]
                            if row[i+1] == 0:
                                row[i+1] = row[i]
                                row[i] = 0
                    row[0] = 0
            newState.append(row)

        if moveMade == False:
            return 0
        else: 
         return newState, score

    def utility(state):
        answer = 0
        # possible actions: up, down, left, right
        upMove = solver2048.moveUp(state)

        downMove = solver2048.moveDown(state)

        leftMove = solver2048.moveLeft(state)

        rightMove = solver2048.moveRight(state)

        if upMove == 0 and downMove == 0 and leftMove == 0 and rightMove == 0:
            answer = -1
              
        # check if theres a win
        for row in state:
            for tile in row:
                if tile == 2048:
                    answer = 1
                    break
        return answer
    
    #%%
    def getSuccessor(state, action):
        if action == "Up":
            return solver2048.moveUp(state)[0]
        
        if action == "Down":
            return solver2048.moveDown(state)[0]
        
        if action == "Left":
            return solver2048.moveLeft(state)[0]
        
        if action == "Right":
            return solver2048.moveRight(state)[0]
        
    def evaluationFunction(state, action):
        if action == None:
            # return score
            total_sum = sum(max(row) for row in state)
            return total_sum
        
        actions = ["Up", "Down", "Left", "Right"]

        successorGameState = solver2048.getSuccessor(state, action)[0]
        
        if successorGameState == 0:
            return -1
        else:
        # finds current score + next score
            # prioritize increasing the score
            currentScore = 0
            for r in state:
                for i in r:
                    currentScore+=i 
            
            nextScore = 0
            for r in successorGameState:
                for i in r:
                    nextScore+=i
            
            increase = nextScore - currentScore
            
            # prioritize how many squares were merged
            currentEmptySquares = 0
            for r in state:
                for i in r:
                    if i == 0:
                        currentEmptySquares+=1
            
            
            nextEmptySquares = 0
            for r in successorGameState:
                for i in r:
                    if i == 0:
                        nextEmptySquares+=1
            
            
            # num squares merged = currentEmptySquares - nextEmptySquares
            numMerged = nextEmptySquares - currentEmptySquares

            # prio move that merges largest tile
            prio_merge = 0

            maxval = max(max(row) for row in state)
            maxsuccessor = max(max(row) for row in successorGameState)
            # to merge largest tile then that means the value must have doubled
            if maxsuccessor == maxval*2:
                prio_merge = 1

            
            #prio having empty space around largest tile
            maxindex_r = 0
            maxindex_c = 0

            max_val = max(max(row) for row in successorGameState)
            
            for row in range(0,4):
                for col in range(0,4):
                    if successorGameState[row][col] == max_val:
                        maxindex_r = row
                        maxindex_c = col
                        
            abovetile = 0
            belowtile = 0
            lefttile = 0
            righttile = 0

            prio_empty = 0

            print(successorGameState)
            if maxindex_r > 0:
                abovetile = successorGameState[maxindex_r-1][maxindex_c]
                if abovetile == 0:
                    print('above')
                    prio_empty += 1

            if maxindex_r < 3:
                belowtile = successorGameState[maxindex_r+1][maxindex_c]
                if belowtile == 0:
                    print('below')
                    prio_empty +=1 

            if maxindex_c > 0:
                lefttile = successorGameState[maxindex_r][maxindex_c-1]
                if lefttile == 0:
                    print('left')
                    prio_empty +=1

            if maxindex_c < 3:  
                righttile = successorGameState[maxindex_r][maxindex_c+1]
                if righttile == 0:
                    print('right')
                    prio_empty +=1

            print('num empty:')
            print(prio_empty)
            
            return increase + numMerged + prio_merge + prio_empty

    def value(state, depth, player):
        # win or loss
        if solver2048.utility(state) == -1 or solver2048.utility(state) == 1 or depth == 0:
            # EVALUATION FUNCTION SHOULD ALSO TAKE IN action
            return solver2048.evaluationFunction(state, None)

        # person playing the game is 0
        if player == 0:  
            return solver2048.maxValue(state, depth)
        
        # randomly generated tile is 1
        if player == 1:
            # take 
            return solver2048.expvalue(state, depth)

    
    def maxValue(state, depth):
        actions = ["Up", "Down", "Left", "Right"]

        maxValue = float('-inf')
        maxAction = None

        for action in actions:
            successorGameState = solver2048.getSuccessor(state, action)[0]
        
            if successorGameState != 0:
                currentValue = solver2048.value(successorGameState, depth, 1)[0]
                # print('current val for max:')
                # print(currentValue)
                
                if currentValue > maxValue:
                    # print('reached')
                    maxValue = currentValue
                    maxAction = action

        # print('return of max:')
        # print((maxValue,maxAction))
    
        return (maxValue, maxAction)

    def expvalue(state, depth):
        # takes in a state with 5 blank cells
        # for all 5 cells, consider all 10 possible next states
        value = 0
        expAction = None

        # generate tile
        # empty cells
        emptycount = 0
        emptyindices = []
        for r in range(0,4):
            for c in range(0,4):
                tile = state[r][c]
                if tile == 0:
                    emptycount +=1
                    emptyindices.append([r,c])

        # all empty cells
        value = 0
        for emptycells in range (0, emptycount):
            # action: placing a 2 or 4
            for randomtile in [2,4]:
                if randomtile == 2:
                    pr = .9
                else:
                    pr = .1

                x, y = emptyindices[emptycells]
                nextstate = copy.deepcopy(state)
                nextstate[x][y] = randomtile

                result = solver2048.value(nextstate, depth-1, 0)
                if isinstance(result, tuple):
                # If it's a tuple, extract the first element
                    currentValue = result[0]
                else:
                # If it's not a tuple, it's already the desired value
                    currentValue = result
                value += pr*currentValue
                expAction = randomtile
        return (value, expAction)

    def generateTile(state):
        # 90% 2 and 10% 4
        return_state = copy.deepcopy(state)
        new_value = random.choices([2,4], weights=[0.9, 0.1])[0]
        
        tiles_needed = 1
        while tiles_needed > 0:
            row = random.randint(0, 3)
            column = random.randint(0, 3)
            
            if return_state[row][column] == 0:
                return_state[row][column] = new_value
                tiles_needed -= 1 
        return return_state
    
    def startState():
        board = [[0,0,0,0], 
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

        new_value = random.choices([2,4], weights=[0.9, 0.1])[0]

        tiles_needed = 2 
        while tiles_needed > 0:
            row = random.randint(0, 3)
            column = random.randint(0, 3)

            if board[row][column] == 0:
                board[row][column] = new_value
                tiles_needed -= 1 
        return board 
    
    def printBoard(state):
        for i in range(4):
            for j in range(4):
                print("%2d  " % state[i][j], end="")
            print("")
        print("")
    
        
    def play(): 
        initialState = solver2048.startState()
        solver2048.printBoard(initialState)
        View.draw(initialState, 0)
        
        depth = 3  
        player = 0  
        score = 0 
        
        while True:
            _, action = solver2048.value(initialState, depth, player)
            nextState, new_score = solver2048.getSuccessor(initialState, action)
            successor = solver2048.generateTile(nextState)
            solver2048.printBoard(successor)
            
            if (solver2048.utility(nextState) == -1):
                break
            score += new_score
            initialState = successor
            View.draw(initialState, score)
            

#%%
            

class Test2048(unittest.TestCase):

    def test_value_function(self):
        #optimal policy --> moving left, down, then left/right should from 64 tile assuming 
        #no interference from randomly generated tile
        initial_state = [
        [8, 8, 4, 32],
        [8, 8, 4, 2],
        [2, 0, 4, 2],
        [4, 4, 4, 8]
    ]
        #state = solver2048.moveLeft(state)
        # forms
        [
        [16, 4, 32, 0],
        [16, 4, 2, 0],
        [2, 4, 2, 0],
        [8, 4, 8, 0]
    ]
        #state = solver2048.moveDown(state)
        # forms
        [
        [0, 0, 0, 0],
        [32, 0, 32, 0],
        [2, 8, 4, 0],
        [8, 8, 8, 0]
    ]
        # move l or r to get 64
        #state = solver2048.moveDown(state)

        # Assuming player value and depth are valid
        depth = 3

        # Make three moves using the value function
        answer = solver2048.value(initial_state, depth, 0)

        # loop throough everything and see if 64 exists

        print(answer)
        

    # def test_empty(self):
    #     board1 = [
    #         [8,8,8,8],
    #         [8,8,8,8],
    #         [8,8,8,8],
    #         [8,0,8,8]
    #     ]

    #     result1 = [[8,8,8,8],
    #         [8,8,8,8],
    #         [8,8,8,8],
    #         [8,2,8,8]]
        
    #     result2 = [[8,8,8,8],
    #         [8,8,8,8],
    #         [8,8,8,8],
    #         [8,4,8,8]]
        
    #     emptymethod = solver2048.generateTile(board1)
    #     print(emptymethod)

    #     r1 = emptymethod == result1
    #     r2 = emptymethod == result2
        

    #     self.assertEqual(True, r1 or r2)

    # def test_up_0(self):
    #     board = [
    #         [0,0,0,0],
    #         [0,0,0,0],
    #         [0,0,0,0],
    #         [0,0,0,0]
    #     ]
    #     self.assertEqual(solver2048.moveUp(board), 0)

    # def test_up_1(self):
    #     board1 = [
    #         [0,0,0,0],
    #         [0,0,0,0],
    #         [0,0,0,0],
    #         [2,0,0,0]
    #     ]
    #     self.assertEqual(solver2048.moveUp(board1), 
    #                      [
    #         [2,0,0,0],
    #         [0,0,0,0],
    #         [0,0,0,0],
    #         [0,0,0,0]
    #     ])


    # def test_up_2(self):
    #     board2 = [
    #         [0,0,0,0],
    #         [0,0,0,0],
    #         [2,0,0,0],
    #         [2,0,0,0]
    #     ]
    #     self.assertEqual(solver2048.moveUp(board2), 
    #                      [
    #         [4,0,0,0],
    #         [0,0,0,0],
    #         [0,0,0,0],
    #         [0,0,0,0]
    #     ])

    # def test_up_3(self):
    #     board3 = [
    #         [0,0,0,0],
    #         [2,0,0,0],
    #         [4,0,0,0],
    #         [2,0,0,0]
    #     ]
    #     self.assertEqual(solver2048.moveUp(board3), 
    #                      [
    #         [2,0,0,0],
    #         [4,0,0,0],
    #         [2,0,0,0],
    #         [0,0,0,0]
    #     ])
    
    # def test_up_4(self):
    #     board4 = [
    #         [8,0,0,0],
    #         [4,0,0,0],
    #         [8,0,0,0],
    #         [2,0,0,0]
    #     ]
    #     self.assertEqual(solver2048.moveUp(board4), 
    #                      0 )
    
    # def test_up_5(self):
    #     board4 = [
    #         [8,8,8,8],
    #         [4,4,4,4],
    #         [8,8,8,8],
    #         [2,2,2,2]
    #     ]
    #     self.assertEqual(solver2048.moveUp(board4), 
    #                      0 )
    


    # def test_down_0(self):
    #     board = [
    # [2, 0, 2, 0],
    # [0, 2, 0, 2],
    # [4, 2, 2, 4],
    # [0, 4, 0, 4]
    #     ]
    #     self.assertEqual(solver2048.moveDown(board), 
    #                      [
    # [0, 0, 0, 0],
    # [0, 0, 0, 0],
    # [2, 4, 0, 2],
    # [4, 4, 4, 8]
    #                      ] )
    
        
    # def test_down_1(self):
    #     board4 = [
    #         [8,8,8,8],
    #         [4,4,4,4],
    #         [8,8,8,8],
    #         [2,2,2,2]
    #     ]
    #     self.assertEqual(solver2048.moveUp(board4), 
    #                      0 )
        
    # def test_down_2(self):
    #     board = [
    # [2, 4, 2, 2],
    # [0, 0, 4, 2],
    # [4, 0, 2, 4],
    # [0, 4, 0, 4]
    #     ]
    #     self.assertEqual(solver2048.moveDown(board), 
    #                      [
    # [0, 0, 0, 0],
    # [0, 0, 2, 0],
    # [2, 0, 4, 4],
    # [4, 8, 2, 8]
    #                      ] )
        
    # def test_down_3(self):
    #     board = [
    # [0, 0, 0, 0],
    # [0, 0, 0, 2],
    # [4, 0, 0, 0],
    # [0, 4, 0, 0]
    #     ]
    #     self.assertEqual(solver2048.moveDown(board), 
    #                      [
    # [0, 0, 0, 0],
    # [0, 0, 0, 0],
    # [0, 0, 0, 0],
    # [4, 4, 0, 2]
    #     ] )




    # def test_right_0(self):
    #     board = [
    # [0, 0, 0, 0],
    # [0, 0, 0, 2],
    # [4, 0, 0, 0],
    # [0, 4, 0, 0]
    #     ]
    #     self.assertEqual(solver2048.moveRight(board), 
    #                      [
    # [0, 0, 0, 0],
    # [0, 0, 0, 2],
    # [0, 0, 0, 4],
    # [0, 0, 0, 4]
    #     ] )

    # def test_right_1(self):
    #     board = [
    # [0, 0, 0, 0],
    # [0, 2, 0, 2],
    # [4, 0, 0, 0],
    # [0, 4, 0, 0]
    #     ]
    #     self.assertEqual(solver2048.moveRight(board), 
    #                      [
    # [0, 0, 0, 0],
    # [0, 0, 0, 4],
    # [0, 0, 0, 4],
    # [0, 0, 0, 4]
    #     ] )



    # def test_right_2(self):
    #     board = [
    # [0, 0, 0, 0],
    # [0, 0, 2, 2],
    # [4, 0, 0, 4],
    # [0, 4, 0, 0]
    #     ]
    #     self.assertEqual(solver2048.moveRight(board), 
    #                      [
    # [0, 0, 0, 0],
    # [0, 0, 0, 4],
    # [0, 0, 0, 8],
    # [0, 0, 0, 4]
    #     ] )


    # def test_right_3(self):
    #     board = [
    # [0, 0, 0, 0],
    # [0, 2, 4, 2],
    # [4, 0, 0, 4],
    # [0, 4, 0, 0]
    #     ]
    #     self.assertEqual(solver2048.moveRight(board), 
    #                      [
    # [0, 0, 0, 0],
    # [0, 2, 4, 2],
    # [0, 0, 0, 8],
    # [0, 0, 0, 4]
    #     ] )


    # def test_right_4(self):
    #     board = [
    # [0, 0, 0, 0],
    # [0, 2, 4, 2],
    # [4, 0, 2, 4],
    # [0, 4, 0, 0]
    #     ]
    #     self.assertEqual(solver2048.moveRight(board), 
    #                      [
    # [0, 0, 0, 0],
    # [0,2, 4 , 2],
    # [0, 4, 2, 4],
    # [0, 0, 0, 4]
    #     ] )       

    # def test_right_5(self):
    #     board = [
    # [0, 0, 0, 0],
    # [0, 2, 2, 0],
    # [0, 0, 0, 0],
    # [0, 0, 0, 0]
    #     ]
    #     self.assertEqual(solver2048.moveRight(board), 
    #                      [
    # [0, 0, 0, 0],
    # [0, 0, 0, 4],
    # [0, 0, 0, 0],
    # [0, 0, 0, 0]
    #     ] )    



    # def test_left_0(self):
    #     board = [
    # [0, 0, 0, 0],
    # [0, 0, 0, 2],
    # [4, 0, 0, 0],
    # [0, 4, 0, 0]
    #     ]
    #     self.assertEqual(solver2048.moveLeft(board), 
    #                      [
    # [0, 0, 0, 0],
    # [2, 0, 0, 0],
    # [4, 0, 0, 0],
    # [4, 0, 0, 0]
    #     ] )

    # def test_left_1(self):
    #     board = [
    # [0, 0, 0, 0],
    # [0, 0, 2, 2],
    # [4, 0, 0, 0],
    # [0, 4, 0, 0]
    #     ]
    #     self.assertEqual(solver2048.moveLeft(board), 
    #                      [
    # [0, 0, 0, 0],
    # [4, 0, 0, 0],
    # [4, 0, 0, 0],
    # [4, 0, 0, 0]
    #     ] )



    # def test_left_2(self):
    #     board = [
    # [0, 0, 0, 0],
    # [0, 0, 2, 2],
    # [4, 0, 0, 4],
    # [0, 4, 0, 0]
    #     ]
    #     self.assertEqual(solver2048.moveLeft(board), 
    #                      [
    # [0, 0, 0, 0],
    # [4, 0, 0, 0],
    # [8, 0, 0, 0],
    # [4, 0, 0, 0]
    #     ] )


    # def test_left_3(self):
    #     board = [
    # [0, 0, 0, 0],
    # [0, 2, 4, 2],
    # [4, 0, 0, 4],
    # [0, 4, 0, 0]
    #     ]
    #     self.assertEqual(solver2048.moveLeft(board), 
    #                      [
    # [0, 0, 0, 0],
    # [2, 4, 2, 0],
    # [8, 0, 0, 0],
    # [4, 0, 0, 0]
    #     ] )


    # def test_left_4(self):
    #     board = [
    # [0, 0, 0, 0],
    # [0, 2, 4, 2],
    # [4, 0, 2, 4],
    # [0, 4, 0, 0]
    #     ]
    #     self.assertEqual(solver2048.moveLeft(board), 
    #                      [
    # [0, 0, 0, 0],
    # [2, 4, 2, 0],
    # [4, 2, 4, 0],
    # [4, 0, 0, 0]
    #     ] )      

    # def test_left_5(self):
    #     board = [
    # [0, 0, 0, 0],
    # [0, 2, 2, 0],
    # [0, 0, 0, 0],
    # [0, 0, 0, 0]
    #     ]
    #     self.assertEqual(solver2048.moveLeft(board), 
    #                      [
    # [0, 0, 0, 0],
    # [4, 0, 0, 0],
    # [0, 0, 0, 0],
    # [0, 0, 0, 0]
    #     ] )    


    
    # def test0down(self):
    #     board = [
    # [2, 0, 0, 0],
    # [2, 2, 0, 0],
    # [4, 2, 4, 8],
    # [4, 4, 4, 8]
    #     ]
    #     self.assertEqual(solver2048.moveDown(board), 
    #                      [
    # [0, 0, 0, 0],
    # [0, 0, 0, 0],
    # [4, 4, 0, 0],
    # [8, 4, 8, 16]
    #     ]
                         
    #                      )
    
    # def test0up(self):
    #     board = [
    # [2, 0, 0, 0],
    # [2, 2, 0, 0],
    # [4, 2, 4, 8],
    # [4, 4, 4, 8]
    #     ]
    #     self.assertEqual(solver2048.moveUp(board), 
    #                      [
    # [4, 4, 8, 16],
    # [8, 4, 0, 0],
    # [0, 0, 0, 0],
    # [0, 0, 0, 0]
    #     ]                
    #                      )

    # def test0left(self):
    #     board = [
    # [2, 0, 0, 0],
    # [2, 2, 0, 0],
    # [4, 2, 4, 8],
    # [4, 4, 4, 8]
    #     ]
    #     self.assertEqual(solver2048.moveLeft(board), 
                         
    # [[2, 0, 0, 0],
    # [4, 0, 0, 0],
    # [4, 2, 4, 8],
    # [8, 4, 8, 0]
    #     ])
    
    # def test0right(self):
    #     board = [
    # [2, 0, 0, 0],
    # [2, 2, 0, 0],
    # [4, 2, 4, 8],
    # [4, 4, 4, 8]
    #     ]
    #     self.assertEqual(solver2048.moveRight(board), 
                         
    # [[0, 0, 0, 2],
    # [0, 0, 0, 4],
    # [4, 2, 4, 8],
    # [0, 4, 8, 8]])

    
    # def test_eval_0(self):
    #     board = [
    # [2, 0, 0, 0],
    # [2, 2, 0, 0],
    # [4, 2, 4, 8],
    # [4, 4, 4, 8]
    #     ]

    #     up_eval = solver2048.evaluationFunction(board, "Up")
    #     down_eval = solver2048.evaluationFunction(board, "Down")
    #     right_eval= solver2048.evaluationFunction(board, "Right")
    #     left_eval = solver2048.evaluationFunction(board, "Left")

    #     self.assertEqual(up_eval > right_eval, True)
    #     self.assertEqual(down_eval > left_eval, True)
    
    # def test_eval_1(self):
    #     board = [
    # [0, 0, 0, 0],
    # [2, 2, 2, 0],
    # [0, 8, 2, 0],
    # [0, 0, 2, 0]
    #     ]

    #     # up move - 2 empty squares and merged 1 pair squares
    #     [
    #     [2, 2, 4, 0],
    #     [0, 8, 2, 0],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0]
    #         ]
        

        
    #     up_eval = solver2048.evaluationFunction(board, "Up")
    #     print('up eval')
    #     print(up_eval)

    #     # down move - 0 empty squares and merged 1 pair of squares
    #     [
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    #     [0, 2, 2, 0],
    #     [2, 8, 4, 0]
    #         ]
        
    #     down_eval = solver2048.evaluationFunction(board, "Down")
    #     print('down eval')
    #     print(down_eval)
 
    #     # right move 2 empty squares and merged 1 pair
    #     [
    #         [0, 0, 0, 0],
    #         [0, 0, 2, 4],
    #         [0, 0, 8, 2],
    #         [0, 0, 0, 2]
    #     ]
    #     right_eval= solver2048.evaluationFunction(board, "Right")

    #     print('righteval :')
    #     print(right_eval)


    #     # left move 0 empty squares and merged 1 pair
    #     [
    #         [0, 0, 0, 0],
    #         [2, 4, 0, 0],
    #         [8, 2, 0, 0],
    #         [2, 0, 0, 0]
    #     ]

    #     left_eval = solver2048.evaluationFunction(board, "Left")
    #     print('left eval')
    #     print(left_eval)

    #     # right and up move is best 
    #     self.assertEqual(right_eval > left_eval, True)
    #     self.assertEqual(right_eval > down_eval, True)

# %%
