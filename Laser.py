###Création classe/objet lazers pour un space invader par CRONOS et Aeraphal
#Date de création:07/01/2022 .Dernière modification:07/01/2022
#To do:tout

###Bibliotèques
import tkinter as tk
import Monde as M

##Class
class Laser:
    #Classe Laser
    def __init__(self,canvas,x,y,window=None):
        self.hitbox=[5,18]
        self.y=y
        self.x=x
        self.canvas=canvas
        self.speed=3
        self.direction=1
        self.window=window
        self.image= tk.PhotoImage(file="Laser.gif")
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
        dy=self.speed
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
        dx=self.speed*5
        dy=0
        self.canvas.move(self.canvas_image,dx,dy)
        self.x=self.x +dx
        self.y=self.y +dy

    def trajet_laser_vessel(self,monde):
        if self.y+self.hitbox[1]>0:
            if self in monde.laser_vessel:
                self.move_up()
                self.window.after(17,self.trajet_laser_vessel,monde)
        else:
            self.canvas.delete(self.canvas_image)
            monde.laser_vessel.remove(self)
        
    def trajet_laser_enemy(self,monde):
        if self.y<500:
            if self in monde.laser_enemy:
                self.move_down()
                self.window.after(17,self.trajet_laser_enemy,monde)
        else:
            self.canvas.delete(self.canvas_image)
            monde.laser_enemy.remove(self)
           
    
