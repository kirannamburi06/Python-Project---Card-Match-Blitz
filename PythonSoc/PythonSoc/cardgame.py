from tkinter import *
from PIL import Image, ImageTk
import cv2

class color:
    r = 0
def labelcolorchanger ():
    list = ['red', 'green', 'blue','orange','violet','yellow']
    color.r = (color.r+1) % (len(list))
    Title_label.config(fg=list[color.r] )
    window.after(100,labelcolorchanger)

def enter(e):
    start_button.config(bg='#1E90FF')
def leave(e):
    start_button.config(bg='blue')
def timelapse():
    interfaceLabel.config(image=logo)
    window.after(3000)

def update_frame():
    val, frame = cap.read()
    if val:
        frame = cv2.resize(frame, (window.winfo_width(), window.winfo_height()))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        video_label.imgtk = imgtk
        video_label.config(image = imgtk)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    window.after(10, update_frame)

#-----------------------------------------------------------------------------------------

window = Tk()
window.title("Card Match Blitz")
window.geometry('1800x2000')
window.configure(background='black')
realimg= Image.open("logo.png")
logo = ImageTk.PhotoImage(realimg)
window.iconphoto(True,logo)
interfaceLabel=Label(window)
interfaceLabel.place(x=500,y=150)

cap = cv2.VideoCapture('backgorund cards game.mp4')
video_label = Label(window)
video_label.pack(fill=BOTH, expand=True)

Title_label = Label(window,
                       text=" Card Match Blitz ",
                       font=('Consolas',50,'bold'),
                       bg='white',
                       fg='red'
                        )
Title_label.place(x=450,y=300)
labelcolorchanger()
start_button = Button(window,
                      text='START',
                      fg='white',
                      bg='blue',
                      font=('Century Gothic',30,'bold'),
                      padx=0,
                      pady=0,
                      bd=10,
                      relief='raised',
                      width = 10,
                      height=1,
                      activeforeground='blue',
                      activebackground='black')
start_button.bind("<Enter>",enter)
start_button.bind('<Leave>',leave)
start_button.place(x=650,y=450)

timelapse()
update_frame()

window.mainloop()

cap.release()
