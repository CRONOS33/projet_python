###Création classe/objet lazers pour un space invader par CRONOS et Aeraphal
#Date de création:07/01/2022 .Dernière modification:23/01/2022
#To do:#une fonction tir avec un temps de recharge random

###Bibliotèques
import tkinter as tk


##Class laser

class Laser:
    def __init__(self,canvas,x,y,window=None):
        self.hitbox=[5,18] #taille du laser [x,y]
        self.x=x           #postion en x du laser
        self.y=y           #postion en y du laser
        self.canvas=canvas  #canvas lié à l'ennemi
        self.speed=3        #permet le deplacement plus ou moins rapide du laser
        self.window=window  #fenêtre lié au laser
        self.image= tk.PhotoImage(file="Laser.gif")
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
        #permet de connaitre les coordonées des 4 points du laser
        return [[self.x,self.y],[self.x+self.hitbox[0],self.y],[self.x,self.y+self.hitbox[1]],[self.x+self.hitbox[0],self.y+self.hitbox[1]]]

    def move_up(self):
        #permet le deplacement vers le haut
        dy=-self.speed
        self.canvas.move(self.canvas_image,0,dy)
        self.y=self.y +dy

    def move_down(self):
        #permet le deplacement vers le bas
        dy=self.speed
        self.canvas.move(self.canvas_image,0,dy)
        self.y=self.y +dy
    

    def trajet_laser_vessel(self,monde):
        #permet le trajet d'un laser partant du navir
        if self.y+self.hitbox[1]>0:
            if self in monde.laser_vessel:
                self.move_up()
                self.window.after(17,self.trajet_laser_vessel,monde)
        else:
            #permet de faire disparaitre le laser si il vas trop haut
            self.canvas.delete(self.canvas_image)
            monde.laser_vessel.remove(self)
        

    def trajet_laser_enemy(self,monde):
        #permet le trajet d'un laser partant d'un ennemi
        if self.y<500:
            if self in monde.laser_enemy:
                self.move_down()
                self.window.after(17,self.trajet_laser_enemy,monde)
        else:
            #permet de faire disparaitre le laser si il vas trop bas
            self.canvas.delete(self.canvas_image)
            monde.laser_enemy.remove(self)
           
    
