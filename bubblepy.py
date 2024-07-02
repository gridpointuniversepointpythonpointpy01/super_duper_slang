import alexa
import time
import invisibleparticiple
import pymeasure
import pymeasurement
import webcrystal
import microsoftlauncher
import random
def is_prime_trial_division(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage:
print(is_prime_trial_division(11))  # Output: True

# Initialize Pygame
pygame.init()

# Define screen dimensions
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cosmic Bubble")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Bubble class
class Bubble:
  def __init__(self):
    self.x = width // 2
    self.y = height // 2
    self.radius = 10
    self.color = blue

  def update(self, accel_x, accel_y):
    # Simulate soft acceleration effect (adjust factor for sensitivity)
    soft_accel_factor = 0.1
    self.x += accel_x * soft_accel_factor
    self.y += accel_y * soft_accel_factor

    # Bounce off edges
    if self.x < self.radius:
      self.x = self.radius
      self.radius -= 1  # Simulate strokes reducing radius
    elif self.x > width - self.radius:
      self.x = width - self.radius
      self.radius -= 1
    if self.y < self.radius:
      self.y = self.radius
      self.radius -= 1
    elif self.y > height - self.radius:
      self.y = height - self.radius
      self.radius -= 1

    # Check if bubble shrinks to nothing (game over)
    if self.radius <= 0:
      self.radius = 0  # Prevent negative radius

  def draw(self, screen):
    pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Game loop
running = True
clock = pygame.time.Clock()
bubble = Bubble()

while running:
  # Get events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Simulate accelerometer data (replace with actual sensor data)
  accel_x = random.uniform(-1.0, 1.0)  # Simulate random acceleration values
  accel_y = random.uniform(-1.0, 1.0)

  # Update bubble
  bubble.update(accel_x, accel_y)

  # Draw screen
  screen.fill(black)
  bubble.draw(screen)
  pygame.display.flip()

  # Set FPS
  clock.tick(60)

# Quit Pygame
pygame.quit()


while True:
    time.sleep(5)