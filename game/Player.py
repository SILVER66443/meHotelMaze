# 玩家类、包含得分、状态等信息


class Player:
    def __init__(self):
        """ 包含当前位置、得分、状态等属性 """
        seeker = [0, 0]
        score = 0
        state = 0  # 0:ready 1:playing 2:end


    # 根据速度移动
    def state_move(self, speed):

        # 当返回的速度为0,则移动失败。
        new_seeker = [self.seeker[0] + speed[0], self.seeker[1] + speed[1]]
        # 下一个点是否可用
        if new_seeker[0] < 0 or new_seeker[0] >= self.size[0] or new_seeker[1] < 0 or new_seeker[
            1] >= self.size[1]:
            return (0, 0)
        # 是否撞墙
        if self.puzzle[new_seeker[0], new_seeker[1]] == 0:
            return (0, 0)

        self.seeker = new_seeker
        return speed

    # 是否结束
    def is_end(self, state):
        if state == self.end:
            return True
        else:
            return False

    # 重置起始点
    def reset(self):
        self.seeker = self.start

    def detector(self):
        print("seeker", self.seeker)
