import ac_math as m
import ac_rangetables as r

class Point:
    def __init__(self, name, grid, alt):
        print "New Point: %s %s %s" % (name, grid, alt)

        # verify grid
        l = len(grid)
        if not l in (4,6,8,10):
            raise ValueError("Grid %s not 4,6,8, or 10-digit grid" % (grid))
        
        l = l/2

        self._xcoord = int(grid[0:l])
        self._ycoord = int(grid[l:l+l])
        self._altitude = int(alt)

        print "%s - %s, %s" % (self._xcoord, self._ycoord, self._altitude)

        if self._xcoord < 0 or self._ycoord < 0:
            raise "Negative Coords not supported"

        self._name = name
        self._grid = grid
        self._alt = alt


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
  
