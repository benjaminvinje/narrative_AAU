from my_xml.XmlAttributes import XmlAttributes


class Coord:
	def __init__(self, x, y, z=0):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return "x: {0}, y: {1}, z: {2}".format(self.x, self.y, self.z)

	def __dict__(self):
		ret = dict()
		ret[XmlAttributes.X] = str(self.x)
		ret[XmlAttributes.Y] = str(self.y)
		ret[XmlAttributes.Z] = str(self.z)
		return ret
	#
	# def __iter__(self):
	# 	yield self.x
	# 	yield self.y
	# 	yield self.z
