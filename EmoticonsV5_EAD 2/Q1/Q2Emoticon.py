# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import pygame
import math
from Q1GeneralConfiguration import GeneralConfiguration

class Emoticon:
    generalConfiguration = GeneralConfiguration()
    # Setters
    def setGeneralConfiguration(self, generalConfiguration):
        self.generalConfiguration = generalConfiguration
    # Draws the emoticon    
    def draw(self):   
        self.head(0)
        self.setEmoticonParameters(400)
        eyeLeftPosition=self.headToArea(self.eyeLeftPosition)
        self.eye(eyeLeftPosition)
        eyeRightPosition=self.headToArea(self.eyeRightPosition)
        self.eye(eyeRightPosition)
        mouthPosition=self.headToArea(self.mouthPosition)
        self.mouth(mouthPosition,1)
    def headToArea(self, position):
        x=position[0]+self.generalConfiguration.get_screen().get_width()//2
        y=self.generalConfiguration.get_screen().get_height()//2-position[1]
        return [x,y]
    def color(self, x):
        couleur=[]
        if x==0:
            couleur=[255,255,0]
        elif -1<=x<0:
            couleur=[255,255+255*x,0]
        elif 0<x<=1:
            couleur=[-255*x+255,255,0]
        return couleur
    def head(self, x):
        couleur=self.color(x)
        pygame.draw.circle(self.generalConfiguration.screen, couleur,self.headToArea([0,0]),self.generalConfiguration.emoticonSize/2)   
            
    def setEmoticonParameters(self, size):
        self.eyeWidth = 0.1*size
        self.eyeHeight = 0.15*size
        self.eyeLeftPosition = [-0.15*size,0.1*size]
        self.eyeRightPosition = [0.15*size,0.1*size]
        self.mouthPosition = [0, -0.25*size]
        self.mouthMaxHeight = 0.3*size
        self.mouthMaxWidth = 0.55*size
        self.mouthAngle = math.pi/10
        
    def eye(self, position):
        pygame.draw.ellipse(self.generalConfiguration.screen,[0,0,0],[position[0]-self.eyeWidth//2,position[1]+self.eyeHeight//2,self.eyeWidth,self.eyeHeight])
        
    def mouth(self,position,x):
        if x>0.15:
            pygame.draw.arc(self.generalConfiguration.screen,[0,0,0],[position[0]-self.mouthMaxWidth/2,position[1]-self.mouthMaxHeight, self.mouthMaxWidth, self.mouthMaxHeight], math.pi+self.mouthAngle ,2*math.pi-self.mouthAngle)
        
        elif x<-0.15:
            pygame.draw.arc(self.generalConfiguration.screen,[0,0,0],[position[0]-self.mouthMaxWidth/2,position[1]-self.mouthMaxHeight/2, self.mouthMaxWidth, self.mouthMaxHeight],self.mouthAngle ,math.pi-self.mouthAngle)
        elif -0.15<x<0.15:
            pygame.draw.arc(self.generalConfiguration.screen,[0,0,0],[position[0]-self.mouthMaxWidth/2,position[1]],[position[0]+self.mouthMaxWidth/2,position[1]])
            