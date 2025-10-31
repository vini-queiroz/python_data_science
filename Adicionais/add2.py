# Exercício 2

# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
# ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
Check = True


while Check == True:
    Nome = input('Digite o nome de usuário: ')
    Senha = input('Digite a senha: ')
    
    if Nome == Senha:
        Check = True
        print('\nO Usuário e a Senha não podem ser iguais!\n')
    else:
        Check = False
        print('\nLogin efetuado com sucesso!')