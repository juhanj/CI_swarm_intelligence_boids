from swarm_boid import *
import numpy as np
import pygame


X_LIM = [-100, 100]
Y_LIM = [-100, 100]
swarm = Swarm(6, X_LIM, Y_LIM)

pygame.init()
size = 400, 400
screen = pygame.display.set_mode(size)

boidRenderGroup = pygame.sprite.RenderPlain()
for boid in self.swarm.list:
    render = BoidRender(boid)
    boidRenderGroup.add(render)

for i in range(0, 1000):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    swarm.simplePrintSwarm()
    swarm.updateSwarm()

    #
    # Graphics calculations here
    #

    pygame.display.flip()
    pygame.time.delay(10)
