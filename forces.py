import numpy as np

"""
Gravity
"""
def apply_gravity(position, time_step, g):
    # Create gravity vector pointing straight down.
    g_vector = np.array([[0, -g]])

    # Calculate velocity change based on gravity
    return np.ones(position.shape) * g_vector * time_step



"""
Viscosity
"""
def apply_viscosity(positions, velocities, smoothing_radius, viscosity_strength):
    length = len(positions)
    dvs = np.zeros((length, 2))
    for i in range(length):
        particle = positions[i]
        velocity = velocities[i]
        viscosity_force = 0
        for j in range(length):
            distance = calculate_dist(particle, positions[j])
            influence = smoothing_function(smoothing_radius, distance)
            viscosity_force += (velocities[j] - velocity) * influence
        dv = viscosity_force * viscosity_strength
        dvs[i] = dv
    return dvs


"""
Pressure
"""
def apply_pressure(positions, ):
    #Pressure_dv = sum over all partciles(Pressure * direction * smoothing_grad / density)
    return 0

def calculate_dist(sample_point, particle_pos):
    vector = np.zeros((2))
    vector[0] = sample_point[0] - particle_pos[0]              #Difference in x
    vector[1] = sample_point[1] - particle_pos[1]              #Difference in y
    dist = ((vector[0])**2 + (vector[1]**2))**(1/2)
    return dist

def velocity_mag(velocities):
    velocities = np.array(velocities)
    magnitudes = np.linalg.norm(velocities, axis=1)
    return magnitudes



def smoothing_function(smoothing_radius, dist):
    influence = smoothing_radius - dist      #This function is a straight line from (x = smoothing_radius, y = 0) to (x = 0, y = smoothing radius) and back down
    if dist > smoothing_radius:
        influence = 0
    norm_influence = influence / ((np.pi * smoothing_radius**3)/3)         #Normalised by dividing by area of smoothing function (cone)
    return norm_influence

def smoothing_grad(smoothing_radius, dist):
    if -smoothing_radius < dist < 0:
        return 1
    elif 0 < dist < smoothing_radius:
        return -1
    elif dist == 0:
        return 1
    else:
        return 0
    

def Av_density(num, xy_bounds):
    x_bound, y_bound = xy_bounds
    return num / (x_bound * y_bound)

def find_pressure(density, Av_density, pressure_strength):
    density_diff = density - Av_density
    return density_diff * pressure_strength






