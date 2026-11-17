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

#using SciPy to try and model a curve
#Source: https://education.molssi.org/python-data-analysis/03-data-fitting/index.html
def f(x, A, B, C, D):
    y = A * (x**3) + B * (x**2) + C * x + D
    return y
parameters, covariance = scp.optimize.curve_fit(f, R_L, V_squared_over_R_L)

fig, ax = plt.subplots()
ax.plot(R_L,V_squared_over_R_L,linestyle=" ", marker='.',color="k")
#plotting fitted curve and smoothing it

moreR_L = np.linspace(np.min(R_L), np.max(R_L), 1000)
fit_polynomial = f(moreR_L, parameters[0], parameters[1], parameters[2], parameters[3])
ax.plot(moreR_L, fit_polynomial, color="red")


ax.set_xlabel("$R_L$, ($\Omega$)")
ax.set_ylabel("$V^2 / R_L$, ($W$)")
plt.show()

#we need to find the maximum power transferred, which is given by dP/dR_L = 0


