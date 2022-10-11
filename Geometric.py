from object import Object 
import pygame, sys

# ----------------------------------------------------------

width = 600
height = 600
fps = 60

# ----------------------------------------------------------

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# ----------------------------------------------------------

sun = Object(screen, (width/2, height/2), (16, 16), .8, 280)
earth = Object(screen, (width/2, height/2), (16, 16), .8, 280)
moon = Object(screen, (width/2, height/2), (16, 16), .8, 280)

# ----------------------------------------------------------

running = True
while running:
	screen.fill((25, 25, 25))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

	# earth.pos = sun.rect.center
	# moon.pos = earth.rect.center
	
	sun.move(0, 0, 1)
	earth.move(1, 1, 1)
	moon.move(0, 1, -1)

	sun.update()
	earth.update()
	moon.update()

	pygame.display.flip()
	clock.tick(fps)

# ----------------------------------------------------------

pygame.quit()
sys.exit()


