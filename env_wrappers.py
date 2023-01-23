import minerl
import torch
import numpy as np
import gym

class continousEnv(minerl.env.core.MineRLEnv):
    def __init__(self, xml):
        super().__init__(
            xml,
            gym.spaces.Box(low=0, high=255, shape=(64, 64, 3), dtype=np.uint8),
            gym.spaces.Box(low=-1, high=1, shape=(5,), dtype=np.uint8),
            None
        )
    def _setup_spaces(self, observation_space, action_space):
        self.observation_space = observation_space
        self.action_space = action_space

    def _process_action(self, action_in) -> str:
        a = action_in
        command_array = [f'move {a[0]}', f'jump {a[1]}', f'attack {a[2]}', f'camera {a[3]} {a[4]}'] 

        print("\n".join(command_array), "\n")
        return "\n".join(command_array)

    def _process_observation(self, pov, info):

        pov = np.frombuffer(pov, dtype=np.uint8)
        pov = pov.reshape((self.height, self.width, self.depth))
        return pov