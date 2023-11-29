import simpy
import math

BULLET_MASS = 0.0648  # Mass of the bullet in kilograms
MUZZLE_VELOCITY = 340  # Initial velocity of the bullet in m/s
GRAVITY = 9.81  # Acceleration due to gravity in m/s^2
AMMUNITION = 17

env = simpy.Environment()


def glock_shooting(env, ammunition):
    if ammunition > 0:
        print("Bullet shot")
        ammunition -= 1  # Decrement the ammunition count
        Bullet.fly(env, AMMUNITION)


class Bullet:
    @staticmethod
    def fly(env, ammunition):
        # Define the angle at which the bullet is shot (90 degrees in your case)
        ANGLE = 90

        # Calculate the bullet's impact velocity (in m/s)
        impact_velocity = MUZZLE_VELOCITY * math.sin(math.radians(ANGLE))

        # Determine if the bullet may cause harm based on impact velocity
        if 38.1 <= impact_velocity <= 70.1:
            print(
                "The bullet may penetrate the skin but is unlikely to cause significant harm.")
        else:
            print("The bullet is unlikely to penetrate the skin and cause harm.")


while AMMUNITION > 0:
    glock_shooting(env, AMMUNITION)

env.run()
