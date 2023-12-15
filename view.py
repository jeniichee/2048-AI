from matplotlib import pyplot as plt
from matplotlib import colors

import numpy as np

class View(): 
    
    def draw(state, score): 
        state = np.array(state)
        score = str(score)

        _, ax = plt.subplots()
        
        for (i, j), z in np.ndenumerate(state):
            if state[i][j] == 0: 
                ax.annotate('',xy = (j + 0.4, i + 0.6))
            else:    
                ax.annotate('{}'.format(z), xy = (j + 0.4, i + 0.6), fontsize=15)
        
        ax.imshow(state, cmap='Pastel1', extent=(0, state.shape[0], state.shape[1], 0))
        ax.set_title("Score: " + score)
        ax.set_axis_off()
        plt.tight_layout()
        plt.show()
    

# import tkinter as tk
# import random 
# import copy

# from solver import solver2048


# class View(tk.Frame):
    
#     Color_grid = "#b8afa9"
#     Color_EmptyCell = "#ffd5b5"
#     Font_ScoreLabel = ("Verdana", 24)
#     Font_Score = ("Helvetica", 48, "bold")
#     Font_GameOver = ("Helvetica", 48, "bold")
#     Font_Color_GameOver = "#ffffff"
#     Winner_BG = "#ffcc00"
#     Loser_BG = "#a39489" 

#     Color_Cells = {
#         2: "#fcefe6",
#         4: "#f2e8cb",
#         8: "#f5b682",
#         16: "#f29446",
#         32: "#ff775c",
#         64: "#e64c2e",
#         128: "#ede291",
#         256: "#fce130",
#         512: "#ffdb4a",
#         1024: "#f0b922",
#         2048: "#fad74d"    
#     }

#     Color_CellNumber = {
#         2: "#695c57",
#         4: "#695c57",
#         8: "#ffffff",
#         16: "#ffffff",
#         32: "#ffffff",
#         64: "#ffffff",
#         128: "#ffffff",
#         256: "#ffffff",
#         512: "#ffffff",
#         2048: "#ffffff"
#     }

#     Fonts_CellNumebr = {
#         2: ("Helvetica", 15, "bold"),
#         4: ("Helvetica", 15, "bold"),
#         8: ("Helvetica", 15, "bold"),
#         16: ("Helvetica", 15, "bold"),
#         32: ("Helvetica", 15, "bold"),
#         64: ("Helvetica", 15, "bold"),
#         128: ("Helvetica", 15, "bold"),
#         256: ("Helvetica", 15, "bold"),
#         512: ("Helvetica", 15, "bold"),
#         1024: ("Helvetica", 15, "bold"),
#         2048: ("Helvetica", 15, "bold"),
#     }   
    
#     def __init__(self):
#         tk.Frame.__init__(self)
#         self.grid()
#         self.master.title("2048 by Salma and Jen")
 
#         self.grid_main = tk.Frame(
#             self, bg=View.Color_grid, bd=3, width=600, height=600
#         )
#         self.grid_main.grid(pady=(110,0))
#         self.cells = []
 
#         self.GUI()
#         self.solver2048 = solver2048()
        
#         self.board = self.startState()
#         self.update(self.board)
    
#         self.after(1000, self.start_game)
#         self.mainloop()
        
#     def start_game(self):
#         _, action = solver2048.value(self.board, 3, 0)
#         next_state = solver2048.getSuccessor(self.board, action)
#         successor = self.generateTile(next_state)

#         self.update_board(successor)

#         if self.solver2048.utility(next_state) == -1:
#             return

#         self.board = successor
#         self.after(1000, self.play)
#         #todo: try to make the cell frame not change w/the font..?
    
#     def startState(self):
#         return solver2048.startState()
        
#     def GUI(self): 
#         self.cells = []
#         for i in range(4):
#             row = []
#             for j in range(4):
#                 cell = tk.Frame(self.grid_main, bg=View.Color_EmptyCell, width=150, height=150) 
#                 cell.grid(row=i, column=j, padx=5, pady=5) 
#                 num = tk.Label(master=cell, text="", justify=tk.CENTER,  bg=View.Color_EmptyCell, width = 10, height = 5) # height, width? 
#                 num.grid()
#                 row.append(num)

#             self.cells.append(row)
            
#         frame_score = tk.Frame(self)
#         frame_score.place(relx=0.5, y=60, anchor="center")
#         tk.Label(
#             frame_score,
#             text="Score",
#             font=View.Font_ScoreLabel).grid(row=0)
#         self.label_score = tk.Label(frame_score, text="0", font= View.Font_Score)
#         self.label_score.grid(row=1)
        
#     def update(self, board):
#         for i in range(4):
#             for j in range(4):
#                 val = int(board[i][j])
#                 if val == 0:
#                     self.cells[i][j].configure(bg=View.Color_EmptyCell, text="" )
#                 else:
#                     self.cells[i][j].configure(bg=View.Color_Cells[val], fg=View.Color_CellNumber[val],
#                         font=View.Fonts_CellNumebr[val], text=str(val))             

#         self.update_idletasks()
    
#     def update_board(self, board):
#         # Update the GUI with the new board
#         self.update(board)

#     def generateTile(self, board):
#         # 90% 2 and 10% 4
#         return_state = copy.deepcopy(board)
#         new_value = random.choices([2,4], weights=[0.9, 0.1])[0]
        
#         tiles_needed = 1
#         while tiles_needed > 0:
#             row = random.randint(0, 3)
#             column = random.randint(0, 3)
            
#             if return_state[row][column] == 0:
#                 return_state[row][column] = new_value
#                 tiles_needed -= 1 
#         return return_state
    

