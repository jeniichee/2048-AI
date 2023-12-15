import copy 
import random
from view import View

class Board:
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