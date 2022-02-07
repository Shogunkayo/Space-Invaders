from tkinter import*
import main
root=Tk()
root.title("SPACE INVADERS")
# icon=PhotoImage(file="icon.png")
# root.iconphoto(root,icon)

root.geometry("1360x720")
mylabel=Label(root,text="Space Invaders")              #background image
bg=PhotoImage(file="bg.png")
bg1=Label(root,image=bg)
bg1.place(x=0,y=0)

def tut():
    import tkinter
    rout=Tk()

    rout.geometry("1360x720")
    rout.title("Tutorials")

    canvas = Canvas(rout, width=1360, height=720)
    bgg = PhotoImage(file="bg.png")
    bg11 = Label(root, image=bgg)
    bg11.place(x=0, y=0)
    canvas.pack()

    exit=Button(rout,text="Quit Tutorials",bg="black",fg="white",padx=390,pady=50,command=rout.quit)
    exit.place(x=255,y=600)
    rout.mainloop()

def start_game():
    if main.running:
        main.run()
    if not main.running:
        main.running = True

new_game=Button(root,text="PLAY",bg="purple",fg="white",padx=190,pady=50,command=start_game)    #play button
new_game.place(x=455,y=300) 

tutorial=Button(root,text="TUTORIALS",bg="purple",fg="white",padx=175,pady=50,command=tut)   #tutorial button
tutorial.place(x=455,y=450)

exit=Button(root,text="EXIT GAME",bg="purple",fg="white",padx=175,pady=50,command=root.destroy)   #exit button
exit.place(x=455,y=600)

root.mainloop()

