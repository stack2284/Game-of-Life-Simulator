from grid import Grid

neighbourhood = [
    
    (-1 , -1) , (1 , 1 ) , (1 , 0) , (0 ,1 ) , (-1 , 0) , (0 ,-1) , (1 , -1 ) , (-1 , 1)
] 

class Sim:
    def __init__(self , width , height , cell_size): 
        self.grid = Grid(width , height , cell_size)
        self.grid.inti_random()
    
    def draw(self , window) : 
        self.grid.draw(window)
    
    def count_live_n(self , grid , i , j) : 
        oncells = 0 

        for mov in neighbourhood : 
            if self.grid.cells[(i + mov[0])%(grid.rows)][(j + mov[1])%grid.columns] == 1 :
                oncells += 1 
        return oncells 
    
    
    def update(self): 
        toggle = []
        for row in range(self.grid.rows): 
            for col in range(self.grid.columns) : 
                neighbour_cnt = self.count_live_n(self.grid , row , col)
                if(self.grid.cells[row][col]) : 
                    if(neighbour_cnt != 3 and neighbour_cnt != 2):
                        toggle.append((row , col))
                elif (self.grid.cells[row][col] == 0 and neighbour_cnt == 3) : 
                    toggle.append([row , col])
        
        for target in toggle : 
            self.grid.cells[target[0]][target[1]] += 1 ;
            self.grid.cells[target[0]][target[1]] %= 2 ;
            
        return; 

        
        

  