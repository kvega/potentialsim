#!/usr/bin/python3

import pylab
import random

"""
Generates a text file of values representing the coordinates of n particles in a
potential.
"""

# Create the Particle Class
class Particle(object):
    """
    Representation of a simple, non-interacting, massive particle
    (assumes point-like, does not model charge).
    """
    def __init__(self, position, velocity, mass=1.0):
        """
        TODO: define attributes
        """
        self.mass = mass
        self.position = position
        self.velocity = velocity

    # Get the current position and velocity of the particle
    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity

    # Set the new position and velocity of the particle
    def set_position(self, position):
        self.position = position

    def set_velocity(self, velocity):
        self.velocity = velocity

# TODO: Implement the equations of motion for a given potential

# TODO: Create function to generate particles