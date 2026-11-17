import numpy as np
import matplotlib.pyplot as plt
import scipy as scp
plt.style.use("ggplot")

#imports the data from task1data.csv
fname = "task1data.csv"
data = np.loadtxt(fname, delimiter=",", skiprows=1)
R_L = data[:,0] #independent variable
V = data[:,1] #dependent variable
assert len(V) == len(R_L)

V_squared = np.array([value ** 2 for value in V])
V_squared_over_R_L = np.array([V_squared[i] / R_L[i] for i in range(len(V))])

fig, ax = plt.subplots()
ax.plot(R_L,V_squared_over_R_L,linestyle=" ", marker='.',color="k")
ax.set_xlabel("$R_L$, ($\Omega$)")
ax.set_ylabel("$V^2 / R_L$, ($W$)")
plt.show()

#we need to find the maximum power transferred, which is given by dP/dR_L = 0

