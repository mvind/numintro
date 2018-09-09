import numpy as np
import matplotlib.pyplot as plt

# Plot the sine curve
x = np.arange(0, 3*np.pi,0.1) # creates [0.0, 0.1, 0.2, ...]
y_sin = np.sin(x) # creates [sin(0.0), sin(0.1), ...]
y_cos = np.cos(x)


# Plot using matplotlib
plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.legend(['Sinus','Cosinus'])
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sinus og Cosinus')
plt.show() # call to make graphics appear
