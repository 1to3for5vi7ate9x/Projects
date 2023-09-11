import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
import glfw
from pyrr import Matrix44

# Initialize OpenGL window and callback functions
def init_window():
    if not glfw.init():
        return
    window = glfw.create_window(800, 600, "Chaotic Systems", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glEnable(GL_POINT_SMOOTH)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    projection = Matrix44.orthogonal_projection(left=-2.0, right=2.0, bottom=-2.0, top=2.0, near=-1.0, far=1.0)
    glLoadMatrixf(projection.astype('float32'))

    return window

# Render callback function
def render(window, systems):
    glClear(GL_COLOR_BUFFER_BIT)

    for system in systems:
        color = system['color']
        data = system['data']

        glColor3f(*color)
        glPushMatrix()
        glTranslatef(*system['position'])
        glBegin(GL_LINE_STRIP)

        for point in data:
            glVertex2f(point[0] / 30, point[1] / 30)

        glEnd()
        glPopMatrix()

    glfw.swap_buffers(window)

# Lorenz system update function
def lorenz_system_update(x, y, z, dt, sigma, rho, beta):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    x += dx * dt
    y += dy * dt
    z += dz * dt
    return x, y, z

# Generate data for Lorenz system
def generate_lorenz_data(dt, num_steps, sigma, rho, beta):
    x, y, z = 0.1, 0.0, 0.0
    data = []

    for _ in range(num_steps):
        data.append((x, y, z))
        x, y, z = lorenz_system_update(x, y, z, dt, sigma, rho, beta)

    return data

# Rössler system update function
def rossler_system_update(x, y, z, dt, a, b, c):
    dx = -y - z
    dy = x + a * y
    dz = b + z * (x - c)
    x += dx * dt
    y += dy * dt
    z += dz * dt
    return x, y, z

# Generate data for Rössler system
def generate_rossler_data(dt, num_steps, a, b, c):
    x, y, z = 0.0, 1.0, 1.0
    data = []

    for _ in range(num_steps):
        data.append((x, y, z))
        x, y, z = rossler_system_update(x, y, z, dt, a, b, c)

    return data

# Henon map update function
def henon_map_update(x, y, a, b):
    x_new = 1 - a * x**2 + y
    y_new = b * x
    return x_new, y_new

# Generate data for Henon map
def generate_henon_data(num_steps, a, b):
    x, y = 0.1, 0.1
    data = []

    for _ in range(num_steps):
        data.append((x, y))
        x, y = henon_map_update(x, y, a, b)

    return data

# Logistic map update function
def logistic_map_update(r, x):
    x_new = r * x * (1 - x)
    return x_new

# Generate data for Logistic map
def generate_logistic_data(r_min, r_max, num_steps):
    data = []

    r = r_min
    while r <= r_max:
        x = 0.1
        for _ in range(num_steps):
            data.append((r, x))
            x = logistic_map_update(r, x)
        r += 0.01

    return data

# Window size callback function
def window_size_callback(window, width, height):
    glViewport(0, 0, width, height)

# Main function
def main():
    window = init_window()
    if not window:
        return

    # Generate data for each system
    lorenz_data = generate_lorenz_data(dt=0.01, num_steps=10000, sigma=10.0, rho=28.0, beta=8.0 / 3.0)
    rossler_data = generate_rossler_data(dt=0.01, num_steps=10000, a=0.2, b=0.2, c=5.7)
    henon_data = generate_henon_data(num_steps=10000, a=1.4, b=0.3)
    logistic_data = generate_logistic_data(r_min=2.4, r_max=4.0, num_steps=10000)

    # Configure systems
    systems = [
        {'data': lorenz_data, 'color': (1.0, 0.0, 0.0), 'position': (0.0, 1.0, 0.0)},
        {'data': rossler_data, 'color': (0.0, 1.0, 0.0), 'position': (0.0, -1.0, 0.0)},
        {'data': henon_data, 'color': (0.0, 0.0, 1.0), 'position': (-1.5, 0.0, 0.0)},
        {'data': logistic_data, 'color': (1.0, 1.0, 0.0), 'position': (1.5, 0.0, 0.0)}
    ]

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render(window, systems)

    glfw.terminate()

if __name__ == "__main__":
    main()

