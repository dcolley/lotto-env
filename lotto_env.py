import numpy as np
import matplotlib.pyplot as plt
import random

'''
Rules: 
    Select 6 numbers from 59
    Pay -2 for each game
    Prize 
        6      = 1000000
        5 + bb = 100000
        5      = 10000
        4      = 1000
        3      = 25
        2      = 0
        1      = 0
'''


class LottoEnv(object):
    def __init__(self, num_balls=59, num_choices=6, has_bonus_ball=True, step_cost=-2, max_loss=10000) -> None:
        self.num_balls = num_balls
        self.num_choices = num_choices
        self.has_bonus_ball = has_bonus_ball
        self.step_cost = step_cost
        self.max_loss = max_loss
        # self.balls = np.arange(1, num_balls+1)
        self.balls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                      11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                      21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                      31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                      41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                      51, 52, 53, 54, 55, 56, 57, 58, 59]
        self.draw = []
        self.bonus_ball = None  # or 0?
        self.selection = []
        self.reward = max_loss
        self.done = False
        self.step_no = 0
        self.stats = [0, 0, 0, 0, 0, 0, 0]
        # self.render()

    def reset(self):
        self.draw_numbers()
        self.reward = self.max_loss
        self.done = False
        self.step_no = 0
        self.stats = [0, 0, 0, 0, 0, 0, 0]
        return self.draw, self.reward, self.done, (self.step_no, self.stats)

    def select_numbers(self):
        self.selection = random.sample(self.balls, self.num_choices)
        return self.selection

    def draw_numbers(self):
        # print(type(self.balls))
        self.draw = random.sample(self.balls, self.num_choices)
        # self.draw = np.random.sample(self.balls, size=self.num_choices)
        self.bonus_ball = random.choice(self.draw)
        self.draw.remove(self.bonus_ball)

    def step(self, action=None):
        self.step_no += 1
        self.draw_numbers()
        # self.reward += self.step_cost
        selection = action  # or self.select_numbers()
        self.calculate_reward(selection)
        if self.reward < 1:
            self.done = True
        if self.step_no > 1000:
            self.done = True
        return self.draw, self.reward, self.done, (self.step_no, self.stats)

    def calculate_reward(self, selection):
        algo = {
            6: 1000000,
            # 5 + bb = 100000
            5: 10000,
            4: 1000,
            3: 25,
            2: 0,
            1: 0,
            0: 0
        }
        num_balls = 0
        for ball in selection:
            if ball in self.draw:
                num_balls += 1

        if num_balls == 5 and self.bonus_ball in selection:
            reward_ = 100000
        else:
            reward_ = algo[num_balls]

        self.reward += (reward_+self.step_cost)
        self.stats[num_balls] += 1

        if self.step_no % 100 == 0:
            print(self.step_no, 'num_balls', num_balls, 'reward', reward_, 'cum reward', self.reward, self.stats)

    def render(self):
        # render the balls, draw and our selection 
        print('-----------------------------')
        for n in self.balls:
            if n in self.draw:
                print("({})".format(n), end='\t')
            else:
                print(" {} ".format(n), end='\t')
            if n % 8 == 0:
                print('\n')
        print('\n-----------------------------')


def max_action(Q, obs, possible_actions):
    return 1


