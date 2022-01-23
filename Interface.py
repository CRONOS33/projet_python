###Création interface graphique space invader par CRONOS et Aeraphal
#Date de création:17/12/2021 .Dernière modification:17/12/2021
#To do:responsive ?

###Bibliotèques
import string
import tkinter as tk



import Vessel as V
import Monde as M
import Enemy_bonus as Eb
import Pile_File as PF


###Variable Interface
def create_window():
    ##Créer l'interface grafiques
 

    #Window
    global main_window
    main_window = tk.Tk()
    main_window.title("Space Invader")
    main_window.geometry('1200x600+100+100')

    
    

    #Images
    background = tk.PhotoImage(file="background.gif")
    
   

    #Canvas
    
    main_canvas= tk.Canvas(main_window,width=1000,height=550,bg="black")
    main_canvas.place(x=0,y=100)
    

    #Canvas image
    main_canvas.create_image(0,0, anchor = "nw", image=background)
    
    #Objects
    global monde
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
  

    option_file=PF.Pile()
    option=tk.StringVar()
    option.set("options")
    option_file.empiler("restart")
    option_file.empiler("cheat1")
    option_file.empiler("cheat2")
    option_file.empiler("cancelcheat")

   


    def start_game():
        global vessel
        vessel=V.Vessel(main_canvas,main_window)
        monde.enemyb=Eb.Enemy_bonus(main_canvas,2,0,main_window)
        monde.vessel.enfiler(vessel)

        txt_nbscore.set(000)
        txt_nblife.set(vessel.life)

        def options(Q):
            global main_window
            global vessel
            global monde
            if option.get() == "restart":
                main_window.destroy()
                create_window()
            elif option.get() == "cheat1":
        
                vessel.life=500

                monde.v_life_txt.set(vessel.life)
            elif option.get() == "cheat2":
                vessel.cheat_move=1
            elif option.get() == "cancelcheat":
                dx=500-vessel.x
                dy=463-vessel.y
                vessel.x= 500
                vessel.y=463
                vessel.canvas.move(vessel.canvas_image,dx,dy)
                vessel.cheat_move=0
                vessel.life=3
                monde.v_life_txt.set(vessel.life)






        menu_option = tk.OptionMenu(main_window,option,*option_file.valeur,command= options)
        menu_option.place(x=1000,y=20)

        monde.creation_ceinture()
        monde.creation_armada()

        main_window.bind("<KeyPress-Left>", lambda e : vessel.move_left(e))
        main_window.bind("<KeyPress-Right>",lambda e : vessel.move_right(e))
        main_window.bind("<KeyPress-Up>", lambda e :vessel.move_up(e))
        main_window.bind("<KeyPress-Down>",lambda e : vessel.move_down(e))

        main_window.after(1,monde.bind) 
        main_window.after(1,monde.collision_laser_enemy)
        main_window.after(1,monde.collision_laser_wall)
        main_window.after(1,monde.collision_vessel)
        main_window.after(1,monde.collision_laser_enemyb)


        monde.tir_enemy()
        monde.trajet_enemy()
        monde.trajet_enemyb()
        start_button.config(state='disable')



    

    ##buttons
    start_button=tk.Button(main_window,text="start",command=start_game)
    end_button=tk.Button(main_window,text="leave the game",fg="red",command= main_window.destroy)


    start_button.place(x=1075,y=300)
    end_button.place(x=1040,y=550)

    ##display
    
    

    
    main_window.mainloop()
