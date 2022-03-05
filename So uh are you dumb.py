import tkinter as tk
from tkinter.font import BOLD
from turtle import window_height
import random

#setting up the main window
dumb = tk.Tk()
dumb.title("Welcum")
dumb.resizable(0, 0) 

#window size and position 
window_width = 240
window_height = 240

screen_width = dumb.winfo_screenwidth()
screen_height = dumb.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

dumb.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


#functions
#swaping the buttons around
def swap_buttons():
        No_button.config(text="Yes", command=i_knew_it)
        Yes_button.config(text="No", command=swap_buttons2)

def swap_buttons2():
        No_button.config(text="No", command=swap_buttons)
        Yes_button.config(text="Yes", command=i_knew_it)


def are_u_sure():

        random_x = random.randrange(240, (screen_width - 240))
        random_y = random.randrange(240, (screen_height - 240))

        sure = tk.Tk()
        sure.geometry(f'{window_width}x{window_height}+{random_x}+{random_y}')
        sure.title("Warning :)")
        sure.resizable(0, 0)

        thelabel = tk.Label(sure, text="Are you sure \n that you are dumb")
        thelabel.place(height=120, width=240)
        

        Yes_button = tk.Button(sure, text="Yes",font=(BOLD),command=lambda:[i_knew_it(),sure.destroy()])
        Yes_button.place(x=135, y=120)

        Yes_button2 = tk.Button(sure, text="Yes",font=(BOLD),command=lambda:[i_knew_it(),sure.destroy()])
        Yes_button2.place(x=60, y=120)

def are_u_sure_quit():

        random_x = random.randrange(240, (screen_width - 240))
        random_y = random.randrange(240, (screen_height - 240))

        sure = tk.Tk()
        sure.geometry(f'{window_width}x{window_height}+{random_x}+{random_y}')
        sure.title("Nope")
        sure.resizable(0, 0)

        thelabel = tk.Label(sure, text="Dont even try quiting",font=(BOLD))
        thelabel.place(height=120, width=240)
        
        def motion(event):
                Yes_button = tk.Button(sure, text="Yes",font=(BOLD),command=lambda:[i_knew_it(),sure.destroy()])
                Yes_button.place(x=135, y=120)

                No_button2 = tk.Button(sure, text="No",font=(BOLD))
                No_button2.place(x=60, y=120)

                thelabel.config(text="Are you dumb")

        sure.bind('<Motion>',motion)


#start up widgets

thelabel = tk.Label(dumb, text="Are you dumb",font=(BOLD))
thelabel.place(height=120, width=240)

Yes_button = tk.Button(dumb, text="Yes",font=(BOLD),command=are_u_sure)
Yes_button.place(x=135, y=120)

No_button = tk.Button(dumb, text="No",font=(BOLD),command=swap_buttons)
No_button.place(x=60, y=120)

#ending function
def i_knew_it():
    thelabel.config(text="I knew it :3")
    dumb.protocol("WM_DELETE_WINDOW", dumb.destroy)
    No_button.place_forget()
    Yes_button.place_forget()

dumb.protocol("WM_DELETE_WINDOW", are_u_sure_quit)
dumb.mainloop()