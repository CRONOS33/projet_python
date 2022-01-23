###Création classe/objet mur pour un space invader par CRONOS et Aeraphal
#Date de création:14/01/2021 .Dernière modification:14/01/2021
#To do:tout
###Bibliotèques

import tkinter as tk
import Laser as L
import Monde as M

class Wall:
    #Classe vaisseau
    def __init__(self,canvas,x,y,window=None,):
        self.hitbox=[23,23]
        self.x = x
        self.y = y
        self.canvas=canvas
        self.window=window
        self.image= tk.PhotoImage(file="Wall.gif")
        self.canvas_image = self.canvas.create_image(self.x,self.y,anchor = "nw",image=self.image)

    @property
    def min_x(self):
        return self.x

    @property
    def min_y(self):
        return self.y

    @property
    def max_x(self):
        return self.x + self.hitbox[0]

    @property
    def max_y(self):
        return self.y + self.hitbox[1]

    @property
    def coordinates(self):
        return [[self.x,self.y],[self.x+self.hitbox[0],self.y],[self.x,self.y+self.hitbox[1]],[self.x+self.hitbox[0],self.y+self.hitbox[1]]]
