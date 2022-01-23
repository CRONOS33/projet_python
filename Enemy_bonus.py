###Création classe/objet ennemi bonys pour un space invader par CRONOS et Aeraphal
#Date de création:07/01/2022 .Dernière modification:23/01/2022
#To do:tout
import tkinter as tk

class Enemy_bonus:
    #Classe enemy
    def __init__(self,canvas,x,y,window=None):
        self.points=500
        self.life=3
        self.op=0
        self.hitbox=[40,40]
        self.x = x
        self.y = y
        self.canvas=canvas
        self.speed=8
        self.direction=1
        self.window=window
        self.image= tk.PhotoImage(file="rouge.gif")
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

    def move_up(self):
        dx=0
        dy=-self.speed
        self.canvas.move(self.canvas_image,dx,dy)
        self.x=self.x +dx
        self.y=self.y +dy

    def move_down(self):
        dx=0
        dy=self.speed*9.9
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