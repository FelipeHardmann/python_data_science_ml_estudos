class Animal:
  def __init__(self, peso: float, idade: int, membros: int) -> None:
    self._peso = peso
    self._idade = idade
    self._membros = membros

  @property
  def peso(self) -> float:
    return self._peso
  
  @peso.setter
  def peso(self, novo_peso) -> None:
    self._peso = novo_peso

  @property
  def idade(self) -> int:
    return self._idade

  @idade.setter
  def idade(self, nova_idade) -> None:
    self._idade = nova_idade

  @property
  def membros(self) -> int:
    return self._membros

  @membros.setter
  def membros(self, quantidade) -> None:
    self._membros = quantidade

  def _locomover(self) -> str:
    return 'Animal se locomovendo'
  
  def _alimentar(self) -> str:
    return 'Animal se alimentando'

  def _emitir_som(self) -> str:
    return 'Animal emitindo som'


class Mamifero(Animal):
  def __init__(self, peso: float, idade: int, membros: int, 
               tem_pelo: bool = True, cor: str = 'caramelo') -> None:
    super().__init__(peso, idade, membros)
    self._pelo = tem_pelo
    self._cor = cor if tem_pelo else None

  @property
  def pelo(self) -> bool:
    return self._pelo

  @pelo.setter
  def pelo(self, crescer_pelo: bool) -> None:
    self._pelo = crescer_pelo

  @property
  def cor(self) -> str:
    return self._cor

  @cor.setter
  def cor(self, nova_cor) -> None:
    self._cor = nova_cor


class Cachorro(Mamifero):
  def __init__(self, nome: str, raca: str,
               peso: float, idade: int, membros: int, 
               tem_pelo: bool, cor: str) -> None:
    super().__init__(peso, idade, membros, tem_pelo, cor)
    self.__nome = nome
    self.__raca = raca

  @property
  def nome(self) -> str:
    return self.__nome

  @nome.setter
  def nome(self, novo_nome: str) -> None:
    self.__nome = novo_nome

  @property
  def raca(self) -> str:
    return self.__raca

  @raca.setter
  def raca(self, nova_raca: str) -> None:
    self.__raca = nova_raca

  def _alimentar(self) -> str:
    return f'{self.nome.title()} está comendo ração'
  
  def _locomover(self) -> str:
    return f'{self.nome.title()} está passeando'

  def _emitir_som(self) -> str:
    return f'{self.nome.title()} está latindo'

  def _fazer_festa(self, pessoa: str = 'mim') -> str:
    return f'{self.nome.title()} está fazendo muita festa pra {pessoa}!'

  def _enterrar_osso(self) -> str:
    return f'{self.nome.title()} enterrou o osso no quintal'