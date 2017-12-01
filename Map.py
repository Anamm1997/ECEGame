
from Tkinter import *


import random
canvas_width   = 800
canvas_height  = 450

master2 = None
def reset():
    pass

def click( event ):
    global imageID
    w.delete(imageID)  # Delete the icon representing your previous stop.

    x1, y1 = event.x, event.y  # Get mouse click coordinates. (0,0) is the top left corner of the map.
    print "Location:", x1, y1
    x2, y2 = ( event.x + 10), (  event.y + 10 )
    # id = w.create_oval( x1, y1, x2, y2, fill = 'yellow', outline = 'blue')
    imageID = w.create_image(x1, y1, image=fisher_image)



# Improved version which will change color n times, instead of forever.
def change_color(my_widget, n):
    if n==0:
        return  # Done flashing
    else:
        current_color = my_widget.cget("background")
        next_color = "red" if current_color == "yellow" else "yellow"
        my_widget.config(background=next_color)
        master.after(250, change_color, my_widget , n-1)

def lets_quit():
    pass

def close_windows():
    frame.destroy()

def make_new():
    global frame

    frame = Toplevel()
    quitButton = Button(frame, text='Quit', width=25, command=close_windows)
    quitButton.pack()



master = Tk()
master.title( "Fish Hunt" )
w = Canvas(master,
           width=canvas_width,
           height=canvas_height, bg="lightblue")

map_image = PhotoImage(file="images/map2.gif")
fisher_image = PhotoImage(file="images/fisher.gif")
w.create_image(0,0, image=map_image,  anchor=NW)
imageID = w.create_image(0,0, image=fisher_image, anchor=NW)

print "The dimensions of the map image are:",  map_image.width(), map_image.height()



# Add widgets to GUI

info_label = Label( master, text = "Now begins your nautical escapades!\nChoose a location to start your ADVENTURE!." , bg = "white")
info_label.grid(row=0, column=0, columnspan=3, sticky="EW")


w.grid(row=1, column=0, columnspan=3)
# w.bind( "<B1-Motion>", paint )
w.bind( "<Button-1>", click )

new_button = Button(master, text="New Window", command=make_new)
new_button.grid(row=3, column=1)


quit_button = Button(master, text="QUIT", command=lets_quit)
quit_button.grid(row=3, column=2)

mainloop()