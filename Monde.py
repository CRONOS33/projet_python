###Création classe/objet lazers pour un space invader par CRONOS et Aeraphal
#Date de création:14/01/2022 .Dernière modification:14/01/2022
#To do:faire un vrais temps de rechargement pas un temps global qui permet de faire de faire des tires grouper (par moment)

###Bibliotèques
import random as rd
import tkinter as tk
import Wall as W
import Enemy as E
import Pile_File as PF



##Class
class Monde:
    def __init__(self,canvas,window=None):
        self.score_txt=None
        self.v_life_txt=None
        self.txt_lose=None
        self.txt_win=None
        self.canvas=canvas
        self.window=window
        self.enemy=[]
        self.enemyb=None
        self.vessel=PF.File()
        self.laser_enemy=[]
        self.laser_vessel=[]
        self.wall=[]
        self.refultime=1000
    
    def collision_laser_enemy(self):
        #S'il y a une collision
        for enemy in self.enemy:
            for laser in self.laser_vessel:
                for laser_x, laser_y in laser.coordinates:
                    if enemy.min_x <= laser_x <= enemy.max_x and enemy.min_y <= laser_y <= enemy.max_y:
                        laser.canvas.delete(laser.canvas_image)
                        self.laser_vessel.remove(laser)
                        enemy.canvas.delete(enemy.canvas_image)
                        self.enemy.remove(enemy)
                        new_points=self.score_txt.get() + enemy.points
                        self.score_txt.set( new_points )
                        break
        if self.enemy==[] and not(self.vessel.estvide()):
            win=tk.Label(self.window,textvariable=self.txt_win)
            win.place(x=500,y=250)
            self.txt_win.set("you win")
            self.window.after(2000,self.window.destroy)
        elif self.enemy==[]:
            self.txt_lose.set("you lose")
            lose=tk.Label(self.window,textvariable=self.txt_lose)
            self.window.after(2000,self.window.destroy)
            lose.place(x=450,y=300)
        else:
            self.window.after(17,self.collision_laser_enemy)

    def collision_laser_wall(self):
        #S'il y a une collision
        for enemy in self.wall:
            for laser in self.laser_vessel:
                for laser_x, laser_y in laser.coordinates:
                    if enemy.min_x <= laser_x <= enemy.max_x and enemy.min_y <= laser_y <= enemy.max_y:
                        laser.canvas.delete(laser.canvas_image)
                        self.laser_vessel.remove(laser)
                        enemy.canvas.delete(enemy.canvas_image)
                        self.wall.remove(enemy)
                        break
            for laser in self.laser_enemy:
                for laser_x, laser_y in laser.coordinates:
                    if enemy.min_x <= laser_x <= enemy.max_x and enemy.min_y <= laser_y <= enemy.max_y:
                        laser.canvas.delete(laser.canvas_image)
                        self.laser_enemy.remove(laser)
                        enemy.canvas.delete(enemy.canvas_image)
                        self.wall.remove(enemy)
                        break
        self.window.after(17,self.collision_laser_wall)

    def collision_vessel(self):
        #S'il y a une collision
        for vessel in self.vessel.valeur:
            for enemy in self.enemy:
                for enemy_x,enemy_y in enemy.coordinates:
                    if vessel.min_x <= enemy_x <= vessel.max_x and vessel.min_y <= enemy_y <= vessel.max_y:
                        vessel.canvas.delete(vessel.canvas_image)
                        self.vessel.defile()
                        enemy.canvas.delete(enemy.canvas_image)
                        self.enemy.remove(enemy)
                        break

            for laser in self.laser_enemy:
                for laser_x, laser_y in laser.coordinates:
                    if vessel.min_x <= laser_x <= vessel.max_x and vessel.min_y <= laser_y <= vessel.max_y:
                        laser.canvas.delete(laser.canvas_image)
                        self.laser_enemy.remove(laser)
                        if vessel.life>1:
                            vessel.life=vessel.life -1
                            self.v_life_txt.set(vessel.life)
                        else:
                            vessel.life=vessel.life -1
                            self.v_life_txt.set(vessel.life)
                            vessel.canvas.delete(vessel.canvas_image)
                            self.vessel.defile()
                            
                            

                        break
                           
        if not(self.vessel.estvide()):
            self.window.after(17,self.collision_vessel)
        else:
            self.txt_lose.set("you lose")
            lose=tk.Label(self.window,textvariable=self.txt_lose)
            self.window.after(2000,self.window.destroy)
            lose.place(x=450,y=300)


    def collision_laser_enemyb(self):
        #S'il y a une collision
        for laser in self.laser_vessel:
            for laser_x, laser_y in laser.coordinates:
                enemy=self.enemyb
                if enemy.min_x <= laser_x <= enemy.max_x and enemy.min_y <= laser_y <= enemy.max_y:
                    if enemy.life==3:
                        laser.canvas.delete(laser.canvas_image)
                        self.laser_vessel.remove(laser)
                        enemy.canvas.delete(enemy.canvas_image)
                        enemy.image=tk.PhotoImage(file="vert.gif")
                        enemy.canvas_image = enemy.canvas.create_image(enemy.x,enemy.y,anchor = "nw",image=enemy.image)
                        enemy.life=enemy.life -1 
                        new_points=self.score_txt.get() + enemy.points
                        self.score_txt.set( new_points )
                        enemy.points=250
                        enemy.speed=5
                    elif enemy.life==2:
                        laser.canvas.delete(laser.canvas_image)
                        self.laser_vessel.remove(laser)
                        enemy.canvas.delete(enemy.canvas_image)
                        enemy.image=tk.PhotoImage(file="enemy.gif")
                        enemy.canvas_image = enemy.canvas.create_image(enemy.x,enemy.y,anchor = "nw",image=enemy.image)
                        enemy.life=enemy.life -1 
                        new_points=self.score_txt.get() + enemy.points
                        self.score_txt.set( new_points )
                        enemy.points=100
                        enemy.speed=3

                    else:
                        laser.canvas.delete(laser.canvas_image)
                        self.laser_vessel.remove(laser)
                        enemy.canvas.delete(enemy.canvas_image)
                        enemy.life=enemy.life -1 
                        new_points=self.score_txt.get() + enemy.points
                        self.score_txt.set( new_points )
                        self.enemyb=None
                        
                    break
        if self.enemyb  != None:
            self.window.after(17,self.collision_laser_enemyb)






    def bind(self):
        if not(self.vessel.estvide()):
            self.window.bind("<space>",lambda e : self.vessel.valeur[0].tir(e,self))
            self.window.after(self.refultime,self.bind)
        else:
            self.window.unbind("<space>")





    def creation_ceinture(self):
        x=50
        y=350
        for i in range(4):
            for j in range(3):
                self.wall.append(W.Wall(self.canvas,x+i*25,y+j*25,self.window))
        x=x+4*25+100
        for i in range(4):
            for j in range(3):
                self.wall.append(W.Wall(self.canvas,x+i*25,y+j*25,self.window))
        x=x+4*25+100
        for i in range(4):
            for j in range(3):
                self.wall.append(W.Wall(self.canvas,x+i*25,y+j*25,self.window))
        x=x+4*25+100
        for i in range(4):
            for j in range(3):
                self.wall.append(W.Wall(self.canvas,x+i*25,y+j*25,self.window))
        x=x+4*25+100
        for i in range(4):
            for j in range(3):
                self.wall.append(W.Wall(self.canvas,x+i*25,y+j*25,self.window))
        
    def creation_armada(self):
        x=150
        y=100
        for i in range(10):
            self.enemy.append(E.Enemy(self.canvas,x+i*65,y,self.window))
        for enemy in self.enemy:
            enemy.op=1


    def tir_enemy(self):
        for enemy in self.enemy:
            enemy.tir(self)
        self.window.after(rd.randint(1000,5000),self.tir_enemy)
        
    def trajet_enemy(self):
        n=len(self.enemy)
        
        if n>=1:
            if self.enemy[0].speed !=6 and n <= 4  :

                for enemy in self.enemy:
                    enemy.speed = 6
                    

            direction=self.enemy[0].direction
            if self.enemy[0].y>=470:
                self.txt_lose.set("you lose")
                lose=tk.Label(self.window,textvariable=self.txt_lose)
                self.window.after(2000,self.window.destroy)
                lose.place(x=450,y=300)

            elif direction==1 and self.enemy[n-1].x<=950:
                for enemy in self.enemy:
                    enemy.move_right()
            elif direction==1 and self.enemy[n-1].x>950 :
                for enemy in self.enemy:
                    enemy.direction=(direction+1)%2
                    enemy.move_down()
            elif direction==0 and self.enemy[0].x>0:
                for enemy in self.enemy:
                    enemy.move_left()
            elif direction==0 and self.enemy[0].x<=0:
                for enemy in self.enemy:
                    enemy.direction=(direction+1)%2
                    enemy.move_down()
            

            self.window.after(17,self.trajet_enemy) 
    
    def trajet_enemyb(self):
        if self.enemyb != None:
            direction=self.enemyb.direction
            if  direction == 1 and self.enemyb.x<=960:
                self.enemyb.move_right()
            elif direction==1 and self.enemyb.x>960:
                self.enemyb.direction=0
            elif direction==0 and self.enemyb.x>3:
                self.enemyb.move_left()
            else:
                self.enemyb.direction=1

            self.window.after(17,self.trajet_enemyb)