from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk

app = Tk()
app.title("AI project")
app.geometry('750x700')
app.configure(bg = "#263D42")
              
myFont = font.Font(size = 11)
              
Label(app, 
	text="Board puzzle illustration through DFS",
	fg = "white",
    bg = "#263D42",
	font = "Helvetica 16 bold italic").pack()

canvas = Canvas(app, height = 700, width = 700, bg = "#263D42" )
canvas.pack(expand = 'YES', fill = BOTH)

def startApp():
    app.destroy()
    import Validator

def closeApp():
    d=messagebox.askquestion("Confirm","Are you sure?") 
    if(d == 'yes'):
        app.destroy()

def startFunc():
    img = Image.open('image.png')
    img = img.resize((550, 550), Image.ANTIALIAS)
    canvas.image = ImageTk.PhotoImage(img)
    canvas.create_image(380, 260, image = canvas.image)
    
    startButton = Button(app, text = "START GAME", padx= 10, pady = 5, width = 15, fg = 'white', bg = '#263D42', command = startApp)
    startButton['font'] = myFont
    startButton.place(relx = 0.145, rely = 0.88, x = -2.5, y = 10)
    
    quitButton = Button(app, text = "QUIT", padx= 10, pady = 5, fg = 'white', bg = '#263D42', width = 15, command = closeApp) 
    quitButton['font'] = myFont                         
    quitButton.place(relx = 0.665, x = -3.5, y = 10, rely = 0.88)
    
startFunc()
app.mainloop()