# Import Standard Libraries
import numpy as np
import matplotlib.pyplot as plt

# Import Custom Functions
import forces
import initialconditions as IC
import boundaryconditions as BC
import Animation as an


def main():
    # Hard coded variables, to later be replaced by GUI or parameter file.
    # Time Variables
    time_step = 0.01

    # Force Variables
    phys_constants = {"g": 9.81}

    # IC & BC variables
    num = 80
    xy_boundaries = [10, 10]
    xy_max_v = [5, 5]
    smoothing_radius = 2
    viscosity_strength = 0.001

    # Generate Initial Conditions
    initial_position = IC.initialise_particles(num, xy_boundaries)
    initial_velocity = IC.initialise_velocity(num, xy_max_v)

    # Generate Boundary Conditions
    #boundary_conditions = BC.generate_BC()

    # Plotting
    # TODO create and run plotting/animation function.
    Animation = an.AnimatedScatter(data_stream_func=new_pos, 
                    cmap="seismic", point_size=50, 
                    xlim=(0, xy_boundaries[0]), ylim=(0, xy_boundaries[1]), 
                    interval=20,
                    time_steps=time_step,
                    position=initial_position,
                    velocity=initial_velocity,
                    phys_constants=phys_constants,
                    boundary_conditions=xy_boundaries,
                    smoothing_radius = smoothing_radius,
                    viscosity_strength = viscosity_strength)
    
    plt.show()

def initilise():
    # Initialise simulation
    pass

def new_pos(time_steps=0, position=0, velocity=0, phys_constants=0, boundary_conditions=0, smoothing_radius = 0, viscosity_strength = 0):
    while True:
        # Calculate changes in velocity due to forces
        gravity_dv = forces.apply_gravity(position, time_steps, phys_constants["g"])
        pressure_dv, densities = forces.apply_pressure(position, smoothing_radius, boundary_conditions, 0.2)     
        viscosity_dv = forces.apply_viscosity(position, velocity, smoothing_radius, viscosity_strength)

        # Calculate new velocity and position
        velocity += pressure_dv
        position += velocity * time_steps

        # Apply boundary conditions
        position, velocity = BC.apply_BC(position, velocity, boundary_conditions, time_steps)

        average_density = forces.Av_density(len(position), boundary_conditions)
        c = densities / average_density

        yield np.c_[position[:,0], position[:,1], c/3] 




if __name__ == '__main__':
    main()