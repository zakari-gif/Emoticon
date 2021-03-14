# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
""" 
import pygame
from Q1GeneralConfiguration import GeneralConfiguration

def main():

    #Creates an instance of the class GeneralConfiguration
    generalConfiguration = GeneralConfiguration()
    print(generalConfiguration.get_emoticonSize())
    print(generalConfiguration.get_buttonWidth())
    print(generalConfiguration.get_buttonHeight())
    print(generalConfiguration.get_emoticonBorder())
    print(generalConfiguration.get_screen())
    
    #Infinite loop    
    while True:
        #Waits for an event
        event = pygame.event.wait()
 
        #Checks if the user wants to quit
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        
        #Display the drawing
        elif event.type == pygame.USEREVENT:
            generalConfiguration.display()
        #Checks if the user has clicked with the m               
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Just pass
            pass
                
# Calls the main functionef
if __name__ == "__main__":
    main()
