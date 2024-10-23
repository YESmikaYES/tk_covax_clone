from tkinter import *

root = Tk()
root.title('Covax 0.5')

screen = Canvas(master=root, width=1000, height=750)
screen.pack()

def kill(self):
    root.nametowidget(self).destroy()

names = ["1", "2", "3", "4", "5"]
for i in names:
    test_button = Button(root, name=i,text = f"{i}", command=lambda: kill(str(test_button)))


root.mainloop()