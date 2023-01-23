import minerl
import gym
import torch
import torch.nn as nn
import torch.optim as optim

import matplotlib.pyplot as plt

import numpy as np

from collections import deque 

from model import Agent
from action_wrappers import ActionWrapper as AW 

env = gym.make('MineRLTreechop-v0')
#env.make_interactive(port=6666, realtime=True)


agent = Agent(state_size=56*56,action_size=11,seed=0)


def dqn(n_episodes= 200, eps_start=1.0, eps_end = 0.1, eps_decay=0.999):
    scores = [] 
    scores_window = deque(maxlen=100) 
    eps = eps_start
    for i_episode in range(1, n_episodes+1):
        state_dict = env.reset()
        state = torch.tensor(state_dict['pov'])
        score = 0
        done = False
        while not done:
            action_template = env.action_space.noop()
            action_raw = agent.act(state,eps)
            action = AW(action_raw, action_template)
            next_state_dict,reward,done,_ = env.step(action)
            next_state = torch.tensor(next_state_dict['pov'])
            agent.step(state,action_raw,reward,next_state,done)

            state = next_state
            score += reward
            scores_window.append(score)
            scores.append(score) 
            eps = max(eps*eps_decay,eps_end)
            print('\rEpisode {}\tAverage Score {:.2f}'.format(i_episode,np.mean(scores_window)), end="")
            
            if np.mean(scores_window)>=200.0:
                print('\nEnvironment solve in {:d} epsiodes!\tAverage score: {:.2f}'.format(i_episode-100, np.mean(scores_window)))
                torch.save(agent.qnetwork_local.state_dict(),'checkpoint.pth')
                break
    return scores

scores = dqn()

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(np.arange(len(scores)),scores)
plt.ylabel('Score')
plt.xlabel('Epsiode #')
plt.show()

