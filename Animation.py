import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, colors, colormaps

def initialise_particles(num, xy_boundaries):
    x_boundary, y_boundary = xy_boundaries
    x = x_boundary * np.random.random(num)
    y = y_boundary * np.random.random(num)
    xy = np.zeros((num, 2))
    for i in range(num):
        xy[i][0] = x[i]
        xy[i][1] = y[i]
    return xy


def plot(xy, xy_boundary):
    fig = plt.figure()
    scatter = plt.scatter(xy[:, 0], xy[:, 1], s = 40, c = 'lime')
    axs = fig.get_axes()
    x_bound, y_bound = xy_boundary
    axs[0].set_xlim(0, x_bound)
    axs[0].set_ylim(0, y_bound)

    plt.show()


def simulate_steps():
    return 0


def main():
    num = 3
    xy_boundaries = [10, 10]
    xy = initialise_particles(num, xy_boundaries)
    print(xy)
    print()
    print(xy[:, 0])                       #This is equal to x
    print(xy[:, 1])                       #This is equal to y
    print()
    
    plot(xy, xy_boundaries)



if __name__ == "__main__":
    main()


