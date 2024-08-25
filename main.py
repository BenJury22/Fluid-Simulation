# Import Standard Libraries
import numpy as np

# Import Custom Functions
import forces
import initialconditions as IC
import boundaryconditions as BC
import customanimation as an


def main():
    # Hard coded variables, to later be replaced by GUI or parameter file.
    # Time Variables
    time_step = 0.1
    frame_number = 1001

    # Force Variables 
    g = 9.91 # Acceleration due to gravity ms^-2

    # IC & BC variables
    num = 10
    xy_boundaries = [10, 10]

    # Generate Initial Conditions
    position = IC.initialise_particles(num, xy_boundaries)
    velocity = IC.initialise_velocity()

    # Generate Boundary Conditions
    BC = BC.generate_BC()

    # Run simulation
    times = np.arange(0, frame_number) * time_step
    for idt, t in enumerate(times):
        # Calculate changes in velocity due to forces
        gravity_dv = forces.apply_gravity(velocity, time_step, g)
        pressure_dv = forces.apply_pressure()
        viscosity_dv = forces.apply_viscosity()

        # Calculate new velocity and position
        velocity += gravity_dv + pressure_dv + viscosity_dv
        position += velocity * time_step

        # Apply boundary conditions
        position, velocity = BC.apply_BC(position, velocity, BC)

        # Plotting
        # TODO create and run plotting/animation function.
        an.draw_frame()


if __name__ == '__main__':
    main()