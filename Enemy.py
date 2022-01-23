###Création classe/objet ennemis pour un space invader par CRONOS et Aeraphal
#Date de création:07/01/2022 .Dernière modification:23/01/2022
#To do:Il y a des redondances de fonctions et propriétées avec d'autres classes il y 
#donc possiblité de créer un classe mère les regroupants.
#il est possible aussi de rajouter à cette ennemi des points de vies et de gérer son etat (affichage)


###Bibliotèques
import tkinter as tk

import Laser as L

#La classe enemy
class Enemy:
    #Classe enemy
    def __init__(self,canvas,x,y,window=None):
        self.points=100     #score offert par l'ennemi lors de l'élimination
        self.op=0           #permet à l'ennemi de tirer (1) ou non (0)
        self.hitbox=[37,30] #taille de l'ennemie [x,y]
        self.x = x          #position x du canvas
        self.y = y          #position y du canvas
        self.canvas=canvas  #canvas lier à l'ennemi
        self.speed=3        #permet le deplacement plus ou moins rapide du monstre
        self.direction=1    #permet le deplacement a droite ou a gauche 
        self.window=window  #fenêtre lier à l'ennemi
        self.image= tk.PhotoImage(file="enemy.gif")
        self.canvas_image = self.canvas.create_image(self.x,self.y,anchor = "nw",image=self.image)

    @property #
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

    def move_up(self):
        dx=0
        dy=-3*4.9
        self.canvas.move(self.canvas_image,dx,dy)
        self.x=self.x +dx
        self.y=self.y +dy

    def move_down(self):
        dx=0
        dy=3*4.9
        self.canvas.move(self.canvas_image,dx,dy)
        self.x=self.x +dx
        self.y=self.y +dy
    
    def move_left(self):
        dx=-self.speed
        dy=0
        self.canvas.move(self.canvas_image,dx,dy)
        self.x=self.x +dx
        self.y=self.y +dy
    
    def move_right(self):
        dx=self.speed
        dy=0
        self.canvas.move(self.canvas_image,dx,dy)
        self.x=self.x +dx
        self.y=self.y +dy

    
    
    def tir(self,monde):
        if self.op==1:
            laser=L.Laser(self.canvas,self.x+18,self.y+self.hitbox[1]+18,self.window)
            monde.laser_enemy.append(laser)
            laser.trajet_laser_enemy(monde)
        


    
    