import numpy as np

def generate_BC():
    #TODO
    return 0

def apply_BC(position, velocity, boundary_conditions, time_step):
    num = len(position)
    x_bound, y_bound = boundary_conditions
    new_pos = np.zeros((num, 2))
    for i in range(num):
        new_pos[i] = position[i] + velocity[i] * time_step
        if new_pos[i, 0] < 0 or new_pos[i, 0] > x_bound:
            velocity[i, 0] = -velocity[i, 0]
            position[i, 0] += velocity[i, 1] * time_step
        if new_pos[i, 1] < 0 or new_pos[i, 1] > y_bound:
            velocity[i, 1] = -velocity[i, 1]
            position[i, 1] += velocity[i, 0] * time_step 
    return position, velocity

