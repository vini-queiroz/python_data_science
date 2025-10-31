num = []

for i in range(10):
    n = int(input('Digite um número: '))
    num.append(n)

num.sort()

print(num)

print('Valor máximo:', max(num))
print('Valor mínimo:', min(num))
print('A média é de:', sum(num)/10)

