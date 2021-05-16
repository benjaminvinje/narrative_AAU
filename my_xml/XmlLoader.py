from Event import Event
from Qualifier import Qualifier
from my_xml.XmlAttributes import XmlAttributes
from my_xml.XmlTags import XmlTags


class XmlLoader:
	def load_value_from_tag(self, node, tag, attr):
		stats = node.getElementsByTagName(tag)
		for stat in stats:
			type = self.try_loading_attr(stat.attributes, XmlAttributes.TYPE)
			if type == attr.lower():
				return stat.firstChild.nodeValue

	def try_loading_attr(self, attrs, attr):
		try:
			return attrs[attr].value
		except KeyError:
			return None

	def create_event_based_on_xml(self, xml_event):
		attrs = xml_event.attributes
		event_id = attrs[XmlAttributes.EVENT_ID].value
		id = attrs[XmlAttributes.ID].value
		last_modified = attrs[XmlAttributes.LAST_MODIFIED].value
		min = attrs[XmlAttributes.MIN].value
		outcome = attrs[XmlAttributes.OUTCOME].value
		period_id = attrs[XmlAttributes.PERIOD_ID].value
		sec = attrs[XmlAttributes.SEC].value
		team_id = attrs[XmlAttributes.TEAM_ID].value
		timestamp = attrs[XmlAttributes.TIMESTAMP].value
		type_id = attrs[XmlAttributes.TYPE_ID].value
		try:
			version = attrs[XmlAttributes.VERSION].value
		except KeyError:
			version = "" # event may have no version attribute
		x = attrs[XmlAttributes.X].value
		y = attrs[XmlAttributes.Y].value
		player_id = self.try_loading_attr(attrs, XmlAttributes.PLAYER_ID)
		reception_id = self.try_loading_attr(attrs, XmlAttributes.RECEPTION_ID)
		player_corrected = self.try_loading_attr(attrs, XmlAttributes.PLAYER_CORRECTED)
		frame_id = self.try_loading_attr(attrs, XmlAttributes.FRAME_ID)

		event = Event(id, event_id, type_id, period_id, min, sec, team_id, outcome, x, y, timestamp, last_modified,
					  version, player_id)
		event.reception_id = reception_id
		event.player_corrected = player_corrected
		event.frame_id = int(frame_id) if frame_id is not None else None

		qualifiers = xml_event.getElementsByTagName(XmlTags.QUALIFIER)
		for q in qualifiers:
			attrs = q.attributes
			qualifier_id = attrs[XmlAttributes.QUALIFIER_ID].value
			q_id = attrs[XmlAttributes.ID].value
			value = self.try_loading_attr(attrs, XmlAttributes.VALUE)

			qualifier = Qualifier(q_id, qualifier_id, value)
			event.qualifiers.append(qualifier)
		return event
