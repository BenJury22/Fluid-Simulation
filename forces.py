import numpy as np

"""
Gravity
"""
def apply_gravity(position, time_step, g):
    # Create gravity vector pointing straight down.
    g_vector = np.array([[0, -g]]).T

    # Calculate velocity change based on gravity
    return np.ones(position.shape) * g_vector * time_step

"""
Pressure
"""
def apply_pressure():
    #TODO
    return 0

"""
Viscosity
"""
def apply_viscosity():
    #TODO
    return 0

# The smoothing function is the function which allows us to find the density at all
# points in the fluid. We could use a variety of functions to do this, i have used a
# very simple one
def smoothing_function(radius, particle_distance):
    return abs(radius - particle_distance)

def target_density(num, xy_boundaries):
    x_boundary, y_boundary = xy_boundaries
    return num / (x_boundary * y_boundary)