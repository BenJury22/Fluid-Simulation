import numpy as np
import initialconditions as IC
import matplotlib.pyplot as plt
import time

def calculate_dist(sample_point, particle_pos):
    vector = np.zeros((2))
    vector[0] = sample_point[0] - particle_pos[0]
    vector[1] = sample_point[1] - particle_pos[1]
    dist = ((vector[0])**2 + (vector[1]**2))**(1/2)
    return dist


def smoothing_function(smoothing_radius, dist):
    influence = smoothing_radius - dist
    if dist > smoothing_radius:
        influence = 0
    norm_influence = influence / ((np.pi * smoothing_radius**3)/3)
    return norm_influence


def find_density(sample_point, position, smoothing_radius):
    influence = 0
    for i in range(len(position)):
        dist = calculate_dist(sample_point, position[i])
        influence += smoothing_function(smoothing_radius, dist)
    return influence                                               #Need to normalise by dividing by the area of the smoothing function


def plot_graph(position, sample_point):
    full_list = np.vstack((position, sample_point))
    length = len(full_list)
    c = np.zeros((length))
    c[length - 1] = 1
    plt.scatter(full_list[:,0], full_list[:,1], s=40, c=c, cmap="rainbow", edgecolor="None")
    plt.show()

def calculate_target_density(num, xy_boundaries):
    x_bound, y_bound = xy_boundaries
    return num / (x_bound * y_bound)



def main():
    start_time = time.process_time()

    num = 1000
    xy_boundaries = [10, 10]
    position = IC.initialise_particles(num, xy_boundaries)
    sample_position = [5, 5]
    smoothing_radius = 1
    x = find_density(sample_position, position, smoothing_radius)
    print(x)

    plot_graph(position, sample_position)

    end_time = time.process_time()
    print(f"CPU time used: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()

