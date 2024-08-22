import matplotlib.pyplot as plt
import numpy as np

def AvTemp(T, E, R = 2.912, Q = 342, a = 0.3, b = 5.67 * pow(10, -8)):
    T_dot = (1/R) * ((Q*(1-a)) - E*b*T**4)
    return T_dot

def EquilTemp(E, T, dt):
    for i in range(len(T) - 1):
        T[i + 1] = T[i] + AvTemp(T[i], E) * dt
    GradFinal = (T[-1] - T[-2])/dt
    return T[-1], GradFinal

def Plot_T_Dependence(T, Time):
    plt.figure()
    plt.xlabel('Year')
    plt.ylabel('Temperature')
    plt.plot(Time, T - 273)

def Plot_E_Dependence(E, T_Final):
    plt.figure()
    plt.xlabel('Emissivity')
    plt.ylabel('Equilibrium Temperature')
    plt.plot(E, T_Final - 273)
    
def Plot_FinalGrad(E, GradFinal):
    plt.figure()
    plt.xlabel('Emissivity')
    plt.ylabel('Final Gradient')
    plt.plot(E, GradFinal)
    
def main():
    # Time parameters
    dt = 0.001
    time_steps = 10000
    
    # Initialize Time Variable
    Time = np.empty((time_steps + 1))
    Time[0] = 2022
    
    # Initialize Temp Variable
    T = np.empty((time_steps + 1))
    T[0] = 14.98 + 273
    
    # Define Emissivity Factor
    E = np.linspace(0.6, 1, 100)
    
    # Initialize Final Values
    T_Final = np.empty((len(E)))
    GradFinal = np.empty((len(E)))
    
    # Calculate Equilibrium Temperatures and Final Gradients
    for i in range(len(E)):
        T_Final[i], GradFinal[i] = EquilTemp(E[i], T, dt)
        
    # Plot Equilibrium temperature vs emissivity factor
    Plot_E_Dependence(E, T_Final)
    
    # Plot Final Gradient vs emissivity factor
    Plot_FinalGrad(E, GradFinal)
    
if __name__ == '__main__':
    main()


#Notes:
#Graphing of global average temperature against emisivity.
#All the temperature projections had an exponential relationship levelling out
# at some equilibrium temperature after around 100 years.
#THIS MODEL SEEMS VERY BAD (unless i made a mistake in the code :/)
#
#Definitions:
#R = Average Heat capacity of Earth / atmosphere system.
#Q = Annual global mean incoming solar radiation per square meter of the Earth’s surface.
#a = (dimensionless) is planetary albedo (reflectivity).
#b = Stefan-Boltzmann constant.
#E = emissivity factor






    