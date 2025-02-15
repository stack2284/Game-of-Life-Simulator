import pygame , random

ALIVE = (255 , 255 , 255) 
DEAD = (0 , 0 , 0)
class Grid: 
    def __init__(self , width , height , cell_size):
        self.rows = height // cell_size 
        self.columns = width // cell_size 
        self.cell_size = cell_size; 
        self.cells = [ [0 for _ in range(self.columns)] for _ in range(self.rows) ]
        
    
    
    def draw(self , window ) : 
        for row in range(self.rows) : 
            for column in range(self.columns):
                color = ALIVE if self.cells[row][column] else DEAD
                pygame.draw.rect(window , color , (column*self.cell_size , row*self.cell_size , self.cell_size - 1 ,self.cell_size - 1));
                
    def inti_random(self) : 
        for i in range(self.rows) : 
            for j in range(self.columns) : 
                self.cells[i][j] = random.choice([1 , 0 , 0 , 0])
                
                