#     # def make_auto_move(self):
#     #     actions = ["Up", "Down", "Left", "Right"]
#     #     action = solver2048.value(self.board, depth=3, player=0)[1]
#     #     if action in actions:
#     #         self.board = solver2048.getSuccessor(self.board, action)
#     #         self.update_board()
#     #         self.after(1000, self.make_auto_move)  # Repeat the process every second

# view = View()
    

# import tkinter as tk
# import random 
# import copy

# from solver import solver2048


# class View(tk.Frame):
    
#     Color_grid = "#b8afa9"
#     Color_EmptyCell = "#ffd5b5"
#     Font_ScoreLabel = ("Verdana", 24)
#     Font_Score = ("Helvetica", 48, "bold")
#     Font_GameOver = ("Helvetica", 48, "bold")
#     Font_Color_GameOver = "#ffffff"
#     Winner_BG = "#ffcc00"
#     Loser_BG = "#a39489" 

#     Color_Cells = {
#         2: "#fcefe6",
#         4: "#f2e8cb",
#         8: "#f5b682",
#         16: "#f29446",
#         32: "#ff775c",
#         64: "#e64c2e",
#         128: "#ede291",
#         256: "#fce130",
#         512: "#ffdb4a",
#         1024: "#f0b922",
#         2048: "#fad74d"    
#     }

#     Color_CellNumber = {
#         2: "#695c57",
#         4: "#695c57",
#         8: "#ffffff",
#         16: "#ffffff",
#         32: "#ffffff",
#         64: "#ffffff",
#         128: "#ffffff",
#         256: "#ffffff",
#         512: "#ffffff",
#         2048: "#ffffff"
#     }

#     Fonts_CellNumebr = {
#         2: ("Helvetica", 15, "bold"),
#         4: ("Helvetica", 15, "bold"),
#         8: ("Helvetica", 15, "bold"),
#         16: ("Helvetica", 15, "bold"),
#         32: ("Helvetica", 15, "bold"),
#         64: ("Helvetica", 15, "bold"),
#         128: ("Helvetica", 15, "bold"),
#         256: ("Helvetica", 15, "bold"),
#         512: ("Helvetica", 15, "bold"),
#         1024: ("Helvetica", 15, "bold"),
#         2048: ("Helvetica", 15, "bold"),
#     }   
    
#     def __init__(self):
#         tk.Frame.__init__(self)
#         self.grid()
#         self.master.title("2048 by Salma and Jen")
 
#         self.grid_main = tk.Frame(
#             self, bg=View.Color_grid, bd=3, width=600, height=600
#         )
#         self.grid_main.grid(pady=(110,0))
#         self.cells = []
 
#         self.GUI()
#         self.solver2048 = solver2048()
        
#         self.board = self.startState()
#         self.update(self.board)
    
#         self.after(1000, self.start_game)
#         self.mainloop()
        
#     def start_game(self):
#         _, action = solver2048.value(self.board, 3, 0)
#         next_state = solver2048.getSuccessor(self.board, action)
#         successor = self.generateTile(next_state)

#         self.update_board(successor)

#         if self.solver2048.utility(next_state) == -1:
#             return

#         self.board = successor
#         self.after(1000, self.play)
#         #todo: try to make the cell frame not change w/the font..?
    
#     def startState(self):
#         return solver2048.startState()
        
#     def GUI(self): 
#         self.cells = []
#         for i in range(4):
#             row = []
#             for j in range(4):
#                 cell = tk.Frame(self.grid_main, bg=View.Color_EmptyCell, width=150, height=150) 
#                 cell.grid(row=i, column=j, padx=5, pady=5) 
#                 num = tk.Label(master=cell, text="", justify=tk.CENTER,  bg=View.Color_EmptyCell, width = 10, height = 5) # height, width? 
#                 num.grid()
#                 row.append(num)

#             self.cells.append(row)
            
#         frame_score = tk.Frame(self)
#         frame_score.place(relx=0.5, y=60, anchor="center")
#         tk.Label(
#             frame_score,
#             text="Score",
#             font=View.Font_ScoreLabel).grid(row=0)
#         self.label_score = tk.Label(frame_score, text="0", font= View.Font_Score)
#         self.label_score.grid(row=1)
        
#     def update(self, board):
#         for i in range(4):
#             for j in range(4):
#                 val = int(board[i][j])
#                 if val == 0:
#                     self.cells[i][j].configure(bg=View.Color_EmptyCell, text="" )
#                 else:
#                     self.cells[i][j].configure(bg=View.Color_Cells[val], fg=View.Color_CellNumber[val],
#                         font=View.Fonts_CellNumebr[val], text=str(val))             

#         self.update_idletasks()
    
#     def update_board(self, board):
#         # Update the GUI with the new board
#         self.update(board)

#     def generateTile(self, board):
#         # 90% 2 and 10% 4
#         return_state = copy.deepcopy(board)
#         new_value = random.choices([2,4], weights=[0.9, 0.1])[0]
        
#         tiles_needed = 1
#         while tiles_needed > 0:
#             row = random.randint(0, 3)
#             column = random.randint(0, 3)
            
#             if return_state[row][column] == 0:
#                 return_state[row][column] = new_value
#                 tiles_needed -= 1 
#         return return_state
    

#     # def make_auto_move(self):
#     #     actions = ["Up", "Down", "Left", "Right"]
#     #     action = solver2048.value(self.board, depth=3, player=0)[1]
#     #     if action in actions:
#     #         self.board = solver2048.getSuccessor(self.board, action)
#     #         self.update_board()
#     #         self.after(1000, self.make_auto_move)  # Repeat the process every second

# view = View()