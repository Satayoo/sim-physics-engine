"""
Ball physics simulation for sim-physics-engine project.

This script simulates a ball moving in a one-dimensional vertical axis under gravity and
simple bounce physics. It calculates the position and velocity of the ball over time and
prints them to the console.

To run this simulation, ensure you have Python 3 installed then execute:

    python ball_simulation.py

You can adjust the parameters in the `simulate_ball` function to change the mass,
initial height, initial velocity, gravity, coefficient of restitution (how bouncy the
ball is), the simulation time step, and the total simulation time.
"""


def simulate_ball(mass: float = 0.2,
                  initial_height: float = 1.0,
                  initial_velocity: float = 0.0,
                  gravity: float = 9.81,
                  restitution: float = 0.8,
                  time_step: float = 0.01,
                  total_time: float = 5.0) -> None:
    """Simulate a bouncing ball and print its position and velocity over time.

    Args:
        mass: Mass of the ball in kilograms (not used in this simple simulation but included
            for future extensions).
        initial_height: Starting height in meters.
        initial_velocity: Starting upward velocity in meters per second (positive is up).
        gravity: Magnitude of gravitational acceleration (m/s^2).
        restitution: Coefficient of restitution (bounciness) on impact with ground. 1.0 means
            perfectly elastic, 0.0 means no bounce.
        time_step: Time step for numerical integration in seconds.
        total_time: Total time to simulate in seconds.
    """
    position = initial_height
    velocity = initial_velocity
    t = 0.0

    while t < total_time:
        # Update velocity and position using simple Euler integration
        velocity -= gravity * time_step
        position += velocity * time_step

        # Handle bounce when the ball hits the ground (position <= 0)
        if position <= 0:
            position = 0
            velocity = -velocity * restitution

        # Print the current time, position and velocity
        print(f"t={t:.2f}s, position={position:.3f}m, velocity={velocity:.3f}m/s")

        # Advance time
        t += time_step


if __name__ == "__main__":
    # Run the simulation with default parameters
    simulate_ball()
