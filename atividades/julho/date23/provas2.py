notas = []
for i in range(4):
    nota = float(input('Digite sua nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)
if media >= 7:
    print(f'Aluno aprovado {media}!')
elif  5 < media < 7:
        print(f'Aluno em recuperação{media}')
else:
        print(f'Aluno reprovado{media}')