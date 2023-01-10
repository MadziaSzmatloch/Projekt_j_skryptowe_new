import matplotlib.pyplot as plt
import numpy as np
import bryly

x = np.linspace(bryly.a, bryly.b, 500)
y = eval(bryly.func)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x, y, 'b') 
plt.ylabel("Wartości y")
plt.xlabel("Argumenty x")
plt.title("Wykres fukncji f(x) = " + bryly.func)
plt.grid(True)

plt.savefig("Plot.png", transparent=True) 