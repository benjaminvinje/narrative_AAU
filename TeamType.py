from enum import Enum


class TeamType(Enum):
	HOME = 'H' #red
	AWAY = 'A' #blue
	UNDEFINED = 'U'

	def __str__(self):
		return self.name.replace("_", " ")
