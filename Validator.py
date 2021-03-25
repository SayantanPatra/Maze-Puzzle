import tkinter as tk
from tkinter import *
import solveMaze

master = tk.Tk()

def evaluateMethod():
    inputList = ['bfs', 'dfs']
    temp = takeInput.get()
    if(temp.lower() in inputList):
        master.destroy()
        solveMaze.main(temp)
    else:
        messagebox.showwarning("warning", "No such technique please give valid input.")
        master.destroy()

master.geometry('600x200')
lbl_title = tk.Label(master, text = "Technique with which you want the puzzle to get solved (DFS, BFS).", font=('Helvetica 16 bold italic', 15), fg = "white", bg = "#263D42")
lbl_title.grid(row=0, column = 0)

takeInput = tk.Entry(master, font=('Helvetica 16 bold italic', 15), width = 35)
takeInput.grid(row=1, column = 0)
takeInput.focus()
takeInput.bind("<Return>",evaluateMethod)

tk.Button(master, 
          text='SUBMIT',width=15, font=('Helvetica 16 bold italic', 15), fg = "white", bg = "#263D42", command = evaluateMethod).grid(row=3, column=0, pady=4)
tk.mainloop
