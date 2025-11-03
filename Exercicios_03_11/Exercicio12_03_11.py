from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# sns.displot(random.normal(size = 10000), kind = 'kde')
sns.displot(random.normal(size = 10000))
plt.show()