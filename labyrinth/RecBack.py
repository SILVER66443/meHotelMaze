import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm


class RecBack:
    def __init__(self, mazesize):
        self.size = mazesize
        self.seeker = []
        self.maze = []
        self.createmaze()

    def initmaze(self):

        # x, y = self.size
        maze = np.zeros(self.size)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if i % 2 == 1 or j % 2 == 1:
                    maze[i, j] = 1
        return maze

    def createmaze(self):
        self.maze = self.initmaze()
        x = 0
        y = 0
        history = [[x, y]]
        while history:

            self.maze[x, y] = 2
            tag = []
            # left
            if y - 2 >= 0 and self.maze[x, y - 2] == 0:
                tag.append('l')
            # right
            if y + 2 < self.size[1] and self.maze[x, y + 2] == 0:
                tag.append('r')
            # up
            if x - 2 >= 0 and self.maze[x - 2, y] == 0:
                tag.append('u')
            # down
            if x + 2 < self.size[0] and self.maze[x + 2, y] == 0:
                tag.append('d')

            if len(tag):
                history.append([x, y])
                step = random.choice(tag)

                self.maze[x, y] = 2
                if step == 'l':
                    self.maze[x, y - 1] = 2
                    y = y - 2
                if step == 'r':
                    self.maze[x, y + 1] = 2
                    y = y + 2
                if step == 'd':
                    self.maze[x + 1, y] = 2
                    x = x + 2
                if step == 'u':
                    self.maze[x - 1, y] = 2
                    x = x - 2
            else:
                x, y = history.pop()

    def dispaly(self):
        plt.imshow(self.maze, cmap=cm.Greys_r, interpolation='none')
        plt.show()

