Nasc = int(input('Digite seu ano de nascimento para saber se é maior de idade: '))

Idade = 2025 - Nasc

print(f'Você tem {Idade} anos\n')

if Idade >= 18:
    print('Voce é maior de idade!')
else:
    print('Voce é menor de idade!')
   