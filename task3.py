import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

fname = "task3data.csv"
data = np.loadtxt(fname, delimiter=",", skiprows=1)
frequency = data[:,0]
actual_gain = data[:,1]
assert len(frequency) == len(actual_gain)

fig, ax = plt.subplots()
ax.plot(frequency, actual_gain)
ax.set_xlabel("Frequency ($f$)")
ax.set_ylabel("Actual gain")
plt.show()