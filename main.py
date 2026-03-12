#Sophia Alexander
#Pachinko CGT 285 Assignment
#Last Edited: 03/12/26

#This is the Physics Code provided by the professor
import pygame
import pymunk

#this initializes pygame and pymunk
pygame.init()
screen = pygame.display.set_mode((800, 600))
space = pymunk.Space()
space.gravity= (0,0.01)

body = pymunk.body.Body(1,1)
ball = pymunk.Circle(body, 10, (0, 0))
body.position = (250, 100)
space.add(body, ball)

# This creates the ramp
line1Body = pymunk.Body(body_type=pymunk.Body.STATIC)
line1 = pymunk.Segment(line1Body, (200, 200), (300, 300), 2)
space.add(line1,line1Body)

#This is the game loop
done = False
while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
    screen.fill((0, 0, 0))
    space.step(1/10.0)
    pygame.draw.circle(screen, (255, 255, 255), body.position, 10)
    # this draws the ramp
    pygame.draw.line(screen,(255, 255, 255),line1.a,line1.b,2)
    pygame.display.update()

    #Now my objective is to add two more ramps. From here down is my own code

