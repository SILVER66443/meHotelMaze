# 游戏类：由地图类和玩家类构成

import Mat
import Player


class Game:
    def __init__(self, mat):
        player = Player.Player
        maze = Mat.Mat(mat)
