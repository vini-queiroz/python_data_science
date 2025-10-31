# Exercício 1
# 
# Faça um programa que peça uma nota, entre zero e dez.Mostre uma mensagem caso o valor
# seja inválido e continue pedindo até que o usuário informe um valor válido.

check =  False
while check == False:
    
    resp = int(input('Digite um número: '))
    
    if resp > 11 or resp < 0:
        print('Número invalido!\n')
        check = False
    else:
        print('Acerto miserávi!\n')
        check = True