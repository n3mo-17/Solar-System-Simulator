from SolarSystem import SolarSystem, Sun, Planet
from yaml import safe_load_all
import numpy as np

ss = SolarSystem()

with open("user_config.yml", "r") as f:
    obj = safe_load_all(f)
    for data in obj:
        if "general" in data.keys():
            gen = data["general"]

            dt = gen["dt"]
            tfinal = gen["tfinal"]
        else:
            name = data["name"] if "name" in data.keys() else None
            if data["type"] == "sun":
                ss.add_body(Sun(data["type"], data["mass"], np.array(data["position"]), np.array(data["velocity"]), name))
            elif data["type"] == "planet":
                ss.add_body(Planet(data["type"], data["mass"], np.array(data["position"]), np.array(data["velocity"]), name))

t = 0
while t < tfinal:
    ss.calc_force()
    ss.update(dt)

    t += dt
    print("Current progress:", t * 100.0 / tfinal)
