import minerl
import gym
from env_wrappers import continousEnv

env = continousEnv('missions/treechop.xml')
#env.make_interactive(port=6666, realtime=True)

obs = env.reset()

done = False
while not done:
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)

