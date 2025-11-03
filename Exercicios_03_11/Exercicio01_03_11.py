# Crie uma matriz com 5 dimensões usando um vetor com valores 1, 2, 3, 4 e verifique
# se a ultima dimensão tem o valor 4?

import numpy as np

arr = np.array([1,2,3,4], ndmin = 5)
print(arr)
print('Shape do array: ', arr.shape)

