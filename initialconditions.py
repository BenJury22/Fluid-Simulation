import numpy as np

# Currently produces particles in random positions but later we could add standard presets
# e.g. all particles with constant seperation (like a lattice)
def initialise_particles(num, xy_boundaries):
    x_boundary, y_boundary = xy_boundaries
    x = x_boundary * np.random.random(num)
    y = y_boundary * np.random.random(num)
    xy = np.zeros((num, 2))
    for i in range(num):
        xy[i][0] = x[i]
        xy[i][1] = y[i]
    return xy

def initialise_velocity():
    #TODO create function that initialises velocities.
    return 0