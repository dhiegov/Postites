
import os

class PostitDAO:

	def converter_para_json(postit):
		pass

	def obter_postits(self):
		"""Retorne uma list<Postit> de postits não-arquivados."""
		simples = obter_postits_simples('dashboard')
		tarefa = obter_postits_tarefa('dashboard')

		postits = simples.extend(tarefa)

		return postits

	def obter_postits_arquivados(self):
		"""Retorne uma list<Postit> de postits arquivados."""
		pass

	def obter_postits_simples(self, local):
		"""Retorne uma lista de PostitSimples de <local>.
		
		<local> pode ser 'dashboard' ou 'arquivo'.
		"""
		pass

	def obter_postits_tarefa(self, local):
		"""Retorne uma lista de PostitTarefa de <local>.
		
		local é str, 'dashboard' ou 'arquivo'.
		"""
		pass

	def salvar_postits(self, postits):
		"""Salve os dados postits no arquivo 'dashboard.json'.
		
		postits é list<Postit>.
		"""
		pass

	def salvar_postits_simples(self, postits):
		"""Salve uma lista de PostitSimples em disco.
		
		postits é list<PostitSimples>.
		"""
		pass

	def salvar_postits_tarefa(self, postits):
		"""Salve uma lista de PostitTarefa em disco.
		
		postits é list<PostitTarefa>.
		"""
		pass

