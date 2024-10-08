import numpy as np

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

    pos_diff = -positions[:, np.newaxis, :] + positions[np.newaxis, :, :]
    distances = np.linalg.norm(pos_diff, axis=2)

    influences = smoothing_function(smoothing_radius, distances)

    velocity_diff = -velocities[:, np.newaxis, :] + velocities[np.newaxis, :, :]

    viscosity_forces = np.sum(velocity_diff * influences[:, :, np.newaxis], axis=1)
    
    dvs = viscosity_forces * viscosity_strength
    
    return dvs


"""
Pressure
"""
def apply_pressure(positions, smoothing_radius, near_smoothing_radius, xy_bounds, pressure_strength, near_pressure_strength):
    #Pressure_dv = sum over all partciles(Pressure * direction * smoothing_grad / density)
    
    num = len(positions)
    densities, near_densities = np.array([find_density(pos, positions, smoothing_radius, near_smoothing_radius) for pos in positions]).T
    average_density = Av_density(num, xy_bounds)
    
    # Calculate all pairwise distances
    pos_diff = -positions[:, np.newaxis, :] + positions[np.newaxis, :, :]       #Calulates the distance between all of the particles
    distances = np.linalg.norm(pos_diff, axis=2)                           #Inputs these values into a matrix Particle i x Particle j
                                                                           #with the displacemnts (vectors) between the points in each element.
    np.fill_diagonal(distances, np.inf)                                        #Adds infinity to all diagonal elements 
    
    directions = pos_diff / distances[..., np.newaxis]                          #Calculates normalised direction of each element
    pressures, near_pressures = find_pressures(densities, near_densities, average_density, pressure_strength, near_pressure_strength)   #Inputs the density at each particle to find the pressure
    grads = smoothing_grad(smoothing_radius, distances)                        #Finds the smmothing grad for each element in the matrix
    
    pressure_forces = (near_pressures[:, np.newaxis] + pressures[:, np.newaxis]) * grads[..., np.newaxis] * directions / densities[:, np.newaxis, np.newaxis]
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

def find_density(sample_point, positions, smoothing_radius, near_smoothing_radius):
    distances = np.linalg.norm(positions - sample_point, axis=1)
    density = np.sum(smoothing_function(smoothing_radius, distances))
    near_density = np.sum(near_density_smoothing(near_smoothing_radius, distances))
    return density, near_density

def near_density_smoothing(smoothing_radius, dist):
    influence = (1 - (dist / smoothing_radius))**3
    influence[dist > smoothing_radius] = 0
    norm_influence = 2 * influence / (np.pi * smoothing_radius)
    return norm_influence


def find_pressures(densities, near_densities, Av_density, pressure_strength, near_pressure_strength):
    density_diff = densities - Av_density
    pressure = density_diff * pressure_strength
    near_pressure = near_densities * near_pressure_strength
    return pressure, near_pressure