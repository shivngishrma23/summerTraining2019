
import numpy as np
import matplotlib.pyplot as plt
    
incomes = np.random.normal(100.0, 20.0, 10000)
print (incomes)
plt.hist(incomes, 50)
plt.show()


print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))

##OUTLIER

incomes = np.append(incomes,[10000000000])


print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))