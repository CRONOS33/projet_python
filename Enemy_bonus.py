###Création classe/objet ennemi bonus pour un space invader par CRONOS et Aeraphal
#Date de création:07/01/2022 .Dernière modification:23/01/2022
#To do:Il y a des redondances de fonctions et propriétées avec d'autres classes il y 
#donc possiblité de créer un classe mère les regroupants.

###Bibliotèques
import tkinter as tk

#La class ennemi bonus
class Enemy_bonus:
    
    def __init__(self,canvas,x,y,window=None):
        self.points=500       #score offert par l'ennemi bonus lors de l'élimination
        self.life=3           #Points de vie de l'ennemi bonus
        self.hitbox=[40,40]   
        self.x = x            #position x du canvas
        self.y = y            #position y du canvas
        self.canvas=canvas    #canvas lié à l'ennemi bonus
        self.speed=8          #permet le deplacement plus ou moins rapide de l'ennemi bonus
        self.direction=1      #permet le deplacement a droite ou a gauche 
        self.window=window    #fenêtre lié à l'ennemi bonus
        self.image= tk.PhotoImage(file="rouge.gif")
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
        #permet de connaitre les coordonées des 4 points de l'ennemi bonus
        return [[self.x,self.y],[self.x+self.hitbox[0],self.y],[self.x,self.y+self.hitbox[1]],[self.x+self.hitbox[0],self.y+self.hitbox[1]]]
    
    def move_left(self):
        #permet de deplacer l'enemi bonus vers la gauche
        dx=-self.speed
        self.canvas.move(self.canvas_image,dx,0)
        self.x=self.x +dx
    
    def move_right(self):
        #permet de deplacer l'enemi bonus vers la gauche
        dx=self.speed
        self.canvas.move(self.canvas_image,dx,0)
        self.x=self.x +dx