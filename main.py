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
    # Time variables
    time_step = 0.01

    # Force variables
    phys_constants = {"Gravitational_Acceleration": 9.81, "Viscosity_Strength": 0.1, "Pressure_Strength": 1, "Near_Pressure_Strength": 1}

    # IC & BC variables
    num = 800
    xy_boundaries = [20, 10]
    velocity_variation = [5, 5]
    mean_velocity = [0, 0]
    particle_spawn_boundaries = [[5, 15], [3, 7]]

    # Smoothing parameters
    smoothing_radius = 0.5
    near_smoothing_radius = 0.2

    # Generate initial conditions
    initial_position = IC.initialise_particles(num, particle_spawn_boundaries)
    initial_velocity = IC.initialise_velocity(num, velocity_variation, mean_velocity)

    # Initialise UI
    root = tk.Tk()
    root.geometry("1500x900")
    root.title("Fluid Simulation")

    # Create UI constnats label
    for key, value in phys_constants.items():
        label = tk.Label(root, text=f"{key} = {value}", font = ('arial', 14))
        label.pack()

    # Run simulation and animation
    Animation = an.AnimatedScatter(data_stream_func=new_pos, root = root,
                    cmap="rainbow", point_size=30, 
                    xlim=(0, xy_boundaries[0]), ylim=(0, xy_boundaries[1]), 
                    interval=20,
                    time_steps=time_step,
                    position=initial_position,
                    velocity=initial_velocity,
                    phys_constants=phys_constants,
                    boundary_conditions=xy_boundaries,
                    smoothing_radius = smoothing_radius,
                    near_smoothing_radius = near_smoothing_radius)

    # End UI loop
    root.mainloop()


def new_pos(time_steps=0, position=0, velocity=0, phys_constants=0, boundary_conditions=0, smoothing_radius = 0, near_smoothing_radius = 0):
    # Calculates next frame of simulation and yield result
    while True:
        # Calculate changes in velocity due to forces
        gravity_dv = forces.apply_gravity(position, time_steps, phys_constants["Gravitational_Acceleration"])
        pressure_dv = forces.apply_pressure(position, smoothing_radius, near_smoothing_radius, boundary_conditions,
                                                       phys_constants["Pressure_Strength"], phys_constants["Near_Pressure_Strength"])     
        viscosity_dv = forces.apply_viscosity(position, velocity, smoothing_radius, phys_constants["Viscosity_Strength"])

        # Calculate new velocity and position
        velocity +=  pressure_dv + gravity_dv + viscosity_dv
        position += velocity * time_steps

        # Apply boundary conditions
        position, velocity = BC.apply_BC(position, velocity, boundary_conditions)

        # Define colour dependent on speed
        c = np.linalg.norm(velocity, axis=1)
    
        yield np.c_[position[:,0], position[:,1], c/6] 


if __name__ == '__main__':
    main()