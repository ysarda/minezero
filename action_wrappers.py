import torch

def ActionWrapper(action_raw,action_temp):
    action = action_temp
    action_raw = action_raw.squeeze()
    
    action['camera'] = [action_raw[2],action_raw[3]]

    if action_raw[0] >= 0.5:
        action['attack'] = 1
    if action_raw[1] >= 0.5:
        action['back'] = 1
    if action_raw[4] >= 0.5:
        action['forward'] = 1
    if action_raw[5] >= 0.5:
        action['jump'] = 1
    if action_raw[6] >= 0.5:
        action['left'] = 1
    if action_raw[7] >= 0.5:
        action['right'] = 1
    if action_raw[8] >= 0.5:
        action['sneak'] = 1
    if action_raw[9] >= 0.5:
        action['sprint'] = 1

    return action

def ActionUnwrapper(action_dict):
    action_list = list(action_dict.values())
    y,x = action_list[2]
    action_list[2] = y
    action_list.insert(3,x)
    return action_list