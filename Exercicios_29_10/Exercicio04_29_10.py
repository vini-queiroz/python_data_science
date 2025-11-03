#x, y = input('Digite a base e a altura do seu quadrado (em metros) separados por espaço: ').split()

#x_int = int(x)
#y_int = int(y)

Base = int(input('Digite a base(em metros): '))
Altura = int(input('Digite a Altura(em metros): '))

Perimetro = ( Base + Altura ) * 2
Area = Base * Altura

print(f'O valor do perímetro do seu quadrado é de: {Perimetro}\nO valor da área do seu quadrado é de: {Area}M²')