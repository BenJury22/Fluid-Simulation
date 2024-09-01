import numpy as np
import initialconditions as IC
import matplotlib.pyplot as plt
import time
import forces



def find_density(sample_point, position, smoothing_radius):
    influence = 0
    for i in range(len(position)):
        dist = forces.calculate_dist(sample_point, position[i])
        influence += forces.smoothing_function(smoothing_radius, dist)
    return influence


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

    num = 100
    xy_boundaries = [10, 10]
    position = IC.initialise_particles(num, xy_boundaries)
    sample_position = [5, 5]
    smoothing_radius = 1

    start_time = time.process_time()
    x = find_density(position[0], position, smoothing_radius)
    print(x)

    plot_graph(position, sample_position)

    end_time = time.process_time()
    print(f"CPU time used: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()

