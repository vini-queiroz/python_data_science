import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

arr = np.array([])

for x in range(5):
    temp = float(input(f'Digite a temperatura do dia {x+1}: '))
    arr = np.append(arr, temp)

print('As temperaturas registradas foram de: ')
print(arr,'\n')
print(f'A tempratura máxima foi de: {max(arr)}')
print(f'A média das temperaturas foram de: {np.mean(arr)}')

sns.displot(arr)
plt.show()