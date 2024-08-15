import matplotlib.pyplot as plt
import numpy as np

def AvTemp(T, E, R = 2.912, Q = 342, a = 0.3, b = 5.67 * pow(10, -8)):
    T_dot = (1/R) * ((Q*(1-a)) - E*b*T**4)
    return T_dot

dt = 0.001
time_steps = 10000
T = np.empty((time_steps + 1))
Time = np.empty((time_steps + 1))
T[0] = 14.98 + 273
Time[0] = 2022
FinalGrad = 0

def EquilTemp(E, T):
    for i in range(time_steps):
        T[i + 1] = T[i] + AvTemp(T[i], E) * dt
        Time[i+1] = Time[i] + dt
    GradFinal = (T[time_steps] - T[time_steps - 1])/dt
    return T[time_steps], Time[time_steps], GradFinal

def Plot_T_Dependence(T, Time):
    plt.figure()
    plt.xlabel('Year')
    plt.ylabel('Temperature')
    plt.plot(Time, T - 273)

E = np.linspace(0.6, 1, 100)
T_Final = np.empty((len(E)))
Time_Final = np.empty((len(E)))
GradFinal = np.empty((len(E)))
for i in range(len(E)):
    T_Final[i], Time_Final[i], GradFinal[i] = EquilTemp(E[i], T)

def Plot_E_Dependence(E, T_Final):
    plt.figure()
    plt.xlabel('Emissivity')
    plt.ylabel('Equilibrium Temperature')
    plt.plot(E, T_Final - 273)
    
plt.figure()
plt.xlabel('Emissivity')
plt.ylabel('Final Gradient')
plt.plot(E, GradFinal)

    
Plot_E_Dependence(E, T_Final)

def main():
    return 0

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
#
#






    