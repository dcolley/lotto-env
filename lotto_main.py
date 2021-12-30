import numpy as np
import matplotlib.pyplot as plt

from lotto_env import LottoEnv


if __name__ == '__main__':
    print('-----')
    env = LottoEnv(num_balls=59, num_choices=6, has_bonus_ball=True, step_cost=-2, max_loss=5000)
    # env.step(None)
    
    ALPHA = 0.1
    GAMMA = 1.0
    EPS = 1.0

    # Q = {}
    # for state in env.stateSpacePlus:
    #     for action in env.possibleActions:
    #         Q[state, action] = 0
    
    numGames = 500  # 00
    totalRewards = np.zeros(numGames)

    env.render()

    for i in range(numGames):
        if i % 5000 == 0:
            print('starting game', i)

        done = False
        epRewards = 0
        observation = env.reset()

        while not done:
            # rand = np.random.random()
            # action = maxAction(Q, observation, env.possibleActions) if rand < (1-EPS) \
            #     else env.actionSpaceSample()
            action = env.select_numbers()
            # print(action)
            observation_, reward, done, info = env.step(action)
            # print('reward', reward)
            epRewards += reward
            observation = observation_

        # if EPS - 2/ numGames > 0:
        #     EPS -= 2 / numGames
        # else: 
        #     EPS = 0
        totalRewards[i] = epRewards
    
    plt.plot(totalRewards)
    plt.show()
