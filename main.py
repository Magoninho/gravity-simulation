from random import paretovariate, random
import pygame
import math
import random
from Attractor import Attractor

SCREEN = pygame.display.set_mode((800, 600))

main_attractor = Attractor(400, 300, 25)

attractors = []

for i in range(55):
	attractors.append(Attractor(random.randint(0, 770), random.randint(0, 550), random.randint(2, 10)))
	attractors[i].addVel(random.uniform(-0.10, 0.10), random.uniform(-0.10, 0.10))
	

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	for a in attractors:
		if not a.destroyed:
			a.update()
			main_attractor.attract(a)

	SCREEN.fill((0, 0, 0))

	main_attractor.render(SCREEN)

	for a in attractors:
		if not a.destroyed:
			a.render(SCREEN)

	pygame.display.update()
