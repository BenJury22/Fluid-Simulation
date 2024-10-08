import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AnimatedScatter(object):

    def __init__(self, root, num=500, data_stream_func=None, cmap="seismic", 
                 point_size=40, xlim=(-10, 10), ylim=(-10, 10), interval=5, time_steps = 0.1, **kwargs):
        
        #Initialise constants and parameters
        self.num = num
        self.data_stream_func = data_stream_func
        self.cmap = cmap
        self.point_size = point_size
        self.xlim = xlim
        self.ylim = ylim
        self.interval = interval

        self.root = root
        self.running = True

        self.kwargs = kwargs
        self.initial_timestep = time_steps
        self.current_timestep = self.initial_timestep
        self.stream = self.data_stream_func(time_steps=self.current_timestep, **kwargs)

        #Initialise Figure with axes
        self.fig, self.ax = plt.subplots()

        #Initialise UI in Figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        #Call Button Function
        self.Play_button = tk.Button(self.root, text = "Play", command = self.play)
        self.Play_button.pack(side = tk.LEFT)

        #Call Button Function
        self.Pause_button = tk.Button(self.root, text = "Pause", command = self.pause)
        self.Pause_button.pack(side = tk.LEFT)

        #Call function which plays and pauses the simulation (both with space bar)
        self.root.bind("<space>", self.play_pause)

        #Call speed x1 function
        self.x1_button = tk.Button(self.root, text = "x1", command = self.speed_x1)
        self.x1_button.pack(side = tk.LEFT)

        #Call speed x2 function
        self.x2_button = tk.Button(self.root, text = "x2", command = self.speed_x2)
        self.x2_button.pack(side = tk.LEFT)

        #Call speed x4 function
        self.x4_button = tk.Button(self.root, text = "x4", command = self.speed_x4)
        self.x4_button.pack(side = tk.LEFT)

        #Runs animation
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=self.interval,    # Setup FuncAnimation (this calls setup_plot and update)
                                          init_func=self.setup_plot, blit=None)


    #Plots each frame
    def setup_plot(self):

        #Collect values from data_stream
        x, y, c = next(self.stream).T
        
        #Remove axis labels
        self.ax.xaxis.set_ticks([])
        self.ax.yaxis.set_ticks([])

        #Set colour of axes
        self.ax.spines['bottom'].set_color('pink')
        self.ax.spines['top'].set_color('pink')
        self.ax.spines['right'].set_color('pink')
        self.ax.spines['left'].set_color('pink')

        #Set colour of the edges of circles
        self.ax.set_facecolor('k')
        self.fig.patch.set_facecolor('k')

        #Draws frame
        self.scat = self.ax.scatter(x, y, c=c, s=self.point_size, vmin=0, vmax=1,
                                    cmap=self.cmap, edgecolor="None")
        self.ax.axis([self.xlim[0], self.xlim[1], self.ylim[0], self.ylim[1]])

        return self.scat,


    #Collects data and checks whether the simulation has been paused
    def update(self, i):
        if not self.running:
            return self.scat
        data = next(self.stream)                       
        self.scat.set_offsets(data[:, :2])
        self.scat.set_array(data[:, 2])

        return self.scat,

    
    
    #Restarts animation if play button is pressed
    def play(self):
        self.running = True
    
    #Stops animation if pause button is pressed
    def pause(self):
        self.running = False

    #Starts/stops the animation if space bar is pressed
    def play_pause(self, event = None):
        self.running = not self.running

    #Makes the timestep equal to its initial value
    def speed_x1(self):
        self.current_timestep = self.initial_timestep * 1
        self.update_timestep()
    
    #Makes the timestep double its initial value
    def speed_x2(self):
        self.current_timestep = self.initial_timestep * 2
        self.update_timestep()
    
    #Makes the timestep 4 times its initial value
    def speed_x4(self):
        self.current_timestep = self.initial_timestep * 4
        self.update_timestep()
    
    #Applies the new timestep to the simulation
    def update_timestep(self):
        self.stream = self.data_stream_func(time_steps=self.current_timestep, **self.kwargs)
        self.ani.event_source.start()


