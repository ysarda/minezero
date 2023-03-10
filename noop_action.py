import minerl
import gym
env = gym.make('MineRLNavigateDense-v0')
env.make_interactive(port=6666, realtime=True)


obs  = env.reset()
done = False

while not done:
    action = env.action_space.noop()

    action['camera'] = [0, 0.03*obs["compassAngle"]]
    action['back'] = 0
    action['forward'] = 1
    action['jump'] = 1
    action['attack'] = 1

    obs, reward, done, info = env.step(action)