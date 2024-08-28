import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class AnimatedScatter(object):

    def __init__(self, num=500):
        self.num = num
        self.stream = self.data_stream()

        self.fig, self.ax = plt.subplots()                                      # Setup the figure and axes
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=5,    # Setup FuncAnimation (this calls setup_plot and update)
                                          init_func=self.setup_plot, blit=True)


    def setup_plot(self):
        x, y, c = next(self.stream).T                                              #Collect values from data_stream
        
        self.ax.xaxis.set_ticks([])                                                #Remove axis labels
        self.ax.yaxis.set_ticks([])
        self.scat = self.ax.scatter(x, y, c=c, s=40, vmin=0, vmax=1,                #Plot scatter graph
                                        cmap="seismic", edgecolor="k")
        self.ax.axis([-10, 15, -10, 15])

        return self.scat,
    
    def data_stream(self):
        xy = (np.random.random((self.num, 2))-0.5)*10    #Maybe incorperate IC.initialise_particles (would need to change format of output)
        c = np.random.random(self.num).T                 #Define nitial colour
        velocity = 1
        while True:
            velocity += 0.1
            xy += np.ones((self.num, 2)) * 0.001 * velocity    #Update xy positions (currently moves along y diagonal line)
            c += 0.0005 * (xy[:,0] - xy[:,1])                   #Updates colour (we may want a meaningful colour dependency)
            yield np.c_[xy[:,0], xy[:,1], c]                   #return an array of current [x, y, c] values

        
    def update(self, i):
        data = next(self.stream)                            #Collect the next timesteps set of data
        self.scat.set_offsets(data[:, :2])                  #x and y values
        self.scat.set_array(data[:, 2])                     #colour value

        return self.scat,


if __name__ == '__main__':
    a = AnimatedScatter()
    plt.show()


