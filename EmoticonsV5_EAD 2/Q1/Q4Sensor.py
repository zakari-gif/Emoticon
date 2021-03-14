# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import http
import urllib
import ssl

class Sensor:
    # Constructor
    def __init__(self, url, label, thresholds):
        self.url = url
        self.label = label 
        self.thresholds = thresholds
    
    # Setters
    def setGeneralConfiguration(self, generalConfiguration):
        self.generalConfiguration = generalConfiguration
    
    # Getters
    def getGeneralConfiguration(self):
        return self.generalConfiguration       

    def getLabel(self):
        return self.label
                     
    # Checks if the connection to the sensor is set
    def isConnectedToUrl(self):        
        try:
            self.request = urllib.request.urlopen(url=self.url, context=ssl.create_default_context(ssl.Purpose.CLIENT_AUTH))
        except OSError:
            return False
        else: 
            return self.request.getcode() == http.HTTPStatus.OK

    # Reads the sensor
    def read(self):
        if self.isConnectedToUrl():
            return self.request.read().decode('utf-8')
        else:
            return None
            
    # Gets the transformed value
            
    # Gets the transformed value
    def getTransformedValue(self):
        valeurcapteur_float=eval(self.read())
        if self.thresholds[0]<valeurcapteur_float<=self.thresholds[1]:
            valeurReduite=0.5*valeurcapteur_float-self.thresholds[1]*0.5
        elif valeurcapteur_float<=self.thresholds[0]:
            valeurReduite=-1.0
        elif valeurcapteur_float>=self.thresholds[2]:
            valeurReduite=1.0
        elif self.thresholds[1]<valeurcapteur_float<self.thresholds[2]:
            valeurReduite=valeurcapteur_float/3-self.thresholds[1]/3
        return valeurcapteur_float
            
                   
        