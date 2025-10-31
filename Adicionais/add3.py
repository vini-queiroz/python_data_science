# Exercício 3
# Faça um programa que leia e valide as seguintes informações:
# 
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Estado Civil: 's', 'c', 'v', 'd';


nome = ''
idade = 0
salario = 0
est_civil = ''

while len(nome) <= 3:
    nome = input('Digite seu nome: ')

while idade < 1 or idade > 150:
    try:
        idade = int(input('Digite sua idade: '))
    except:
        print('Digite um valor valido')
        
while salario == 0:
    try:
        salario = int(input('Digite Salário: '))
    except:
        print('Digite um valor valido')
        
while est_civil != ('s' or 'c' or 'v' or 'd'): 
    est_civil = input('Digite seu Estado Civil: ')

print(nome, '\n', idade, '\n', salario, '\n', est_civil)