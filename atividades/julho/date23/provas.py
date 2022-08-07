nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
nota3 = float(input('Digite sua nota: '))
nota4 = float(input('Digite sua nota: '))

notas = [nota1, nota2, nota3, nota4]
media = sum(notas) / 4
print(media) 

if media >= 7:
    print('Aluno aprovado!')
elif  5 < media < 7:
    print('Aluno em recuperação')
else:
    print('Aluno reprovado')