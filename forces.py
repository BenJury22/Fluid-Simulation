import numpy as np

"""
Gravity
"""
def apply_gravity(position, time_step, g):
    # Create gravity vector pointing straight down and calculate velocity change
    g_vector = np.array([[0, -g]])                              
    return np.ones(position.shape) * g_vector * time_step


"""
Viscosity
"""
def apply_viscosity(positions, velocities, smoothing_radius, viscosity_strength):

    # Calculate the distance between each pair of particles
    pos_diff = -positions[:, np.newaxis, :] + positions[np.newaxis, :, :]
    distances = np.linalg.norm(pos_diff, axis=2)

    # Sum over influence from surrounding particles
    influences = smoothing_function(smoothing_radius, distances)

    # Calculate a weighted average from surrounding particles velocity and multiply by viscosity strength
    velocity_diff = -velocities[:, np.newaxis, :] + velocities[np.newaxis, :, :]
    viscosity_forces = np.sum(velocity_diff * influences[:, :, np.newaxis], axis=1)    
    dvs = viscosity_forces * viscosity_strength   
    return dvs


"""
Pressure
"""
def apply_pressure(positions, smoothing_radius, near_smoothing_radius, xy_bounds, pressure_strength, near_pressure_strength):
    num = len(positions)
    
    # Finds the average density within the bounds
    average_density = Av_density(num, xy_bounds)
    
    # Calculate the distance between each pair of particles
    pos_diff = -positions[:, np.newaxis, :] + positions[np.newaxis, :, :]
    distances = np.linalg.norm(pos_diff, axis=2)

    # Adds infinity to all diagonal elements (Avoid self-interaction)
    np.fill_diagonal(distances, np.inf)
    
    # Calculate normalised direction of each particle
    directions = pos_diff / distances[..., np.newaxis]

    # Finds density, near denisty, pressure, near_pressure and smoothing_gradient of every particle
    densities, near_densities = np.array([find_density(pos, positions, smoothing_radius, near_smoothing_radius) for pos in positions]).T
    pressures, near_pressures = find_pressures(densities, near_densities, average_density, pressure_strength, near_pressure_strength)
    grads = smoothing_grad(smoothing_radius, distances)
    
    # Calculate the pressure force on each particle
    pressure_forces = (near_pressures[:, np.newaxis] + pressures[:, np.newaxis]) * grads[..., np.newaxis] * directions / densities[:, np.newaxis, np.newaxis]
    total_pressure_forces = np.sum(pressure_forces, axis=1)
    return total_pressure_forces

# Linear smoothing function to calculate the weight of contribution of each surrounding particle
def smoothing_function(smoothing_radius, dist):
    influence = np.maximum(smoothing_radius - dist, 0)
    norm_influence = influence / ((np.pi * smoothing_radius**3) / 3)
    return norm_influence

# Gradient of the smoothing function
def smoothing_grad(smoothing_radius, distances):
    mask = (0 < distances) & (distances < smoothing_radius)
    grad = np.zeros_like(distances)
    grad[mask] = -1
    return grad
    
# Calculates the avergae density within the bounds
def Av_density(num, xy_bounds):
    x_bound, y_bound = xy_bounds
    return num / (x_bound * y_bound)

# Calculates the densities and near densities at every particle position
def find_density(sample_point, positions, smoothing_radius, near_smoothing_radius):
    distances = np.linalg.norm(positions - sample_point, axis=1)
    density = np.sum(smoothing_function(smoothing_radius, distances))
    near_density = np.sum(near_density_smoothing(near_smoothing_radius, distances))
    return density, near_density

# Different smoothing function for near densities
def near_density_smoothing(smoothing_radius, dist):
    influence = (1 - (dist / smoothing_radius))**3
    influence[dist > smoothing_radius] = 0
    norm_influence = 2 * influence / (np.pi * smoothing_radius)
    return norm_influence

# Calculates the densities and near densities at every particle position (near_pressure is purely repulsive)
def find_pressures(densities, near_densities, Av_density, pressure_strength, near_pressure_strength):
    density_diff = densities - Av_density
    pressure = density_diff * pressure_strength
    near_pressure = near_densities * near_pressure_strength
    return pressure, near_pressure