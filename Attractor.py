import math
import random

import pygame

G = 25

class Attractor:
	def __init__(self, x, y, mass):
		self.x = x
		self.y = y
		self.mass = mass
		self.destroyed = False
		self.vx = 0
		self.vy = 0

	def attract(self, other):
		dx = (self.x - other.x)
		dy = (self.y - other.y)
		dist = math.hypot(dx, dy)

		angle = math.atan2(dy, dx)

		# Newton's Law of Universal Gravitation
		force = G * (self.mass * other.mass) / dist**2


		if dist < self.mass*0.5:
			self.mass += other.mass
			other.destroyed = True


		"""
		- F: force
		- m: mass
		- a: acceleration

		F = m*a

		then,

		a = F/m

		Force x and y components:
		Fx = F * cos(angle)
		Fy = F * sin(angle)

		Acceleration for both components:

		a = Fx/m
		a = (F * cos(angle)) / m

		a = Fy/m
		a = (F * sin(angle)) / m
		"""

		
		self.x += force*math.cos(angle)/self.mass
		self.y += force*math.sin(angle)/self.mass
		
		other.x += force*math.cos(angle)/other.mass
		other.y += force*math.sin(angle)/other.mass

		

	def addVel(self, vx, vy):
		self.vx = vx
		self.vy = vy

	
	def update(self):
		# just adding a little velocity
		self.x += self.vx
		self.y += self.vy



	def render(self, screen):
		# rendering a little bit offseted
		pygame.draw.circle(screen, (255, 255, 255), (int(self.x - self.mass*0.5), int(self.y - self.mass*0.5)), self.mass)
