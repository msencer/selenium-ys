import os
import xml.etree.ElementTree as ET
def singleton(cls):
	_instances = {}
	def getinstance():
		if cls not in _instances:
			_instances[cls] = cls()
		return _instances[cls]
	return getinstance
@singleton
class configs(object):
	def __init__(self,xmlFile = "config.xml"):
		f = os.path.join(os.path.dirname(os.path.realpath(__file__)),xmlFile)
		conf = ET.parse(f)
		root = conf.getroot()
		self.members = {}
		try:
			for child in root:
			   self.members[child.tag] = child.attrib
		except:
			print "Exception on parsing XML"
	def __getattr__(self,name):
		if name in self.members:
			return self.members[name]
		return None