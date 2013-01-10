import ac_math as m
import ac_rangetables as r

class Gun:
    def __init__(self, table, coords, lay, alt, deflection=3200.0):
        self._table = table
        self._coords = coords
        self._lay = lay
        self._deflection = deflection
        self._altitude = alt

    def target(self, coords, alt):
        dalt = alt - self._altitude
        range = m.dst(self._coords, coords)
        azimuth = m.azimuth(self._coords,coords)

        elev, time = solution(range, dalt, self._table)

       

class Battery:
    def __init__(self):
        self._guns = []
  
