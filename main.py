import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as mc


# Currently produces particles in random positions but later we could add standard presets
# e.g. all particles with constant seperation (like a lattice)
def initialise_particles(num, xy_boundaries):
    x_boundary, y_boundary = xy_boundaries
    x = x_boundary * np.random.random(num)
    y = y_boundary * np.random.random(num)
    xy = [[0 for x in range(2)] for y in range(num)]
    for i in range(num):
        xy[i][0] = x[i]
        xy[i][1] = y[i]
    return xy



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


# 

def main():
    
    num = 10
    xy_boundaries = [10, 10]
    xy = initialise_particles(num, xy_boundaries)
    print(xy)

main()