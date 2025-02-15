from grid import Grid

neighbourhood = [
    
    (-1 , -1) , (1 , 1 ) , (1 , 0) , (0 ,1 ) , (-1 , 0) , (0 ,-1) , (1 , -1 ) , (-1 , 1)
] 

class Sim:
    def __init__(self , width , height , cell_size): 
        self.grid = Grid(width , height , cell_size)
    
    def draw(self , window) : 
        self.grid.draw(window)
    
    def count_live_n(self , grid , i , j) : 
        oncells = 0 

        for mov in neighbourhood : 
            if self.grid.cells[(i + mov[0])%(grid.rows)][(j + mov[1])%grid.columns] == 1 :
                oncells += 1 
        return oncells 
        
        

  