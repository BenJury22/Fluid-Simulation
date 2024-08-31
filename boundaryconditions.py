import numpy as np

def generate_BC():
    #TODO
    return 0

def apply_BC(position, velocity, boundary_conditions, time_step):
    num = len(position)
    x_bound, y_bound = boundary_conditions
    for i in range(num):
        if position[i, 0] < 0:
            velocity[i, 0] = -velocity[i, 0]
            position[i,0] = -position[i,0]
        elif position[i, 0] > x_bound:
            velocity[i, 0] = -velocity[i, 0]
            position[i, 0] = (2*x_bound) - position[i,0]

        if position[i, 1] < 0:
            velocity[i, 1] = -velocity[i, 1]
            position[i, 1] = -position[i, 1]
        elif position[i, 1] > y_bound:
            velocity[i, 1] = -velocity[i, 1]
            position[i, 1] = (2*y_bound) - position[i, 1]
            
    return position, velocity

