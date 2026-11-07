import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, m, v):
        self.m = m  # Set instance attribute
        self.v = v  # Set instance attribute, note: vectorize 

    def getV(self):
        return self.v

    def getM(self):
        return self.m

class Collision:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def initial_momentum(self):
        # calculate initial momentum for 2 bodies of specified mass and velocity
        m1, v1 = self.p1.getM(), self.p1.getV()
        m2, v2 = self.p2.getM(), self.p2.getV()
        return (m1*v1) + (m2*v2)

    def calculate_v(self):
        # calculate combined velocity once two bodies collide
        m1, v1 = self.p1.getM(), self.p1.getV()
        m2, v2 = self.p2.getM(), self.p2.getV()
        return ((m1*v1) + (m2*v2))/(m1 + m2)

    def final_momentum(self):
        m1 = self.p1.getM()
        m2 = self.p2.getM()
        return (m1 + m2) * self.calculate_v()

if __name__ == "__main__":

    for i in range(10):
        def random_particle():
            return Particle(np.random.randint(1, 101), np.random.randint(-100, 101))

        a = random_particle()
        b = random_particle()
        c = Collision(a, b)

        print(f"{'Mass of a:':<35} {a.getM():>10}")
        print(f"{'Velocity of a:':<35} {a.getV():>10}")
        print(f"{'Mass of b:':<35} {b.getM():>10}")
        print(f"{'Velocity of b:':<35} {b.getV():>10}")
        print("")
        print(f"{'Initial momentum:':<35} {c.initial_momentum():>10}")
        print(f"{'Combined velocity after collision:':<35} {c.calculate_v():>10.2f}")
        print(f"{'Final momentum:':<35} {c.final_momentum():>10.1f}")
        print("")

        