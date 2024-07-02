import usb
import bluetooth_clocks
import midi
import ptpm
import wifi
import time
import pdb
import prisma
import pybroom
import pandas
import launcherp
import copilot
import cython
import computer
import numpy
import pyglet
import MLgeometry
import logging
import random

class Bubble:
  def __init__(self, x, y, radius):
    self.x = x
    self.y = y
    self.radius = radius

  def move(self):
    # Simulate random movement in microgravity (no gravity)
    self.x += random.uniform(-1, 1)
    self.y += random.uniform(-1, 1)

  def is_in_vicinity(self, x, y, vicinity_radius):
    # Check if bubble is within a certain distance (vicinity)
    distance = ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5
    return distance <= vicinity_radius

# Create a bubble object
bubble = Bubble(50, 50, 10)

# Set the guided vicinity measurement parameters
target_x = 100  # Target position (X-axis)
vicinity_radius = 15  # Radius of the "vicinity" zone

# Loop to simulate bubble movement and measurement
while True:
  # Move the bubble
  bubble.move()

  # Check if bubble is in the vicinity of the target
  is_in_vicinity = bubble.is_in_vicinity(target_x, bubble.y, vicinity_radius)

  # Print information
  print(f"Bubble position: ({bubble.x}, {bubble.y})")
  print(f"Is bubble in vicinity? {is_in_vicinity}")

  # Optional: Add code to adjust target position based on bubble location

  # Pause for a short time
  import time
  time.sleep(0.1)
