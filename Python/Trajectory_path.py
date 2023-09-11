import math

# Get launch angle and velocity from user
angle = math.radians(float(input("Enter launch angle in degrees: ")))
velocity = float(input("Enter launch velocity in meters per second: "))

# Define launch position
x0, y0 = 0, 0

# Define constants
g = 9.81

# Define time interval and step size
time_interval = 0.1
step_size = 0.01
time_steps = int(time_interval / step_size)

# Create list of positions
positions = []
for i in range(time_steps):
    # Calculate time elapsed since launch
    t = i * step_size

    # Calculate horizontal and vertical positions
    x = x0 + velocity * math.cos(angle) * t
    y = y0 + velocity * math.sin(angle) * t - 0.5 * g * t**2

    # Add position to list
    positions.append((x, y))

# Print list of positions
print(positions)

