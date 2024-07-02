import numpy as np
import matplotlib.pyplot as plt

min = 0
max = 15
h = .001

# Define an Additional Function
def realDef(t):
    return 2 * np.exp(t) * np.sin(t)

def derivative(t):
    return 2 * np.exp(t) * np.cos(t) + 2 * np.exp(t) * np.sin(t)

eulerPoints = [0]
xPoints = [0]
itter = min
i = 0
while itter < max:
    newPoint = eulerPoints[i] + h * derivative(itter)
    eulerPoints.append(newPoint)
    xPoints.append(itter+h)
    itter += h
    i+=1


# Create x and y values
t = np.linspace(min, max, 100000)
y1 = realDef(t)
#y2 = eulerApprox(t)

print(realDef(0))

# Plot both functions
fig, ax = plt.subplots()
ax.plot(t, y1, label='y(t)=2exp(t)sin(t)')
ax.plot(xPoints, eulerPoints, label='Euler\'s method (step size = ' + str(h) + ')')
#ax.plot(t, y2, label='Euler\'s method')
ax.set_title('Plotting Functions in Matplotlib', size=14)
ax.set_xlim(min, max)
ax.set_ylim(-10, 10)
plt.legend()
plt.show()
