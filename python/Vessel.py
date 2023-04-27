###Création classe/objet navire pour un space invader par CRONOS et Aeraphal
#Date de création:17/12/2021 .Dernière modification:23/01/2021
#To do:Il y a des redondances de fonctions et propriétées avec d'autres classes il y 
#donc possiblité de créer un classe mère les regroupants.
# On pourrai avoir plus type de tire et de navire


###Bibliotèques
import tkinter as tk
import Laser as L

###Class Navire

class Vessel:
    def __init__(self,canvas,window=None):
        self.life=3             #points de vie du navire
        self.hitbox=[36,37]     #taille du navire
        self.x = 500            #position en x
        self.y = 463            #position en y
        self.cheat_move=0       #permet de cheat et ce deplacer vers le haut et le bas
        self.canvas=canvas      #canvas lié au navire
        self.window=window      #fenêtre lié au navire
        self.image= tk.PhotoImage(file="Image/vessel.gif")
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

    def move_up(self,event):
        #permet le deplacement vers le haut
        if self.cheat_move==1:
            dy=-5
            if  self.y>0: 
                self.canvas.move(self.canvas_image,0,dy)
                self.y=self.y +dy

    def move_down(self,event):
        #permet le deplacement vers le bas
        if self.cheat_move==1:
            dy=5
            if  self.y< 455: 
                self.canvas.move(self.canvas_image,0,dy)
                self.y=self.y +dy
    
    def move_left(self,event):
        #permet le deplacement vers la gauche
        dx=-5
        if  self.x >0:  
            self.canvas.move(self.canvas_image,dx,0)
            self.x=self.x+dx
            
    
    def move_right(self,event):
        #permet le deplacement vers la droite
        dx=5
        next_pos_max=self.hitbox[0]+self.x 
        if next_pos_max<1000: 
            self.canvas.move(self.canvas_image,dx,0)
            self.x=self.x+dx
    

    def tir(self,event,monde):
        #permet au navire de tire en créant un laser a la position du navire
        
        laser=L.Laser(self.canvas,self.x+15,self.y-18,self.window)
        monde.laser_vessel.append(laser)

        #tentative de "no spam" du tir
        self.window.unbind("<space>")

        laser.trajet_laser_vessel(monde)
        
       
        
        
        
    

        



