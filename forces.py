def apply_gravity(dt, veloctiy):
    # Calculate velocity change based on gravity
    dv = 0
    return dv

def apply_pressure():
    #TODO
    return 0

def apply_viscosity():
    #TODO
    return 0

# The smoothing function is the function which allows us to find the density at all
# points in the fluid. We could use a variety of functions to do this, i have used a
# very simple one
def smoothing_function(radius, particle_distance):
    return abs(radius - particle_distance)