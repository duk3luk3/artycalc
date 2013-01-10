import math
from operator import math
## Basic geometry

# Coordinate System origin is in lower left (Or South-West)

# x component of a tuple "point"
def x(a):
  return a[0]

# y components
def y(a):
  return a[1]

# "manhattan distance"
def sdst(a,b):
  return ( x(a)-x(b), y(a)-y(b) )

# euclidean distance
def dst(a, b):
  x,y = sdst(a,b)
  return math.sqrt(x*x+y*y)

# azimuth against north (0 = north, PI = south) in rad
def azimuth(a,b):
  range = dst(a,b)
  az = math.acos((y(a)-y(b))/range)
  if x(a) > x(b):
      az = 2* math.pi - az
  return az
# Quadrant (elevation) and flight time
def calc(range, dAlt, table):
  rtable, atable, ttable, ltable, r = table

  nom = lambda a, x, e: a*(x**e)
  ranges = [range for x in range(len(rtable))]
  exps = range(rtable)

  elev = \
    reduce(add, map ( nom, rtable, ranges, exps)) - \               # range
    reduce(add, map ( nom, atable, ranges, exps)) * dAlt / 100.0    # altitude adjust
 
  time = \
    reduce(add, map ( nom, ttable, ranges, exps)) - \               # range
    reduce(add, map ( nom, ltable, ranges, exps)) * dAlt / 100.0    # altitude adjust
  
  return elev, time

# Solution
def solution(range, dAlt, table, add):
    #limits = [(t[4][0],t[4][1]) for t in table]
    p = lambda t,x: x >= t[4][0] and x <= t[4][1]
    usable = filter(p, table)
    use = usable[min(len(usable))-1,add]

    return calc(range, dAlt, use)


