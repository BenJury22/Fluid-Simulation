import numpy as np

# Produces particles in random positions
def initialise_particles(num, xy_boundaries):
    xy = np.random.rand(num, 2) * xy_boundaries
    return xy

# Produces particles with random positions
def initialise_velocity(num, xy_max_v):
    xy_v = (np.random.rand(num, 2) - 0.5) * xy_max_v
    return xy_v