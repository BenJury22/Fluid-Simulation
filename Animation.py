import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, colors, colormaps
import initialconditions as IC

def draw_frame(xy, xy_boundary):
    fig = plt.figure()
    scatter = plt.scatter(xy[:, 0], xy[:, 1], s = 40, c = 'lime')
    axs = fig.get_axes()
    x_bound, y_bound = xy_boundary
    axs[0].set_xlim(0, x_bound)
    axs[0].set_ylim(0, y_bound)

    plt.show()

#Arbitrary function at the moment
def simulate_steps(initial_pos, velocity, dt, time_steps):
    num = len(initial_pos)
    x = np.zeros((time_steps, num))
    y = np.zeros((time_steps, num))
    x[0, :] = initial_pos[:, 0]
    y[0, :] = initial_pos[:, 1]
    for i in range(time_steps - 1):
        x[i + 1] = x[i] + velocity * dt
        y[i + 1] = y[i]
    return x, y

def test_animate():
    num = 3
    xy_boundaries = [10, 10]
    xy = IC.initialise_particles(num, xy_boundaries)
    print(xy)

    velocity = 1
    dt = 0.01
    time_steps = 10
    x, y = simulate_steps(xy, velocity, dt, time_steps)
    print(x)
    print(y)

    draw_frame(xy, xy_boundaries)
    




if __name__ == "__main__":
    test_animate()


