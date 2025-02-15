import pygame , sys
from simulation import Sim

pygame.init();

WINDOW_WIDTH = 1000 ## dimensions of window 
WINDOW_HEIGHT = 1000
FRAMES_PER_SECOND = 10 
CELL_SIZE = 40
 
window = pygame.display.set_mode((WINDOW_HEIGHT , WINDOW_WIDTH))

pygame.display.set_caption("SIMULATION")
clock = pygame.time.Clock();

simulation = Sim(WINDOW_WIDTH , WINDOW_HEIGHT , CELL_SIZE)
simulation.grid.cells[0][0] = 1
simulation.grid.cells[0][1] = 1
simulation.grid.cells[0][2] = 1
simulation.grid.cells[1][0] = 1
print(simulation.count_live_n(simulation.grid , 0, 24))
##game loop
while True : 
    window.fill((255 ,255, 255))
    #event handeling 
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
              
    #updating state 
    
    #drawing 
    simulation.draw(window)
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
  
    
    
    
 