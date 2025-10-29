N1 = float(input('Digite a nota da P1 do aluno: '))
N2 = float(input('Digite a nota da P2 do aluno: '))

Media = (N1 + N2) / 2

print(f'A média do aluno é: {Media}\n')
if Media < 5:
    print('Aluno reprovado')
elif Media >= 5 and Media < 6:
    print('Aluno para conselho')
else:
    print('Aluno aprovado')