#coding:utf-8
import sys
import pygame
import math

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
RED=(255, 0, 0)
BLUE=(0, 0 , 255)

sun_position = (400, 400)
sun_radius = 40
earth_radius = 10
moon_radius = 5
mercury_radis = 8

earth_to_sun_dis = 150
moon_to_earth_dis = 30
mercury_to_sun_dis = 50\

sun_ball = pygame.image.load('img/sun.png')
sun_ball = pygame.transform.scale(sun_ball, (sun_radius*2, sun_radius*2))

earth_ball = pygame.image.load('img/earth.png')
earth_ball = pygame.transform.scale(earth_ball, (earth_radius*2, earth_radius*2))

def simulate():
	earth_angle = 0
	moon_angle = 0
	pygame.init()
	global screen
	screen = pygame.display.set_mode((800, 800))
	pygame.display.set_caption("Model of Solar System")
	#screen.fill(BLACK)
	clock = pygame.time.Clock()

	while True:
		clock.tick(40)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				
		screen.fill(BLACK)
		screen.blit(sun_ball, sun_position)
		
		earth_position = cal_position(sun_position, earth_to_sun_dis, earth_radius, BLUE, earth_angle)
		screen.blit(earth_ball, (earth_position[0] - earth_radius, earth_position[1] - earth_radius))
		earth_angle = (earth_angle + 1) % 360


		pygame.display.flip()
		#pygame.display.update()

def cal_position (mum_position, distance, radis, color, angle):
	planet_position = (mum_position[0] + int(distance * math.cos(math.radians(angle))), \
		              mum_position[1] + int(distance * math.sin(math.radians(angle))))
	return planet_position	

def draw_planet(mum_position, distance, radis, color, angle):
	planet_position = (mum_position[0] + int(distance * math.cos(math.radians(angle))), \
		              mum_position[1] + int(distance * math.sin(math.radians(angle))))
	pygame.draw.circle(screen, color, planet_position, radis)
	
	return planet_position


# 程序入口
if __name__=="__main__":
    print("programe loaded...")
    simulate()
