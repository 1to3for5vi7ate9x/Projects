import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint

# Lorenz attractor parameters
sigma = 10
rho = 28
beta = 8/3

# Rössler attractor parameters
a = 0.2
b = 0.2
c = 5.7

# Henon map parameters
henon_a = 1.4
henon_b = 0.3

# Time steps
dt = 0.01
t = np.arange(0, 100, dt)

# Lorenz attractor equations
def lorenz_equations(state, t):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

# Rössler attractor equations
def rossler_equations(state, t):
    x, y, z = state
    dx = -y - z
    dy = x + a * y
    dz = b + z * (x - c)
    return dx, dy, dz

# Henon map equation
def henon_map(x, y):
    return y + 1 - henon_a * x**2, henon_b * x

# Solve the Lorenz equations
initial_state_lorenz = (1, 1, 1)
states_lorenz = odeint(lorenz_equations, initial_state_lorenz, t)

# Solve the Rössler equations
initial_state_rossler = (0, 0, 0)
states_rossler = odeint(rossler_equations, initial_state_rossler, t)

# Generate Henon map data
n_iterations = len(t)
x_henon, y_henon = [0], [0]
for _ in range(n_iterations):
    x_i, y_i = henon_map(x_henon[-1], y_henon[-1])
    x_henon.append(x_i)
    y_henon.append(y_i)

# Plot the combined chaotic systems
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(states_lorenz[:, 0], states_lorenz[:, 1], states_lorenz[:, 2], label='Lorenz Attractor')
ax.plot(states_rossler[:, 0], states_rossler[:, 1], states_rossler[:, 2], label='Rössler Attractor')
ax.scatter(x_henon[:-1], y_henon[:-1], range(n_iterations), s=1, c=range(n_iterations), cmap='jet', label='Henon Map')
ax.legend()
plt.show()

