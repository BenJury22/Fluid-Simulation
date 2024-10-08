import numpy as np

# Produces particles in random positions
def initialise_particles(num, particle_boundaries):
    x_min, x_max = particle_boundaries[0]
    y_min, y_max = particle_boundaries[1]

    x_values = np.random.rand(num) * (x_max - x_min) + x_min
    y_values = np.random.rand(num) * (y_max - y_min) + y_min

    xy = np.vstack((x_values, y_values)).T
    return xy

# Produces particles with random positions
def initialise_velocity(num, xy_max_v, mean_velocity):
    xy_v = (np.random.rand(num, 2) - 0.5) * xy_max_v
    return xy_v + mean_velocity