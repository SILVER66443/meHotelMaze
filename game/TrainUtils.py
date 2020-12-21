import numpy as np
import random
from labyrinth import PrimLaby
from game import MapUtils


class Model(MapUtils.Map):

    def __init__(self, mazemat):

        MapUtils.Map.__init__(self, mazemat)
        # 动作空间
        self.actions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # 状态空间的v值
        self.v = dict()
        for i in range(self.mazesize[0]):
            for j in range(self.mazesize[1]):
                self.v[(i, j)] = 0.0
        # 决策矩阵
        self.pi = dict()
        for i in range(self.mazesize[0]):
            for j in range(self.mazesize[1]):
                self.pi[(i, j)] = self.get_action((i, j))
        self.gamma = 0.8

    # 获得当前点的可用路径
    def get_action(self, state):

        a_temp = []
        for a in self.actions:
            self.seeker = state
            if self.state_move(a) != (0, 0):
                a_temp.append(a)
        return random.choice(a_temp)

    def policy_evaluate(self):
        for i in range(1000):
            delta = 0.0
            for state in self.v.keys():
                if state in self.walls:
                    continue

                action = self.pi[state]
                s, r = self.transform(state, action)

                new_v = r + self.gamma * self.v[s]
                delta += abs(self.v[state] - new_v)
                self.v[state] = new_v

            print(self.v)
            if delta < 1e-6:
                break

    #def policy_improve(self):

    def transform(self, state, action):
        new_state = (state[0] + action[0], state[1] + action[1])
        if new_state == (4, 4):
            return new_state, 1
        else:
            return new_state, 0

    def display(self):
        print(self.v)
        print(self.pi)
        print(self.walls)


mazemat = PrimLaby.PrimMaze().getMaze()
print(mazemat)
model = Model(mazemat)

model.policy_evaluate()
