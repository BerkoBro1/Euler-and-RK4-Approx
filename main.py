import numpy as np
import matplotlib.pyplot as plt

min = 0
max = 5
h = .1

# Define an Additional Function
def realDef(t):
    return 2 * np.exp(t) * np.sin(t)

def derivative(t):
    return 2 * np.exp(t) * np.cos(t) + 2 * np.exp(t) * np.sin(t)

eulerPoints = [0]
rk41Points = [0]
rk42Points = [2]
xPoints = [0]
itter = min
i = 0
while itter < max:
    newPoint = eulerPoints[i] + h * derivative(itter)
    eulerPoints.append(newPoint)

    z = rk41Points[i]
    w = rk42Points[i]

    k11 = w
    k12 = (2 * w) - (2 * z)

    k21 = w + (h * (k12 / 2))
    k22 = (2 * (w + (h * (k12 / 2)))) - (2 * (z + (h * (k11 / 2))))


    k31 = w + (h * (k22 / 2))
    k32 = (2 * (w + (h * (k22 / 2)))) - (2 * (z + (h * (k21 / 2))))

    k41 = w + (h * k32)
    k42 = (2 * (w + (h * k32))) - (2 * (z + (h * k31)))

    rk41Points.append(z + ((h/6) * (k11 + 2*k21 + 2*k31 + k41)))
    rk42Points.append(w + ((h/6) * (k12 + 2*k22 + 2*k32 + k42)))

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
ax.plot(xPoints, rk41Points, label='RK4 (step size = ' + str(h) + ')')
#ax.plot(t, y2, label='Euler\'s method')
ax.set_title('Plotting Functions in Matplotlib', size=14)
ax.set_xlim(min, max)
ax.set_ylim(-50, 50)
plt.legend()
plt.show()
