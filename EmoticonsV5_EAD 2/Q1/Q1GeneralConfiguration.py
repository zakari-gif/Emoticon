# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import pygame
import math

class GeneralConfiguration:
    # Constructor
    def __init__(self):
        self.initPygame()
        # Parameters for the buttons
        self.buttonWidth = 150
        self.buttonHeight = 80
        # Parameters for the emoticons
        self.emoticonSize = 400
        self.emoticonBorder = 20

    # Initializes pygame
    def initPygame(self): 
        #Initialization
        pygame.init()
        # Sets the screen size.
        pygame.display.set_mode((800, 600))    
        # Sets the timer to check event every 200 ms
        pygame.time.set_timer(pygame.USEREVENT, 200)
        # Gets pygame screen
        self.screen =pygame.display.get_surface()
        
    # Draws on pygame screen    
    def draw(self):
        # Draws a circle in red with a center in 100, 100 and a radius equal to 80
        pygame.draw.circle(self.screen, [0,255, 0], [100, 100], 80) 
        # Draws a black ellipse contained in a rectangle whose left upper corner is 50,60, 
        # width=15 and height=20
        pygame.draw.ellipse(self.screen, [0,0,0], [50, 60, 15, 20])
        # Draws a black arc contained in a rectangle whose left upper corner is 60,120, 
        # width=80, height=30, starting angle=5*pi/4, ending angle=7*pi/4
        pygame.draw.arc(self.screen, [0,0,0], [60, 120, 80, 30], 5*math.pi/4, 7*math.pi/4)
        # Draws a black line starting in position 50,100 and ending in position 150,100
        SIZE = [500,500]
        RED = [255, 255, 255]
        rect =[20,20,160,160]
        pygame.draw.rect(self.screen, RED, rect,1)
    
        
            
    # Displays pygame screen
    def display(self):
        # Draws on the screen surface
        self.draw()        
        # Updates the displat and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)
    # Ajout des getters aux attributs
    def get_buttonWidth(self):
        return self.buttonWidth
    def get_buttonHeight(self):
        return self.buttonHeight
    def get_emoticonSize(self):
        return self.emoticonSize
    def get_emoticonBorder(self):
        return self.emoticonBorder
    def get_screen(self):
        return self.screen
    
    
    
            