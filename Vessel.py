###Création classe/objet vaisseau pour un space invader par CRONOS et Aeraphal
#Date de création:17/12/2021 .Dernière modification:14/01/2021
#To do:tout

###Bibliotèques
import tkinter as tk
import Laser as L

###Class
class Vessel:
    #Classe vaisseau
    def __init__(self,canvas,window=None):
        self.life=3
        self.hitbox=[36,37]
        self.x = 500
        self.y = 463
        self.cheat_move=0
        self.canvas=canvas
        self.window=window
        self.image= tk.PhotoImage(file="vessel.gif")
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

    def move_up(self,event):
        if self.cheat_move==1:
            dy=-5
            if  self.y>= 0: 
                self.canvas.move(self.canvas_image,0,dy)
                self.y=self.y +dy

    def move_down(self,event):
        if self.cheat_move==1:
            dy=5
            if  self.y< 455: 
                self.canvas.move(self.canvas_image,0,dy)
                self.y=self.y +dy
    
    def move_left(self,event):
        dx=-5
        if  self.x >0:  
            self.canvas.move(self.canvas_image,dx,0)
            self.x=self.x+dx
            
    
    def move_right(self,event):
        dx=5
        next_pos_max=self.hitbox[0]+self.x 
        if next_pos_max<1000: 
            self.canvas.move(self.canvas_image,dx,0)
            self.x=self.x+dx
    

    def tir(self,event,monde):
        
        laser=L.Laser(self.canvas,self.x+15,self.y-18,self.window)
        monde.laser_vessel.append(laser)
        self.window.unbind("<space>")
        laser.trajet_laser_vessel(monde)
        
       
        
        
        
    

        



