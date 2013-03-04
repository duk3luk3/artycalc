import math
from operator import add
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

def adjust(coords, ot, add, right, up):
  x,y,z = coords
  north = math.cos(ot) * add + math.sin(ot) * right
  east = math.sin(ot) * add + math.cos(ot) * right
  return (x+east,y+north,z+up)

def mils(rad):
  return rad / (2.0 * math.pi) * 6400.0

def rad(mils):
  return mils * (2.0 * math.pi) / 6400.0

def rad_from_deg(deg):
  return deg * (2.0 * math.pi) / 360.0

def angle(a):
  try:
    return rad(float(a))
  except ValueError:
    if isinstance ( a , str):
      v = float(a[0:-1])
      d = a[-1]
      if d == 'd':
        return rad_from_deg(float(v))
      elif d == 'm':
        return rad(float(v))
      else:
        raise ValueError("No valid unit denotated in angle string %s" % (a))
    else:
      raise TypeError("angle function expects floatable value or string, got " + str(type(a)))

def is_angle(a):
  try:
    angle(a)
    return True
  except:
    return False
    

# Quadrant (elevation) and flight time
def calc(range, dAlt, table):
  rtable, atable, ttable, ltable, r = table

  nom = lambda a, x, e: a*(x**e)
  ranges = [range for x in range(len(rtable))]
  exps = range(rtable)

  elev = \
    reduce(add, map ( nom, rtable, ranges, exps)) - \
    reduce(add, map ( nom, atable, ranges, exps)) * dAlt / 100.0   
 
  time = \
    reduce(add, map ( nom, ttable, ranges, exps)) - \
    reduce(add, map ( nom, ltable, ranges, exps)) * dAlt / 100.0 
  
  return elev, time

# Solution
def solution(range, dAlt, table, add):
    #limits = [(t[4][0],t[4][1]) for t in table]
    p = lambda t,x: x >= t[4][0] and x <= t[4][1]
    usable = filter(p, table)
    use = usable[min(len(usable))-1,add]

    return calc(range, dAlt, use)


