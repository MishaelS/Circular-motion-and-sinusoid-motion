from math import cos, sin, pi
import pygame

# ----------------------------------------------------------

class Object:
	def __init__(self, surface, pos, size, speed, radius):
		self.image = pygame.Surface(size)
		self.rect = self.image.get_rect(center=pos)
		
		self.image.fill((250, 250, 250))

		self.switch = True
		self.surface = surface

		self.pos = pos
		self.__angle = 0
		self.__speed = speed
		self.__radius = radius

	def move(self, x=1, y=1, direction=1):
		self.__angle += round(1/self.__speed, 2)
		self.__radian = self.__angle * pi/180

		if self.__angle >= 360: self.__angle = 0
		
		if self.switch:
			if x:
				self.rect.centerx = (self.__radius*cos(self.__radian*direction)) + self.pos[0]
			if y:			
				self.rect.centery = (self.__radius*sin(self.__radian*direction)) + self.pos[1]

	def update(self):
		self.surface.blit(self.image, self.rect)
