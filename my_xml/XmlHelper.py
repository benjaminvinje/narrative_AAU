import html
from xml.dom import minidom
from xml.parsers.expat import ExpatError

import Constants


def load_xml(path):
	try:
		return minidom.parse(path)
	except ExpatError:
		with open(path, 'r') as file:
			lines = file.readlines()

		for i in range(len(lines)):
			if lines[i] == Constants.xml_defining_string_16 or lines[i] == Constants.xml_defining_string_8:
				headline = lines[i]
				del lines[i]
				lines.insert(0, headline)
				break

		with open(path, 'w') as file:
			file.writelines(lines)

		file_text = html.unescape(open(path, 'r').read())
		xmldoc = minidom.parseString(file_text)
		return xmldoc
