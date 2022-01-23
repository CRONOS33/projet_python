###Création interface graphique space invader par CRONOS et Aeraphal
#Date de création:17/12/2021 .Dernière modification:23/01/2022
#To do:responsive ?

###Bibliotèques
import tkinter as tk

import Vessel as V
import Monde as M
import Enemy_bonus as Eb
import Pile_File as PF


###Variable Interface
def create_window():
    ##permet de créer l'interface grafiques
 

    #variable globales
    global main_window
    global monde

    #Carartéristiques de la fenêtre
    main_window = tk.Tk()
    main_window.title("Space Invader")
    main_window.geometry('1200x600+100+100')

    #Images
    background = tk.PhotoImage(file="background.gif")

    #Canvas
    main_canvas= tk.Canvas(main_window,width=1000,height=550,bg="black")
    main_canvas.place(x=0,y=100)
    main_canvas.create_image(0,0, anchor = "nw", image=background)
    
    #Creation de notre monde regroupant tous nous élements (murs,laser,navir,ennemis)
    monde=M.Monde(main_canvas,main_window)
    
    #labels
    txt_nbscore=tk.IntVar()
    txt_nblife=tk.IntVar()
    txt_win=tk.StringVar()
    txt_lose=tk.StringVar()

    score=tk.Label(main_window,text= "score  :")
    nbscore=tk.Label(main_window,textvariable=txt_nbscore)
    life=tk.Label(main_window,text= "Lives :")
    nblife=tk.Label(main_window,textvariable= txt_nblife)
    
    monde.score_txt=txt_nbscore
    monde.v_life_txt=txt_nblife
    monde.txt_win=txt_win
    monde.txt_lose=txt_lose

    score.place(x=0,y=75)
    nbscore.place(x=50,y=75)
    life.place(x=900,y=75)
    nblife.place(x=950,y=75)
  
    #Création du menu deroulant utlisable uniquement en partie
    option_file=PF.Pile()
    option=tk.StringVar()
    option.set("options")
    option_file.empiler("restart")
    option_file.empiler("cheat1")
    option_file.empiler("cheat2")
    option_file.empiler("cancelcheat")

   


    def start_game():
        #cette fonction permet de lancer la partie

        #Variables globales
        global vessel

        #Objet et mise de ces objets dans notre monde
        vessel=V.Vessel(main_canvas,main_window)
        monde.enemyb=Eb.Enemy_bonus(main_canvas,2,0,main_window)
        monde.vessel.enfiler(vessel)

        #Initialisation du score et du nombre de vie
        txt_nbscore.set(000)
        txt_nblife.set(vessel.life)

        def options(Q):
            #Cette fonction permet de gerer l'action des differentes options du menu deroulant

            #Variables globaes
            global main_window
            global vessel
            global monde

            if option.get() == "restart":
                #Permet de relancer une game mais la fermeture de l'ancienne n'est pas "propre"
                main_window.destroy()
                create_window()

            elif option.get() == "cheat1":
                #Permet à votre navire d'avoir 500 vies (oui c'est beaucoup)
        
                vessel.life=500
                monde.v_life_txt.set(vessel.life)

            elif option.get() == "cheat2":
                #Permet à votre navire de monter et descendre
                vessel.cheat_move=1

            elif option.get() == "cancelcheat":
                #Permet d'enlever les cheats précédents et vous téléporte à vos
                # coordonnées initial (peut etre utiliser en cheat (il redonne 3 vies
                # et vous tp)) 

                dx=500-vessel.x
                dy=463-vessel.y

                vessel.x= 500
                vessel.y=463

                vessel.canvas.move(vessel.canvas_image,dx,dy)

                vessel.cheat_move=0

                vessel.life=3

                monde.v_life_txt.set(vessel.life)





        #Affiche le menu d'options
        menu_option = tk.OptionMenu(main_window,option,*option_file.valeur,command= options)
        menu_option.place(x=1000,y=20)

        #créer les protections
        monde.creation_ceinture()

        #creer les ennemis
        monde.creation_armada()

        #Bind des touches
        main_window.bind("<KeyPress-Left>", lambda e : vessel.move_left(e))
        main_window.bind("<KeyPress-Right>",lambda e : vessel.move_right(e))
        main_window.bind("<KeyPress-Up>", lambda e :vessel.move_up(e))
        main_window.bind("<KeyPress-Down>",lambda e : vessel.move_down(e))

        #tentative de clock permettant un rechargement du tir du navir
        main_window.after(1,monde.bind) 

        #lancement des coloisions possibles et "valorisées"
        main_window.after(1,monde.collision_laser_enemy)
        main_window.after(1,monde.collision_laser_wall)
        main_window.after(1,monde.collision_vessel)
        main_window.after(1,monde.collision_laser_enemyb)

        #deplacement et tir des enemies
        monde.tir_enemy()
        monde.trajet_enemy()
        monde.trajet_enemyb()

        start_button.config(state='disable')



    

    ##buttons
    start_button=tk.Button(main_window,text="start",command=start_game)
    end_button=tk.Button(main_window,text="leave the game",fg="red",command= main_window.destroy)

    start_button.place(x=1075,y=300)
    end_button.place(x=1040,y=550)

    main_window.mainloop()
