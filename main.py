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
    time_step = 0.1
    frame_number = 1001

    # Force Variables
    phys_constants = {"g": 9.81}
    g = 9.81 # Acceleration due to gravity ms^-2

    # IC & BC variables
    num = 10
    xy_boundaries = [10, 10]

    # Generate Initial Conditions
    initial_position = IC.initialise_particles(num, xy_boundaries)
    initial_velocity = IC.initialise_velocity()

    # Generate Boundary Conditions
    boundary_conditions = BC.generate_BC()

    # Plotting
    # TODO create and run plotting/animation function.
    Animation = an.AnimatedScatter(num=500, data_stream_func=new_pos, 
                    cmap="hot", point_size=50, 
                    xlim=(-0, xy_boundaries[0]), ylim=(0, xy_boundaries[1]), 
                    interval=5,
                    time_steps=time_step,
                    position=initial_position,
                    velocity=initial_velocity,
                    phys_constants=phys_constants,
                    boundary_conditions=boundary_conditions)
    
    plt.show()

def initilise():
    # Initialise simulation
    pass

def new_pos(time_step=None, position=None, velocity=None, phys_constants=None, boundary_conditions=None):
    while True:
        # Calculate changes in velocity due to forces
        gravity_dv = forces.apply_gravity(position, time_step, phys_constants["g"])
        pressure_dv = forces.apply_pressure()
        viscosity_dv = forces.apply_viscosity()

        # Calculate new velocity and position
        velocity += gravity_dv + pressure_dv + viscosity_dv
        position += velocity * time_step

        # Apply boundary conditions
        # position, velocity = BC.apply_BC(position, velocity, boundary_conditions)

        yield np.c_[position[:,0], position[:,1], position[:,1]] 




if __name__ == '__main__':
    main()