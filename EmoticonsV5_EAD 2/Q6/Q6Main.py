# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame
from Q6GeneralConfiguration import GeneralConfiguration
from Q6Sensor import Sensor
             
def main():
 
    # Creates the general configuration and the sensors
    generalConfiguration = GeneralConfiguration()
    
    generalConfiguration.addSensor(
        Sensor(
            'https://www.polytech.univ-smb.fr/apps/myreader/capteur.php?capteur=epua_b204_clim', 
            'Temp. Clim B204',
            [20, 22, 23]
        )
    )

    # Infinite loop    
    while True:

        # Waits for an event
        event = pygame.event.wait()
 
        if event.type == pygame.QUIT:
            pygame.quit()
            break 
        
        # Displays the selected sensor
        elif event.type == pygame.USEREVENT: 
            generalConfiguration.display()
                                  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Checks if the display of a new sensor is required
            generalConfiguration.checkIfSensorChanged(event.pos)
                
# Calls the main function
if __name__ == "__main__":
    main()    