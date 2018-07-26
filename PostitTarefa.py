
from Postit import Postit

class PostitTarefa(Postit):

	def __init__(self, tags, descricao, deadline):
		super().__init__(tags, descricao)
		self.deadline = deadline

	def __str__(self):
		rtn = super().__str__()
		rtn += ' (' + str(self.deadline) + ')'
		return rtn

