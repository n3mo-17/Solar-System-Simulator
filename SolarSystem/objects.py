from yaml import safe_load as _load
import numpy as _np


with open("SolarSystem/config.yml", "r") as f:
    constants = _load(f)


class HeavenlyBody:
    _id = 0

    def __init__(self, o_type, mass, pos, vel = _np.zeros(2), name=None):
        self.o_type = o_type
        self.mass = mass * constants["M_EARTH"]
        self.pos  = pos * constants["AU"]
        self.vel  = vel * constants["AU"] / 86400.0
        self.acc  = _np.zeros(2)
        self.name = name

        self.id_self = HeavenlyBody._id
        HeavenlyBody._id += 1

        self.write_pos(overwrite=True)
        self.write_vel(overwrite=True)
    
    def calc_force(self, bodies):
        self.acc *= 0.0
        for b in bodies:
            if b.id_self != self.id_self:
                self.acc += constants["G"] * b.mass * (b.pos - self.pos) / (_np.linalg.norm(b.pos - self.pos) ** 3)
    
    def update(self, dt):
        self.vel += self.acc * dt
        self.pos += self.vel * dt
    
    def write_pos(self, com = None, overwrite=False):
        open_mode = "w" if overwrite else "a"
        if self.name is None:
            file_path = f"output/{self.o_type}_{self.id_self}_pos.txt"
        else:
            file_path = f"output/{self.o_type}_{self.name}_pos.txt"

        curr_pos = self.pos / constants["AU"]
        if com is None:
            with open(file_path, open_mode) as f:
                f.write(f"{curr_pos[0]},{curr_pos[1]}\n")
        else:
            with open(file_path, open_mode) as f:
                f.write(f"{curr_pos[0] - com[0]},{curr_pos[1] - com[1]}\n")
    
    def write_vel(self, overwrite=False):
        open_mode = "w" if overwrite else "a"
        if self.name is None:
            file_path = f"output/{self.o_type}_{self.id_self}_vel.txt"
        else:
            file_path = f"output/{self.o_type}_{self.name}_vel.txt"
        
        curr_vel = self.vel * 86400.0 / constants["AU"]
        with open(file_path, open_mode) as f:
            f.write(f"{curr_vel[0]},{curr_vel[1]}\n")


class Sun(HeavenlyBody):
    def __new__(self, o_type, mass, pos, vel = _np.zeros(2), name=None):
        obj = super().__new__(HeavenlyBody)
        obj.__init__(o_type, mass, pos, vel, name)
        return obj


class Planet(HeavenlyBody):
    def __new__(self, o_type, mass, pos, vel = _np.zeros(2), name=None):
        obj = super().__new__(HeavenlyBody)
        obj.__init__(o_type, mass, pos, vel, name)
        return obj