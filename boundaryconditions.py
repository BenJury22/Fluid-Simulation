# Apply rectangular boundary conditions to particles
def apply_BC(position, velocity, boundary_conditions):
    x_bound, y_bound = boundary_conditions
    
    # Reflect positions and velocities at x boundary
    mask_x_low = position[:, 0] < 0
    mask_x_high = position[:, 0] > x_bound
    
    velocity[mask_x_low | mask_x_high, 0] *= -1
    position[mask_x_low, 0] *= -1
    position[mask_x_high, 0] = 2 * x_bound - position[mask_x_high, 0]

    # Reflect positions and velocities at y boundary
    mask_y_low = position[:, 1] < 0
    mask_y_high = position[:, 1] > y_bound
    
    velocity[mask_y_low | mask_y_high, 1] *= -1
    position[mask_y_low, 1] *= -1
    position[mask_y_high, 1] = 2 * y_bound - position[mask_y_high, 1]
    
    return position, velocity

