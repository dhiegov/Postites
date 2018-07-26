
from PostitSimples import PostitSimples
from PostitTarefa import PostitTarefa

class Fachada:

    def __init__(self):
        self.postits = list()
        self.arquivados = list()

    def criar_postit_simples(self, tags, descricao):
        postit = PostitSimples(tags, descricao)

        self.postits.append(postit)

    def criar_postit_tarefa(self, tags, descricao, deadline):
        postit = PostitTarefa(tags, descricao, deadline)

        self.postits.append(postit)

    def buscar_postit(self, tag):
        resultados = list()

        for postit in self.postits:
            if tag in postit.tags:
                resultados.append(postit)

        return resultados

    def obter_dashboard(self):
        return self.postits

    def obter_postits_arquivados(self):
        return self.arquivados

    def arquivar_postit(self, postit):
        self.postits.remove(postit)
        self.arquivados.append(postit)
