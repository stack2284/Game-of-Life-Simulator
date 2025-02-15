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

##game loop
while True : 
    #event handeling 
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_r and simulation.run == False:
                simulation.grid.inti_random() 
                continue
            if event.key == pygame.K_SPACE : 
                simulation.Toggle_Sim()
            if event.key == pygame.K_UP : 
                FRAMES_PER_SECOND += 2 
            if event.key == pygame.K_DOWN and FRAMES_PER_SECOND >= 5: 
                FRAMES_PER_SECOND -= 2
                
            
            
    #updating state 
    simulation.update()
    #drawing 
    window.fill((255 ,255, 255))
    simulation.draw(window)
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
  
    
    
    
 