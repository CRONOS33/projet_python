###Création classe/objet ennemis pour un space invader par CRONOS et Aeraphal
#Date de création:07/01/2022 .Dernière modification:23/01/2022
#To do:Il y a des redondances de fonctions et propriétées avec d'autres classes il y 
#donc possiblité de créer un classe mère les regroupants.
#il est possible aussi de rajouter à cette ennemi des points de vies et de gérer son etat (affichage)


###Bibliotèques
import tkinter as tk

import Laser as L

#La classe enemi
class Enemy:
    
    def __init__(self,canvas,x,y,window=None):
        self.points=100     #score offert par l'ennemi lors de l'élimination
        self.op=0           #permet à l'ennemi de tirer (1) ou non (0)
        self.hitbox=[37,30] #taille de l'ennemie [x,y]
        self.x = x          #position x du canvas
        self.y = y          #position y du canvas
        self.canvas=canvas  #canvas lié à l'ennemi
        self.speed=3        #permet le deplacement plus ou moins rapide de l'ennemi
        self.direction=1    #permet le deplacement a droite ou a gauche 
        self.window=window  #fenêtre lié à l'ennemi
        self.image= tk.PhotoImage(file="enemy.gif")
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
        #permet de connaitre les coordonées des 4 points de l'ennemi
        return [[self.x,self.y],[self.x+self.hitbox[0],self.y],[self.x,self.y+self.hitbox[1]],[self.x+self.hitbox[0],self.y+self.hitbox[1]]]


    def move_down(self):
        #permet de deplacer l'enemi vers le bas
        dy=3*4.9
        self.canvas.move(self.canvas_image,0,dy)
        self.y=self.y +dy
    
    def move_left(self):
        #permet de deplacer l'ennemi vers la gauche
        dx=-self.speed
        self.canvas.move(self.canvas_image,dx,0)
        self.x=self.x +dx
    
    def move_right(self):
        #permet de deplacer l'ennemi vers la droite
        dx=self.speed
        self.canvas.move(self.canvas_image,dx,0)
        self.x=self.x +dx
    
    def tir(self,monde):
        #permet à l'ennemi de tier en créant un objet laser à la position de l'alien 
        # et en deplancant celui-ci
        if self.op==1:
            
            laser=L.Laser(self.canvas,self.x+18,self.y+self.hitbox[1]+18,self.window)
            monde.laser_enemy.append(laser)
            laser.trajet_laser_enemy(monde)