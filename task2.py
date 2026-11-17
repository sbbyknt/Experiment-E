import numpy as np
import matplotlib.pyplot as plt
import scipy as scp
plt.style.use("ggplot")

fname = "task2data.csv"
rawdata = np.loadtxt(fname, delimiter=",", skiprows=1)
V_in = rawdata[:,0]
V_out = rawdata[:,1]

resistance = 10_000
assert len(V_in) == len(V_out)
applied_voltage = [V_in[i] - V_out[i] for i in range(len(V_in)) ]
diode_current = [applied_voltage[j] / resistance for j in range(len(applied_voltage))]

fig, ax = plt.subplots()
ax.plot(applied_voltage, diode_current,linestyle=" ",marker='.',color="k")
ax.set_xlabel("Applied voltage ($V$)")
ax.set_xscale("log") #used logscale to show sudden jump
ax.set_ylabel("Diode current ($I_D$)")
plt.show()