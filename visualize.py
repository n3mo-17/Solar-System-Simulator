import matplotlib.pyplot as plt
import numpy as np
import glob

output_dir  = ".\\output\\"
planets_pos = glob.glob(output_dir + "planet*pos.txt")
suns_pos    = glob.glob(output_dir + "sun*pos.txt")

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.grid(color='gray', linestyle='dashed')
ax.set_axisbelow(True)

for planet_pos in planets_pos:
    name = planet_pos.split("_")[1]
    planet = np.loadtxt(planet_pos, delimiter=",")
    ax.scatter(planet[:, 0], planet[:, 1], s=0.1, label=name)

for sun_pos in suns_pos:
    name = sun_pos.split("_")[1]
    sun = np.loadtxt(sun_pos, delimiter=",")
    ax.scatter(sun[:, 0], sun[:, 1], s=5, label=name)

ax.set_aspect("equal")
ax.set_xlabel("X (AU)")
ax.set_ylabel("Y (AU)")
plt.legend(loc="lower left")
plt.title("Solar System Simulation")
plt.savefig("output/graphs/pos_graph.png")