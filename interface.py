from tkinter import *
import main


root = Tk()  # Object from class Tk, blank (main) window
root.title('Beagle TitleGenerator v0.0')
root.geometry('500x300')

labelTitle = Label(root, text='TitleGenerator v0.0', fg='black')
labelTitle.grid(row=0)

button = Button(root, text='Generate', bg='lightgray', fg='blue', command=main.generateTitle)
button.grid(row=5)

root.mainloop()  # Keeps the window running until I click the close button