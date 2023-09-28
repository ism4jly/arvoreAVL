class NoAVL:
  def __init__(self, chave):
      self.chave = chave
      self.altura = 1
      self.left = None
      self.right = None


class ArvoreAVL:
  def __init__(self):
      self.raiz = None

  def altura(self, no):
      if no is None:
          return 0
      return no.altura

  def fator_balanceamento(self, no):
      if no is None:
          return 0
      return self.altura(no.left) - self.altura(no.right)

  def atualizar_altura(self, no):
      if no is not None:
          no.altura = 1 + max(self.altura(no.left), self.altura(no.right))

  def rotacao_esquerda(self, z):
      y = z.right
      T2 = y.left

      y.left = z
      z.right = T2

      self.atualizar_altura(z)
      self.atualizar_altura(y)

      return y

  def rotacao_direita(self, y):
      x = y.left
      T2 = x.right

      x.right = y
      y.left = T2

      self.atualizar_altura(y)
      self.atualizar_altura(x)

      return x

  def balancear(self, no):
      if no is None:
          return None

      no.altura = 1 + max(self.altura(no.left), self.altura(no.right))

      fator = self.fator_balanceamento(no)

      if fator > 1:
          if self.fator_balanceamento(no.left) < 0:
              no.left = self.rotacao_esquerda(no.left)
          return self.rotacao_direita(no)
      if fator < -1:
          if self.fator_balanceamento(no.right) > 0:
              no.right = self.rotacao_direita(no.right)
          return self.rotacao_esquerda(no)

      return no

  def inserir(self, raiz, chave):
      if raiz is None:
          return NoAVL(chave)
      if chave < raiz.chave:
          raiz.left = self.inserir(raiz.left, chave)
      else:
          raiz.right = self.inserir(raiz.right, chave)

      return self.balancear(raiz)

  def remover(self, raiz, chave):
      if raiz is None:
          return raiz
      if chave < raiz.chave:
          raiz.left = self.remover(raiz.left, chave)
      elif chave > raiz.chave:
          raiz.right = self.remover(raiz.right, chave)
      else:
          if raiz.left is None:
              return raiz.right
          elif raiz.right is None:
              return raiz.left
          min_no = self.minimo_no(raiz.right)
          raiz.chave = min_no.chave
          raiz.right = self.remover(raiz.right, min_no.chave)

      return self.balancear(raiz)

  def minimo_no(self, no):
      while no.left is not None:
          no = no.left
      return no

  def buscar(self, raiz, chave):
      if raiz is None or raiz.chave == chave:
          return raiz
      if chave < raiz.chave:
          return self.buscar(raiz.left, chave)
      return self.buscar(raiz.right, chave)

  def inserir_chave(self, chave):
      self.raiz = self.inserir(self.raiz, chave)

  def remover_chave(self, chave):
      self.raiz = self.remover(self.raiz, chave)

  def buscar_chave(self, chave):
      return self.buscar(self.raiz, chave)
