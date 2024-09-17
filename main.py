# Import Standard Libraries
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

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
    phys_constants = {"Gravitational_Acceleration": 9.81, "Viscosity_Strength": 0.001, "Pressure_Strength": 1}

    # IC & BC variables
    num = 500
    xy_boundaries = [10, 10]
    xy_max_v = [5, 5]
    smoothing_radius = 0.5


    # Generate Initial Conditions
    initial_position = IC.initialise_particles(num, xy_boundaries)
    initial_velocity = IC.initialise_velocity(num, xy_max_v)

    root = tk.Tk()
    root.geometry("1500x900")
    root.title("Fluid Simulation")

    for key, value in phys_constants.items():
        label = tk.Label(root, text=f"{key} = {value}", font = ('arial', 14))
        label.pack()

    Animation = an.AnimatedScatter(data_stream_func=new_pos, root = root,
                    cmap="rainbow", point_size=30, 
                    xlim=(0, xy_boundaries[0]), ylim=(0, xy_boundaries[1]), 
                    interval=20,
                    time_steps=time_step,
                    position=initial_position,
                    velocity=initial_velocity,
                    phys_constants=phys_constants,
                    boundary_conditions=xy_boundaries,
                    smoothing_radius = smoothing_radius)

    root.mainloop()

def new_pos(time_steps=0, position=0, velocity=0, phys_constants=0, boundary_conditions=0, smoothing_radius = 0):
    while True:
        # Calculate changes in velocity due to forces
        gravity_dv = forces.apply_gravity(position, time_steps, phys_constants["Gravitational_Acceleration"])
        pressure_dv, densities = forces.apply_pressure(position, smoothing_radius, boundary_conditions, phys_constants["Pressure_Strength"])     
        viscosity_dv = forces.apply_viscosity(position, velocity, smoothing_radius, phys_constants["Viscosity_Strength"])

        # Calculate new velocity and position
        velocity +=  pressure_dv + gravity_dv + viscosity_dv
        position += velocity * time_steps

        # Apply boundary conditions
        position, velocity = BC.apply_BC(position, velocity, boundary_conditions)

        # Finding colour (dependent on density)

#         average_density = forces.Av_density(len(position), boundary_conditions)
#         c = densities / average_density

        # Finding Colour (dependent on speed)
        c = forces.velocity_mag(velocity)
    

        yield np.c_[position[:,0], position[:,1], c/10] 


if __name__ == '__main__':
    main()