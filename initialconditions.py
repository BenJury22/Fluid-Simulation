import numpy as np

# Currently produces particles in random positions but later we could add standard presets
# e.g. all particles with constant seperation (like a lattice)
def initialise_particles(num, xy_boundaries):
    # Creates a 2 by num numpy array containing the
    x_boundary, y_boundary = xy_boundaries
    x = x_boundary * np.random.random(num)
    y = y_boundary * np.random.random(num)
    xy = [[0 for x in range(2)] for y in range(num)]
    for i in range(num):
        xy[i][0] = x[i]
        xy[i][1] = y[i]
    return xy

def initialise_velocity():
    #TODO create function that initialises velocities.
    return 0