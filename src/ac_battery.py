import ac_math as m
import ac_rangetables as r
from xml.dom import minidom

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

class Mission:
    def __init__(self, pre, num, coords):
        self._pre = pre
        self._num = num
        self._coords = coords

    def adjust(self, ot, add, right, up):
        self._coords = m.adjust(self._coords,ot,add,right,up)


def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def getNodeText(dom, name):
    return getText(dom.getElementsByTagName(name)[0].childNodes)

def addText(dom, name, val):
    elem = dom.createElement(name)
    text = dom.createTextNode(val)
    dom.appendChild(elem)
    elem.appendChild(text)

class Ballistics:
    def __init__(self, files):

class Battery:
    def __init__(self, name="", callsign="", type=None, grid="", alt=0, lay=0, line_dir=0, line_dist=0, guns=0, tgtpre="", tgtstart=0):
        self._info = [name, callsign, type]
        self._lay = [grid, alt, lay]
        self._line = [line_dir, line_dist, guns]
        self._tgtinfo = [tgtpre, tgtstart]

    def xml_save(file):
        doc = minidom.getDOMImplementation.createDocument(None, "battery", None)

        dom = doc.documentElement

        addText(dom, "name", self._info[0])
        addText(dom, "callsign", self._info[1])
        addText(dom, "type", self._info[2])

        addText(dom, "grid", self._lay[0])
        addText(dom, "alt", self._lay[1])
        addText(dom, "lay", self._lay[2])

        addText(dom, "gunline_dir", self._line[0])
        addText(dom, "gunline_dist", self._line[1])
        addText(dom, "gunline_guns", self._line[2])

        addText(dom, "tgtpre", self._tgtinfo[0])
        addText(dom, "tgtidx", self._tgtinfo[1])

        xml = dom.toxml()

        f = open(file, 'w')
        f.write(xml)
        f.close()



    @classmethod
    def xml_load(file):
        # load basic info
        dom = minidom.parse(file)

        name = getNodeText(dom, "name")
        callsign = getNodeText(dom, "callsign")
        type = getNodeText(dom, "type")

        grid = getNodeText(dom, "grid")
        alt = getNodeText(dom, "alt")
        lay = getNodeText(dom, "lay")

        tgtpre = getNodeText(dom, "tgtpre")
        tgtidx = (int)getNodeText(dom, "tgtidx")

        gunline_guns = getNodeText(dom, "gunline_guns")
        gunline_dir = getNodeText(dom, "gunline_dir")
        gunline_dist = getNodeText(dom, "gunline_dist")

        bat = cls(name, callsign, type, grid, alt, lay, gunline_dir, gunline_dist, gunline_guns, tgtpre, tgtidx)

        # load missions
        #mnode = dom.getElementsByTagName("missions")[0]

        #bat._missions = []

        #for n in mnode.childNodes:
        #    pre = getNodeText(n, "pre")
        #    num = getNodeText(n, "num")
        #    coords = getNodeText(n, "coords")

        #    bat._missions.append(Mission(pre, num, coords))


        #return bat
