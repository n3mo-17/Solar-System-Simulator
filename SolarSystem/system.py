from numpy import zeros


class SolarSystem:
    def __init__(self):
        self.num_bodies = 0
        self._bodies = []
        self._com = zeros(2)
    
    def add_body(self, body):
        self._bodies.append(body)
        self.num_bodies += 1
        self.calc_com()
    
    def calc_com(self):
        self._com *= 0.0
        tot_mass = 0
        for b in self._bodies:
            self._com += b.mass * b.pos
            tot_mass += b.mass
        
        if tot_mass != 0:
            self._com /= tot_mass
    
    def calc_force(self):
        for b in self._bodies:
            b.calc_force(self._bodies)
    
    def update(self, dt):
        for b in self._bodies:
            b.update(dt)
        
        self.calc_com()
        self.write_self()
    
    def write_self(self):
        for b in self._bodies:
            # b.write_pos(self._com)
            b.write_pos()
            b.write_vel()