import random
import numpy as np
import pygame
import time as t
# http://www.kfish.org/boids/pseudocode.html

def main() :
    pygame.init()
    size = 800, 600
    screen = pygame.display.set_mode(size)

    X_LIM = 10
    Y_LIM = 10
    swarm = Swarm( 6, X_LIM, Y_LIM )

    for i in range(0,100) :
        drawSwarm( swarm )
        swarm.updateSwarm()
        t.sleep(0.5)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #for boid in boidlist
        #boidRect = pygame.Rect()
        #pygame.draw.rect()

    #keeping boids inside window
    #maxX = 800
    #minX = 0
    #maxY = 600
    #minY = 0
    #if boid.x > maxX
    #elif boid.x < minX
    #if boid.y > maxY
    #elif boid.y < minY

    pygame.display.flip()
    pygame.time.delay(10)

    return;

def drawSwarm( swarm ) :
    for boid in swarm.list :
        print( np.round(boid.position,0), end='' )
    print('')
    return;

class Swarm :
    def __init__(self, sizeOfFlock, xAxis, yAxis):
        self.sizeOfFlock = sizeOfFlock
        self.list = []
        for i in range( 0, sizeOfFlock ) :
            self.list.append( Boid(
                random.randint(0,xAxis),
                random.randint(0,yAxis),
                0,
                self
            ))

    def updateSwarm(self) :

        for boid in self.list :
            v1 = boid.rule1_separation() # for rule 1 - separation, avoiding collision
            v2 = boid.rule2_alignment()  # for rule 2 - alignment, matching velocity
            v3 = boid.rule3_cohesion()   # for rule 3 - cohesion, staying close to others

            #boid.velocity = np.array([ boid.velocity, v1, v2, v3 ]).sum(axis=0)
            boid.velocity = boid.velocity + v1 + v2 + v3
            #boid.position = np.add( boid.position + boid.velocity )
            boid.position = boid.position + boid.velocity

        return;


class Boid :
    def __init__(self, x, y, velocity, swarm):
        self.swarm = swarm
        self.x = x
        self.y = y
        # By using np.array() we can use simple x + y operators,
        # instead of np.add(x,y). Makes code more readable.
        self.velocity = np.array([ self.x, self.y ], dtype=np.float64)
        self.position = np.array([ self.x, self.y ], dtype=np.float64)

    def rule1_separation(self) :
        c = np.array([0,0], dtype=np.float64)

        for boid in self.swarm.list :
            if boid != self :
                if abs(boid.position - self.position).all() < 5 :
                    c = c - (boid.position - self.position)

        return c;
    
    def rule2_alignment(self) :
        perceivedVelocity = None

        for boid in self.swarm.list :
			print ( boid != self )
            if boid != self :
                if perceivedVelocity is not None :
                    perceivedVelocity = perceivedVelocity + boid.velocity
                else :
                    perceivedVelocity = boid.velocity

        perceivedVelocity = perceivedVelocity / (self.swarm.sizeOfFlock-1)
        perceivedVelocity = (perceivedVelocity - self.velocity) / 8;

        return perceivedVelocity;

    def rule3_cohesion(self) :
        perceivedCenter = None

        for boid in self.swarm.list :
            if boid != self :
                if perceivedCenter is not None :
                    perceivedCenter = perceivedCenter + boid.position
                else :
                    perceivedCenter = boid.position

        perceivedCenter = perceivedCenter / (self.swarm.sizeOfFlock-1)
        perceivedCenter = (perceivedCenter - self.position) / 50

        return perceivedCenter;

main()
