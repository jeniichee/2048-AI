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
        # check if theres a loss
        # possible actions: up, down, left, right
        movepossible = False
        # action = up
        # for every possible index

        #issue with indexing -- need index from original row not alltiles

        alltiles = []
        for row in state:
            for val in row:
                alltiles.append(val)
            
            for tile in alltiles:
                numinstances = 0
                indices = []
                if tile != 0:
                    for tileindex in range(len(alltiles)):
                        if alltiles[tileindex] == tile:
                            indices.append((tileindex,tile))
                        if len(indices) != 1:
                            numinstances = len(indices)
                    if numinstances == 2:
                        print(indices)
                        print(indices[0][0])
                        print(indices[1][0])

                        if abs(indices[0][0] - indices[1][0]) == 1:
                            print('hooray!!!!!')
                            movepossible = True
                        else:
                            indexofoccurence = indices[0][0]
                            column = []
                            # find COLUMN where indices occur
                            # state -- get all rows then index colums
                            for subrow in state:
                                column.append(subrow[indexofoccurence])
                                print(column)