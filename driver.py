__author__ = 'lego90511'
from Tkinter import *
import animation


class Alien(object):
    def __init__(self):
        #Set up canvas
        self.root = Tk()
        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        #Vars
        self.map = [[1, 0, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [1, 0, 0, 1, 0]]
        self.x = 0
        self.y = 0
        r = 50
        self.land = {}
        #Draw Init
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                color = "black" if cell else "green"
                self.canvas.create_rectangle(r * i, r * j, r * (i + 1), r * (j + 1),
                                             outline=color, fill=color)
                self.land[(i, j)] = self.canvas.create_text(r * i, r * j, anchor=NE, fill="white", text="1", tag=str((i, j)))
        self.creature = self.canvas.create_rectangle(r * self.x, r * self.y, r * (self.x + 1), r * (self.y + 1),
                                                     outline="red", fill="red")
        self.canvas.pack(fill=BOTH, expand=1)
        #Action
        movement = animation.Animation(self.root, self.canvas, self.creature, self.land)
        self.root.after(0, movement.animate)
        #Clost TK
        self.root.mainloop()
a = Alien()