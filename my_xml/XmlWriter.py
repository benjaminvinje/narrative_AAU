from xml.dom import minidom
from xml.etree.ElementTree import Element, ElementTree, SubElement, Comment, tostring
from xml.etree import ElementTree

from my_xml.XmlTags import XmlTags


class XmlWriter:
	def __init__(self, path, game):
		self.path = path
		# self.event_data_improved_path = "{0}/f24-100-2019-{1}-eventdetails_improved.xml"
		self.event_data_improved_path = game.event_data_improved_path

	def generate_event_details_xml(self, game):
		root = Element(XmlTags.GAMES, game.game_summary.__dict__)

		xml_game = SubElement(root, XmlTags.GAME)

		for event in game.events:
			event_attr_dict = vars(event)()
			xml_event = SubElement(xml_game, XmlTags.EVENT, event_attr_dict)
			for q in event.qualifiers:
				quali_attr_dict = vars(q)()
				xml_quali = SubElement(xml_event, XmlTags.QUALIFIER, quali_attr_dict)

		return root

	def prettify(self, elem):
		rough_string = ElementTree.tostring(elem, 'utf-8')
		reparsed = minidom.parseString(rough_string)
		return reparsed.toprettyxml(indent="  ")
