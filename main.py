# Import Standard Libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as mc

# Import Custom Functions
import forces
import initialconditions as IC
import boundaryconditions as BC


# This function currently uses matplotlib to draw a single frame instead of a
# continous animation. By the end we should find a better looking library than
# matplotlib.
def draw_frame(xy, radius):
    plt.rcParams["figure.figsize"] = [7.50, 5]
    num = len(xy[0])
    sizes = [radius] * num
    fig, ax = plt.subplots()
    collection = mc.CircleCollection(sizes, offsets=xy, transOffset=ax.transData, color='blue')
    ax.add_collection(collection)
    ax.margins(0.1)
    plt.show()
   

# The smoothing function is the function which allows us to find the density at all
# points in the fluid. We could use a variety of functions to do this, i have used a
# very simple one
def smoothing_function(radius, particle_distance):
    return abs(radius - particle_distance)


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


if __name__ == '__main__':
    main()