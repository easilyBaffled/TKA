__author__ = 'lego90511'
from random import randrange
import sys


class Animation():
    def __init__(self, root, canvas, creature, land):
        self.x = self.y = 0
        self.ctr = 1
        self.canvas = canvas
        self.creature = creature
        self.root = root
        self.land = land
        #self.root.after(250, self.animate)
        self.canvas.move(self.creature, 2 * 50, 2 * 50)

    def animate(self):

        self.root.after(1000, self.canvas.move, self.creature, self.x * 50, self.y * 50)
        if self.ctr > 0:
            self.root.after(1000, self.canvas.move, self.creature, self.x * 50, self.y * 50)
            for i in range(2):
                i = randrange(1, 5)
                if i == 1:
                    self.y = -1
                elif i == 2:
                    self.y = 1
                elif i == 3:
                    self.x = -1
                elif i == 4:
                    self.x = 1

                """Moves creature around canvas"""
                #self.movement()
            self.root.after(250, self.animate)

    def movement(self):
        self.root.after(1000, self.canvas.move, self.creature, self.x * 50, self.y * 50)