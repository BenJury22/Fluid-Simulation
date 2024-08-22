import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as mc

def generate_circles(num, max_position):
    xy = max_position * np.random.random((num, 2))
    return xy
    
def draw_circles(xy, radius):
    
    plt.rcParams["figure.figsize"] = [7.50, 5]
#    plt.rcParams["figure.autolayout"] = True
    
    num = len(xy[0])
    sizes = [radius] * num
    fig, ax = plt.subplots()
    collection = mc.CircleCollection(sizes, offsets=xy, transOffset=ax.transData, color='blue')
    ax.add_collection(collection)
    ax.margins(0.1)
    plt.show()
    
def gravity(num, radius, max_position, g, dt, time_steps):
    velocity = [[0 for x in range(num)] for y in range(time_steps)]
    xy = generate_circles(num, max_position)
    y = [[0 for x in range(num)] for y in range(time_steps)]
    for j in range(num):
        y[0][j] = xy[j][1]
    for i in range(time_steps - 1):
        for j in range(num):
            velocity[i + 1][j] = velocity[i][j] - g * dt
            y[i + 1][j] = y[i][j] + velocity[i][j] * dt      
    return velocity, y

    
def main():
    num = 10
    radius = 50
    max_position = 10
    g = 9.8
    dt = 0.1
    time_steps = 10
    
    xy = generate_circles(num, max_position)
    velocity, y = gravity(num, radius, max_position, g, dt, time_steps)
    draw_circles(xy, radius)    
    print("Initial Co-ordinates:", xy)
    print()
    print("Velocities:", velocity)
    print()
    print("y Positions:", y)
    
main()