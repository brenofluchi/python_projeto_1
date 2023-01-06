from random import randint

class Calcular:
    def __init__(self: object, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1,3)
        self.__resultado: int = self.gerar_resultado
@property
def dificuldade(self:object) -> int:
    return self.__dificuldade

@property
def valor1(self:object) -> int:
    return self.__valor1

@property
def valor2(self:object) -> int:
    return self.__valor2

@property
def operacao(self:object) -> int:
    return self.__operacao

@property
def resultado(self:object) -> int:
    return self.__resultado

def __str__(self:object) -> str:
    op: str = ''
    if self.operacao == 1:
        op = 'somar'
    elif self.operacao == 2:
        op = 'diminuir'
    elif self.operacao == 3:
        op = 'multiplicar'
    else:
        op = 'Operação desconhecida'
    return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação : {op}'