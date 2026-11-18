import numpy as np
import matplotlib.pyplot as plt
import scipy as scp
plt.style.use("ggplot")

fname = "task3data.csv"
data = np.loadtxt(fname, delimiter=",", skiprows=1)
frequency = data[:,0]
actual_gain = data[:,1]
assert len(frequency) == len(actual_gain)

fig, ax = plt.subplots()
ax.plot(frequency, actual_gain,linestyle=" ",marker='.',color='k') #removes point-by-point line

ax.set_xlabel("Frequency ($f$)")
ax.set_ylabel("Actual gain")
plt.show()