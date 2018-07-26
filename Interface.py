
from Fachada import Fachada

class Interface():

	def __init__(self):
		self.fachada = Fachada()

	def mostrar_dashboard(self):
		postits = self.fachada.obter_dashboard()

		for postit in postits:
			print(postit)

	def mostrar_postits_arquivados(self):
		postits = self.fachada.obter_postits_arquivados()

		for postit in postits:
			print(postit)

	def criar_postit_simples(self):
		descricao = input("Descrição: ")
		tag = input("Tags: ")

		self.fachada.criar_postit_simples(tag, descricao)

	def criar_postit_tarefa(self):
		descricao = input("Descrição: ")
		tag = input("Tags: ")
		deadline = input("Deadline: ")

		self.fachada.criar_postit_tarefa(tag, descricao, deadline)

	def arquivar_postit(self):
		postits = self.fachada.obter_dashboard()

		contador = 0
		for postit in postits:
			print(contador, postit)

		numero = input("Número do post-it a ser arquivado: ")

		self.fachada.arquivar_postit(postit)

	def buscar_postit(self):
		tag = input("tag termo de pesquisa: ")

		postits = self.fachada.buscar_postit(tag)

		for postit in postits:
			print(postit)
