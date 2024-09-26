import numpy as np
import matplotlib.pyplot as plt
sims = 10000000
A = np.random.uniform(1, 5, sims)
B = np.random.uniform(2, 6, sims)
duration = A + B
# this is the size of the graph where the first paramter is the width and the second is the height
plt.figure(figsize=(3, 3))
plt.hist(duration, density=True)
plt.axvline(9, color='r')
plt.show()
