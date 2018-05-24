from tkinter import *
tk = Tk()
canvas = Canvas(tk, width = 500 , height= 300)
canvas.pack()

my_image2 = PhotoImage(file = "arco.gif")
canvas.create_image(10,10,anchor= NW,image=my_image2)

my_image = PhotoImage(file = "ball.gif")
canvas.create_image(400,50,anchor= NW,image= my_image)

def moveball(event):
    if event.keysym == 'Up':
        canvas.move(2,0,-3)
    elif event.keysym == 'Down':
        canvas.move(2,0,3)
    elif event.keysym == 'Left':
        canvas.move(2,-3,0)
    else:
        canvas.move(2,2,0)
canvas.bind_all('<KeyPress-Up>',moveball)
canvas.bind_all('<KeyPress-Down>',moveball)
canvas.bind_all('<KeyPress-Left>',moveball)
canvas.bind_all('<KeyPress-Right>',moveball)
print("Posicion",canvas.winfo_pointerxy())

def Mensaje():
    if  canvas.move == canvas.move(2,10,10):
        print("Gol!!")
    else:
        print("")
tk.mainloop()

moveball()

Mensaje()





