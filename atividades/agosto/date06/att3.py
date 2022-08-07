from bdb import Breakpoint


def valorHora(salario: float, dias: int, horas: int = 8) -> float:
    totalSalario = salario / (dias * horas)
    print(f'O valor hora de trabalho é: {totalSalario}')

salario_pessoa: float = float(input('Digite seu salário: '))
num_dias: int = int(input('Digite a quantidade de dias trabalhados: '))
horas_dia: str = (input('Digite a quantidade de horas: '))
  
if horas_dia == '' or not horas_dia.isdigit():
    valorHora(salario_pessoa, num_dias)
else:
    valorHora(salario_pessoa, num_dias, int(horas_dia))