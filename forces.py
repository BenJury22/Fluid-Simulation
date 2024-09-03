import numpy as np
import Density as den

"""
Gravity
"""
def apply_gravity(position, time_step, g):
    g_vector = np.array([[0, -g]])                              # Create gravity vector pointing straight down.
    return np.ones(position.shape) * g_vector * time_step       # Calculate velocity change based on gravity


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
            dist = np.linalg.norm(positions[j] - particle)
            influence = smoothing_function(smoothing_radius, dist)
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
    densities = np.array([find_density(pos, positions, smoothing_radius) for pos in positions])
    average_density = Av_density(num, xy_bounds)
    
    # Calculate all pairwise distances
    pos_diff = -positions[:, np.newaxis, :] + positions[np.newaxis, :, :]       #Calulates the distance between all of the particles
    distances = np.linalg.norm(pos_diff, axis=2)                           #Inputs these values into a matrix Particle i x Particle j
                                                                           #with the displacemnts (vectors) between the points in each element.
    np.fill_diagonal(distances, np.inf)                                        #Adds infinity to all diagonal elements 
    
    directions = pos_diff / distances[..., np.newaxis]                          #Calculates normalised direction of each element
    pressures = find_pressures(densities, average_density, pressure_strength)   #Inputs the density at each particle to find the pressure
    grads = smoothing_grad(smoothing_radius, distances)                        #Finds the smmothing grad for each element in the matrix
    
    pressure_forces = pressures[:, np.newaxis] * grads[..., np.newaxis] * directions / densities[:, np.newaxis, np.newaxis]
    total_pressure_forces = np.sum(pressure_forces, axis=1)          #Sums over contribution from each particle

    return total_pressure_forces, densities


def calculate_dist(sample_point, particle_pos):
    vector = np.array(sample_point) - np.array(particle_pos)
    dist = np.linalg.norm(vector)
    return dist

def velocity_mag(velocities):
    velocities = np.array(velocities)
    magnitudes = np.linalg.norm(velocities, axis=1)
    return magnitudes



def smoothing_function(smoothing_radius, dist):
    influence = np.maximum(smoothing_radius - dist, 0)
    norm_influence = influence / ((np.pi * smoothing_radius**3) / 3)
    return norm_influence

def smoothing_grad(smoothing_radius, distances):
    mask = (0 < distances) & (distances < smoothing_radius)
    grad = np.zeros_like(distances)
    grad[mask] = -1
    return grad
    

def Av_density(num, xy_bounds):
    x_bound, y_bound = xy_bounds
    return num / (x_bound * y_bound)

def find_density(sample_point, positions, smoothing_radius):
    distances = np.linalg.norm(positions - sample_point, axis=1)
    density = np.sum(smoothing_function(smoothing_radius, distances))
    return density

def find_pressures(densities, Av_density, pressure_strength):
    density_diff = densities - Av_density
    return density_diff * pressure_strength