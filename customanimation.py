import matplotlib.pyplot as plt
import matplotlib.collections as mc

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