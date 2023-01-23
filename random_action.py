import minerl
import gym
env = gym.make('MineRLNavigateDense-v0')
env.make_interactive(port=6666, realtime=True)

obs = env.reset()

done = False
while not done:
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)

