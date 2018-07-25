
class Postit:
  def __init__(tags, descricao):
    self.tags = tags
    self.descricao = descricao
  
  def __str__():
    rtn = str(self.descricao)
    rtn += ' [' + str(self.tags) + ']'
    return rtn
