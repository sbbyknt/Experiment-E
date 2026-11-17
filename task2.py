import numpy as np
import matplotlib.pyplot as plt
import scipy as scp
plt.style.use("ggplot")

fname = "task2data.csv"
rawdata = np.loadtxt(fname, delimiter=",", skiprows=1)
applied_voltage = rawdata[:,0]
diode_current = rawdata[:,1]
assert len(applied_voltage) == len(diode_current)


fig, ax = plt.subplots()
ax.plot(applied_voltage, diode_current,linestyle=" ",marker=".",color="k")
ax.set_xlabel("Applied voltage ($V$)")
ax.set_ylabel("Diode current ($I_D$)")
plt.show()