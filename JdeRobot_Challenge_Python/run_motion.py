
from BrownianMotion.Brownianmotion import BrownianMotion

import numpy as np
import pygame
import time


def main():

    # Brownian Motion object
    brownianmotion = BrownianMotion()

    # Initialise pygame
    pygame.init()

    # Display the window
    display = pygame.display.set_mode(brownianmotion.windowsize)
    simulation = True
    
    while simulation:

        # Close button to close the simulation window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                simulation = False

        # simulate robot
        brownianmotion.start_robot()

        # fill the window with white
        display.fill((255, 255, 255))

        # draw point robot 
        pygame.draw.circle(display, brownianmotion.robot_color, brownianmotion.position.astype(int), brownianmotion.robot_radius)
       
        # update screen
        pygame.display.update()

        # wait
        time.sleep(0.0095)

    pygame.quit()

if __name__ == "__main__":
    main()


