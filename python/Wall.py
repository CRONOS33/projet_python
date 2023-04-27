###Création classe/objet mur pour un space invader par CRONOS et Aeraphal
#Date de création:14/01/2021 .Dernière modification:23/01/2021
#To do:Il y a des redondances de fonctions et propriétées avec d'autres classes il y 
#donc possiblité de créer un classe mère les regroupants.
#differant mur avec des pv differents

###Bibliotèques

import tkinter as tk

 #Classe mur
class Wall:
   
    def __init__(self,canvas,x,y,window=None,):
        self.hitbox=[23,23] #taille de chaque parties du mur
        self.x = x          #position en x 
        self.y = y          #position en y
        self.canvas=canvas  #canvas lié au mur
        self.window=window  #fenêtre lié au mur
        self.image= tk.PhotoImage(file="Image\Wall.gif")
        self.canvas_image = self.canvas.create_image(self.x,self.y,anchor = "nw",image=self.image)

    @property 
    def min_x(self):
        #permet de connaitre la position minimum en x
        return self.x
    
    @property
    def min_y(self):
        #permet de connaitre la position minimum en y
        return self.y
    
    @property
    def max_x(self):
        #permet de connaitre la position maximum en x
        return self.x + self.hitbox[0]
    
    @property
    def max_y(self):
        #permet de connaitre la position maximum en y
        return self.y + self.hitbox[1]
    
    @property
    def coordinates(self):
        #permet de connaitre les coordonées des 4 points du navire
        return [[self.x,self.y],[self.x+self.hitbox[0],self.y],[self.x,self.y+self.hitbox[1]],[self.x+self.hitbox[0],self.y+self.hitbox[1]]]