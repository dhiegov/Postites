
class Postit:
	"""Classe 'abstrata'."""

	def __init__(self, tags, descricao):
		self.tags = tags
		self.descricao = descricao

	def __str__(self):
		rtn = str(self.descricao)
		rtn += ' [' + str(self.tags) + ']'
		return rtn

