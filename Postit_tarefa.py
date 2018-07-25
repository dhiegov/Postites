
from Postit import Postit

class Postit_tarefa(Postit):

	def __init__(tags, descricao, deadline):
		super().__init__(tags, descricao)
		self.deadline = deadline

	def __str__():
		rtn = super().__str__()
		rtn += ' (' + str(self.deadline) + ')'
		return rtn

