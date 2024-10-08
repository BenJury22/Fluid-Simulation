import numpy as np

# Currently produces particles in random positions but later we could add standard presets
# e.g. all particles with constant seperation (like a lattice)
def initialise_particles(num, xy_boundaries):
    xy = np.random.rand(num, 2) * xy_boundaries
    return xy

def initialise_velocity(num, xy_max_v, mean_velocity):
    xy_v = (np.random.rand(num, 2) - 0.5) * xy_max_v
    return xy_v + mean_velocity