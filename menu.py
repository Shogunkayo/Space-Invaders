from tkinter import *
import main

def open_tutorial(window):
    if window:
        window.destroy()
    root=Tk()
    root.title("Tutorials")
    root.geometry("1280x720")

    bg_image = PhotoImage(file="images/tutorialimg.png")
    bg = Label(root, image=bg_image)
    bg.place(x=0, y=0)
    
    exit=Button(root,text="Back to menu",bg="purple",fg="white",padx=50,pady=20,command=lambda: main_menu(root))
    exit.place(x=70,y=600)
    root.mainloop()

def start_game(window):
    window.destroy()
    if main.running:
        main.run()
    if not main.running:
        main.running = True
        main_menu(0)

def main_menu(window):
    if window:
        window.destroy()

    root = Tk()
    root.title("SPACE INVADERS")
    root.geometry("1280x720")

    bg_img=PhotoImage(file="images/bg.png")
    bg=Label(root,image=bg_img)
    bg.place(x=0,y=0)

    new_game=Button(root,text="PLAY",bg="purple",fg="white",padx=190,pady=50,command=lambda: start_game(root))    #play button
    new_game.place(x=455,y=250) 

    tutorial=Button(root,text="CONTROLS",bg="purple",fg="white",padx=175,pady=50,command=lambda: open_tutorial(root))   #tutorial button
    tutorial.place(x=455,y=400)

    exit=Button(root,text="EXIT GAME",bg="purple",fg="white",padx=175,pady=50,command=root.destroy)   #exit button
    exit.place(x=455,y=550)

    root.mainloop()


main_menu(0)
