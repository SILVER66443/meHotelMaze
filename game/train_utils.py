import numpy as np
from labyrinth import prim_self
from game import map_utils


class Model(map_utils.Map):

    def __init__(self, mazemat):

        map_utils.Map.__init__(self, mazemat)
        # 动作空间
        self.actions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # 状态空间的v值
        self.v = dict()
        for i in range(self.mazesize[0]):
            for j in range(self.mazesize[1]):
                self.v[(i, j)] = 0
        # 决策矩阵
        self.pi = dict()
        for i in range(self.mazesize[0]):
            for j in range(self.mazesize[1]):
                self.pi[(i, j)] = self.getAction((i, j))

    def getAction(self, state):

        a_temp = []
        for a in self.actions:
            self.seeker = state
            if self.stateMove(a) != (0, 0):
                a_temp.append(a)
        return a_temp

    def display(self):
        print(self.v)
        print(self.pi)

mazemat = prim_self.PrimMaze().getMaze()
print(mazemat)
model = Model(mazemat)
model.display()
