import numpy as np

# Currently produces particles in random positions but later we could add standard presets
# e.g. all particles with constant seperation (like a lattice)
def initialise_particles(num, xy_boundaries):
    x_boundary, y_boundary = xy_boundaries
    xy = np.random.rand(num, 2)
    xy[:, 0] *= x_boundary
    xy[:, 1] *= y_boundary
    return xy

def initialise_velocity(num, xy_max_v):
    x_max, y_max = xy_max_v
    xy_v = np.random.rand(num, 2) - 0.5
    xy_v[:, 0] *= x_max
    xy_v[:, 1] *= y_max
    return xy_v