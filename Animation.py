import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class AnimatedScatter(object):

    def __init__(self, num=500, data_stream_func=None, cmap="seismic", 
                 point_size=40, xlim=(-10, 15), ylim=(-10, 15), interval=5, **kwargs):
        self.num = num
        self.stream = data_stream_func(self.num, **kwargs) if data_stream_func else self.data_stream()

        self.cmap = cmap
        self.point_size = point_size
        self.xlim = xlim
        self.ylim = ylim
        self.interval = interval

        self.fig, self.ax = plt.subplots()                                      # Setup the figure and axes
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=self.interval,    # Setup FuncAnimation (this calls setup_plot and update)
                                          init_func=self.setup_plot, blit=None)

    def setup_plot(self):
        x, y, c = next(self.stream).T                                              #Collect values from data_stream
        
        self.ax.xaxis.set_ticks([])                                                #Remove axis labels
        self.ax.yaxis.set_ticks([])
        self.scat = self.ax.scatter(x, y, c=c, s=self.point_size, vmin=0, vmax=1,    # Plot scatter graph
                                    cmap=self.cmap, edgecolor="k")
        self.ax.axis([self.xlim[0], self.xlim[1], self.ylim[0], self.ylim[1]])
        return self.scat,


    def update(self, i):
        data = next(self.stream)                            #Collect the next timesteps set of data
        self.scat.set_offsets(data[:, :2])                  #x and y values
        self.scat.set_array(data[:, 2])                     #colour value

        return self.scat,




