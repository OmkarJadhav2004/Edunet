import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
bounciness = 0.8  # Coefficient of restitution (0 < bounciness < 1)
initial_height = 10  # Initial height (meters)
time_step = 0.05  # Time step for the simulation (seconds)

# Ball properties
ball_radius = 0.1  # Radius of the ball (meters)
ball_color = 'red'

# Initialize variables
height = initial_height
velocity = 0
time = 0
positions = []

# Simulation loop
while height > 0.01:  # Stop when the ball is very close to the ground
    # Update position and velocity
    velocity += g * time_step  # Update velocity due to gravity
    height -= velocity * time_step  # Update height based on velocity

    # Check for bounce
    if height <= 0:
        height = -height * bounciness  # Reverse height and apply bounciness
        velocity = -velocity * bounciness  # Reverse velocity and apply bounciness

    positions.append(height)  # Store the height for plotting
    time += time_step

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, initial_height + 1)
ax.set_title('Elastic Ball Bounce Simulation')
ax.set_xlabel('Horizontal Position (m)')
ax.set_ylabel('Height (m)')

# Create a ball object
ball = plt.Circle((0, initial_height), ball_radius, color=ball_color)
ax.add_artist(ball)

# Animation update function
def update(frame):
    ball.set_center((0, positions[frame]))
    return ball,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(positions), interval=50, blit=True)

# Show the animation
plt.show()