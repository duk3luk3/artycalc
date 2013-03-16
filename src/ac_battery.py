# vim:set ts=2 sw=2 noexpandtab:

import ac_math as m
import ac_rangetables as r
from xml.dom import minidom


def ApplyStyle(w,s):
	w['style']=s
	print w['style']

NormalStyle = lambda w: ApplyStyle(w,'TEntry')
InvalidStyle = lambda w: ApplyStyle(w, 'Invalid.TEntry')
inv = lambda x: InvalidStyle(x)
val = lambda x: NormalStyle(x)

class ControllableStrings:
	def __init__(self, vals={})
		self._vals = vals
		self._listeners = dict([(x,[]) for x in vals.keys()])
		self._validators = dict([(x,None) for x in vals.keys()])

	def queryProp(self, prop):
		return 'String'

	def attachProp(self, prop, listener):
		self._listeners[prop].append(listener)

	def addProp(self, prop, val, validator):
		if prop in self._vals:
			raise KeyError("Duplicate key %s" % (prop))
		else:
			self._vals[prop] = val
			self._listeners[prop] = []
			self._validators[prop] = validator
	
	def getProp(self, prop):
		return self._vals[prop]

	def setProp(self, prop, value):
		if not prop in self._vals:
			raise KeyError("Missing key %s" % (prop))

		if self._validators[prop](value):
			self._vals[prop] = value
			for l in self._listeners[prop]:
				l()
			return True
		else:
			return False

	def trace_validate(self, control, var, prop):
		if self._object.setProp(var.get()):
			val(control)
		else:
			inv(control)

	## attach a control to a property
	def attachControl(self, prop, control,read=True,write=True):
		t = self._object.queryProp(prop)
		if t == 'String':
			if read or write:
				v = StringVar()
			if read:
				control["textvariable"] = v
				v.trace("w",lambda n i m: self.trace_validate(control, v, prop))
			if write:
				self._object.attachProp(prop, v.set)

class Point:
	def __init__(self, name="", grid="0000", alt=0):
		print "New Point: %s %s %s" % (name, grid, alt)
		self.setGrid(grid)
		self.setAlt(alt)
		print "%s - %s, %s" % (self._xcoord, self._ycoord, self._altitude)

	def setGrid(self, grid):
		# verify grid
		l = len(grid)
		if not l in (4,6,8,10):
			raise ValueError("Grid %s not 4,6,8, or 10-digit grid" % (grid))
		l = l/2
		self._xcoord = int(grid[0:l])
		self._ycoord = int(grid[l:l+l])
		if self._xcoord < 0 or self._ycoord < 0:
			raise "Negative Coords not supported"

	def setAlt(self, alt):
		self._altitude = float(alt)

	def tpl(self):
		return (self._xcoord, self._ycoord, self._altitude)

	def setTpl(self, coords):
		self._xcoord,self._ycoord,self._altitude = coords

	def adjust(self, ot, add, right, up):
		self.setTpl(m.adjust(self._tpl,ot,add,right,up))


class Mission(EditController):
	def __init__(self):
		self.Store = ControllableStrings({
			'description':'',
			'extent':'',
			'length':'',
			'attitude':''




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


class Battery:
	def __init__(self, name="", callsign="", type="", coords=Point(), lay=0, line_dir=0, line_dist=0, guns=0, tgtpre="", tgtstart=0):
		self._info = [name, callsign, type]
		self._lay = [coords, lay]
		self._line = [line_dir, line_dist, guns]
		self._tgtinfo = [tgtpre, tgtstart]

	def setName(self, name):
		self._info[0] = name
		print "Battery name set to %s" % (name)

	def setCallsign(self,name):
		self._info[1] = name
		print "Battery callsign set to %s" % (name)

	def setType(self, type):
		self._info[2] = type
		print "Battery type set to %s" % (type)

	def setGrid(self, grid):
		self._lay[0].setGrid(grid)

	def setAlt(self, alt):
		self._lay[0].setAlt(alt)

	def setLay(self, lay):
		a = angle(lay)
		self._lay[1] = lay

	def setLinedir(self, dir):
		a = angle(dir)
		self._line[0] = dir

	def setLinedist(self, dist):
		self._line[1] = float(dist)

	def setLineguns(self, guns):
		self._line[2] = int(guns)

	def setPrefix(self, pre):
		self._tgtinfo[0] = pre

	def setOffset(self, off):
		self._tgtinfo[1] = int(off)


	def xml_save(file):
		doc = minidom.getDOMImplementation.createDocument(None, "battery", None)

		dom = doc.documentElement

		addText(dom, "name", self._info[0])
		addText(dom, "callsign", self._info[1])
		addText(dom, "type", self._info[2])

		addText(dom, "grid", self._lay[0]._grid)
		addText(dom, "alt", self._lay[0]._alt)
		addText(dom, "lay", self._lay[1])

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
		tgtidx = int(getNodeText(dom, "tgtidx"))

		gunline_guns = getNodeText(dom, "gunline_guns")
		gunline_dir = getNodeText(dom, "gunline_dir")
		gunline_dist = getNodeText(dom, "gunline_dist")

		c = Point("",grid,alt)

		bat = cls(name, callsign, type, c, lay, gunline_dir, gunline_dist, gunline_guns, tgtpre, tgtidx)

		# load missions
		#mnode = dom.getElementsByTagName("missions")[0]

		#bat._missions = []

		#for n in mnode.childNodes:
		#	pre = getNodeText(n, "pre")
		#	num = getNodeText(n, "num")
		#	coords = getNodeText(n, "coords")

		#	bat._missions.append(Mission(pre, num, coords))


		#return bat
