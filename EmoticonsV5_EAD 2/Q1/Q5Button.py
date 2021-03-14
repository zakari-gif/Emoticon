# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame     
from Q3GeneralConfiguration import GeneralConfiguration        
class Button: 
    # Constructor      
    def __init__(self, sensor) :
        self.sensor = sensor
        
    # Gets the sensor position on the screen   
    def getPosition(self):
        return [self.sensor.generalConfiguration.buttonWidth,self.sensor.generalConfiguration.buttonHeight]

    # Draws the text 
    def draw(self):
        SIZE = [150,80]
        blanc = [255, 255, 255]
        rect =[150,70,255,80]
        pygame.draw.rect(self.sensor.generalConfiguration.screen, blanc, rect,1)
        self.drawLines(['affichage','ok'])
    
    def drawLines(self, lines):
        screen = pygame.display.get_surface()
        # Creates the font
        font = pygame.font.Font(None, 80)
        # Creates the text image containing « This is a test » written in white
        for i in lines:
            textImage = font.render(i, 1, [0,255,255],[0,0,255])
            # Pastes the image on the screen. The upper left corner is at the position 
            screen.blit(textImage,[self.sensor.generalConfiguration.buttonWidth,self.sensor.generalConfiguration.buttonHeight])
      

