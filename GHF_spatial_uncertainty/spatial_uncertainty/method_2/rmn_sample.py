import numpy as np
import matplotlib.pyplot as plt

mean = (-100.389, -762.530)
cov = [[200, 0], [0, 200]]

sample = np.random.multivariate_normal(mean, cov, size=2000)
#print(sample)
np.savetxt('sample.txt', sample)

#plt.plot(sample[:, 0], sample[:, 1], '.', alpha=0.5)
#plt.axis('equal')
#plt.grid()
#plt.show()	
