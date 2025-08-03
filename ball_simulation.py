"""
Ball physics simulation for sim-physics-engine project.

This script simulates a ball moving in a one-dimensional vertical axis under gravity and
simple bounce physics using object-oriented design. It features a Ball class with position,
velocity, and acceleration properties, along with an update method to advance the simulation.

To run this simulation, ensure you have Python 3 installed then execute:

    python ball_simulation.py

You can adjust the parameters when creating the Ball object and running the simulation loop.
"""


class Ball:
    """A ball object with position, velocity, and acceleration for physics simulation."""
    
    def __init__(self, mass: float = 0.2, position: float = 1.0, velocity: float = 0.0):
        """Initialize a Ball with given mass, position, and velocity.
        
        Args:
            mass: Mass of the ball in kilograms.
            position: Initial vertical position in meters (positive is up from ground).
            velocity: Initial velocity in meters per second (positive is up).
        """
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = 0.0  # Will be set by forces during simulation
    
    def update(self, time_step: float, gravity: float = 9.81, restitution: float = 0.8) -> None:
        """Update the ball's state for one time step.
        
        Args:
            time_step: Time step for numerical integration in seconds.
            gravity: Magnitude of gravitational acceleration (m/s^2).
            restitution: Coefficient of restitution (bounciness) on impact with ground.
                        1.0 means perfectly elastic, 0.0 means no bounce.
        """
        # Set acceleration due to gravity (downward)
        self.acceleration = -gravity
        
        # Update velocity and position using Euler integration
        self.velocity += self.acceleration * time_step
        self.position += self.velocity * time_step
        
        # Handle bounce when the ball hits the ground
        if self.position <= 0:
            self.position = 0
            self.velocity = -self.velocity * restitution
            
            # Prevent tiny oscillations by stopping the ball if velocity is very small
            if abs(self.velocity) < 0.1:
                self.velocity = 0.0
    
    def get_state(self) -> tuple[float, float, float]:
        """Get the current state of the ball.
        
        Returns:
            Tuple of (position, velocity, acceleration) in meters, m/s, and m/s^2.
        """
        return (self.position, self.velocity, self.acceleration)


def simulate_ball(mass: float = 0.2,
                  initial_height: float = 1.0,
                  initial_velocity: float = 0.0,
                  gravity: float = 9.81,
                  restitution: float = 0.8,
                  time_step: float = 0.01,
                  total_time: float = 5.0) -> None:
    """Run a ball physics simulation using the Ball class.

    Args:
        mass: Mass of the ball in kilograms.
        initial_height: Starting height in meters.
        initial_velocity: Starting upward velocity in meters per second (positive is up).
        gravity: Magnitude of gravitational acceleration (m/s^2).
        restitution: Coefficient of restitution (bounciness) on impact with ground.
        time_step: Time step for numerical integration in seconds.
        total_time: Total time to simulate in seconds.
    """
    # Create a ball object
    ball = Ball(mass=mass, position=initial_height, velocity=initial_velocity)
    
    # Simulation loop
    t = 0.0
    while t < total_time:
        # Get current state
        position, velocity, acceleration = ball.get_state()
        
        # Print the current time and ball state
        print(f"t={t:.2f}s, position={position:.3f}m, velocity={velocity:.3f}m/s, acceleration={acceleration:.3f}m/s²")
        
        # Update ball for next time step
        ball.update(time_step, gravity, restitution)
        
        # Advance time
        t += time_step
        
        # Stop simulation if ball has come to rest
        if ball.position == 0 and ball.velocity == 0:
            print(f"Ball came to rest at t={t:.2f}s")
            break


if __name__ == "__main__":
    # Run the simulation with default parameters
    simulate_ball()
