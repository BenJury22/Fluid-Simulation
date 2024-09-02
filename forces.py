import numpy as np
import Density as den

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
    num = len(positions)
    dvs = np.zeros((num, 2))
    for i in range(num):
        particle = positions[i]
        velocity = velocities[i]
        viscosity_force = 0
        for j in range(num):
            influence = smoothing_function_test(smoothing_radius, particle, positions[j])
            viscosity_force += (velocities[j] - velocity) * influence
        dv = viscosity_force * viscosity_strength
        dvs[i] = dv
    return dvs


"""
Pressure
"""
def apply_pressure(positions, smoothing_radius, xy_bounds, pressure_strength):
    #Pressure_dv = sum over all partciles(Pressure * direction * smoothing_grad / density)
    num = len(positions)
    dvs = np.zeros((num, 2))
    densities = np.zeros((num))
    average_density = Av_density(num, xy_bounds)
    for i in range(num):
        densities[i] = find_density(positions[i], positions, smoothing_radius)
    for i in range(num):
        pressure_force = 0
        for j in range(num):
            if j == i:
                continue
            density = densities[j]
            pressure = find_pressure(density, average_density, pressure_strength)
            distance = calculate_dist(positions[i], positions[j])
            direction = (positions[j] - positions[i]) / distance
            grad = smoothing_grad_test(smoothing_radius, positions[i], positions[j])
            pressure_force += pressure * grad * direction / density
        dvs[i] = pressure_force
    return dvs, densities

            
    return 0

def calculate_dist(sample_point, particle_pos):
    vector = np.array(sample_point) - np.array(particle_pos)
    dist = np.linalg.norm(vector)
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
    if 0 < dist < smoothing_radius:
        return -1
    return 0
    

def Av_density(num, xy_bounds):
    x_bound, y_bound = xy_bounds
    return num / (x_bound * y_bound)

def find_density(sample_point, position, smoothing_radius):
    influence = 0
    for i in range(len(position)):
        influence += smoothing_function_test(smoothing_radius, sample_point, position[i])
    return influence

def find_pressure(density, Av_density, pressure_strength):
    density_diff = density - Av_density
    return density_diff * pressure_strength

def smoothing_grad_test(smoothing_radius, sample_point, particle):
    if  sample_point[0] - smoothing_radius < particle[0] < sample_point[0] + smoothing_radius and sample_point[1] - smoothing_radius < particle[1] < sample_point[1] +smoothing_radius:
        return -1
    return 0

def smoothing_function_test(smoothing_radius, sample_point, particle):
        if  sample_point[0] - smoothing_radius < particle[0] < sample_point[0] + smoothing_radius and sample_point[1] - smoothing_radius < particle[1] < sample_point[1] +smoothing_radius:
            vector = np.array(sample_point) - np.array(particle)
            dist = np.linalg.norm(vector)
            influence = smoothing_radius - dist
            return influence / ((np.pi * smoothing_radius**3)/3)
        return 0