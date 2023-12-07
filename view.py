from matplotlib import pyplot as plt
from matplotlib import colors

import numpy as np

class View(): 
    
    def draw(state): 
        state = np.array(state)

        cmap = colors.ListedColormap(['red', 
                                      'orange', 
                                      'yellow',  
                                      'green', 
                                      'blue',
                                      'purple'])
        
        _, ax = plt.subplots()
        
        for (i, j), z in np.ndenumerate(state):
            ax.annotate('{}'.format(z), xy = (j + 0.4, i + 0.6), fontsize=15)
        
        ax.imshow(state, cmap=cmap, extent=(0, state.shape[0], state.shape[1], 0))
        ax.set_axis_off()
        plt.show()
        