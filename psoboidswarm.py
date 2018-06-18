import random
import numpy as np
import pygame
import time as t
# http://www.kfish.org/boids/pseudocode.html

def main() :
    pygame.init()
    size = 800, 600
    screen = pygame.display.set_mode(size)

    X_LIM = [-100,100]
    Y_LIM = [-100,100]
    swarm = Swarm( 6, X_LIM, Y_LIM )

    for i in range(0,10) :
        swarm.simplePrintSwarm()
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
    return;

class Swarm :
    def __init__(self, sizeOfFlock, xAxis, yAxis):
        self.sizeOfFlock = sizeOfFlock # For calculating averages
        self.bounds = [xAxis, yAxis]
        self.list = []
        for i in range( 0, sizeOfFlock ) :
            self.list.append( Boid(
                random.randint(xAxis[0],xAxis[1]),
                random.randint(yAxis[0],yAxis[1]),
                0,
                self
            ))

    def updateSwarm(self) :

        for boid in self.list :
            ## Three main rules
            v1 = boid.rule1_separation() # separation, avoiding collision
            v2 = boid.rule2_alignment()  # alignment, matching velocity
            v3 = boid.rule3_cohesion()   # cohesion, staying close to others
            ## Extra rules
            v4 = boid.rule4_bounds() # bounds, boid should stay inside visible boundaries
            #v5 = boid.rule5_speedLimit() # speed limit, no arbitarily fast speeds

            boid.velocity = boid.velocity + v1 + v2 + v3 + v4
            boid.position = boid.position + boid.velocity

        return;

    def simplePrintSwarm(self) :
        for boid in self.list :
            print( np.round(boid.position,1), end='' )
        print('')
        return;
        


class Boid :
    def __init__(self, x, y, velocity, swarm):
        self.swarm = swarm
        self.x = x
        self.y = y
        # By using np.array() we can use simple x + y operators,
        # instead of np.add(x,y). Makes code more readable.
        self.position = np.array([ self.x, self.y ], dtype=np.float64)
        self.velocity = np.array([ 0, 0 ], dtype=np.float64)

    def rule1_separation(self) :
        c = np.array([0,0], dtype=np.float64)

        for boid in self.swarm.list :
            if boid != self :
                if abs(boid.position - self.position).all() < 10 :
                    c = c - (boid.position - self.position)

        return c;
    
    def rule2_alignment(self) :
        perceivedVelocity = None

        for boid in self.swarm.list :
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
        perceivedCenter = (perceivedCenter - self.position) / 100

        return perceivedCenter;

    def rule4_bounds(self) :
        v = np.array([0,0], dtype=np.float64)

        if self.position[0] < self.swarm.bounds[0][0] :
            v[0] = 10
        elif self.position[0] > self.swarm.bounds[0][1] :
            v[0] = -10
        
        if self.position[1] < self.swarm.bounds[1][0] :
            v[1] = 10
        elif self.position[1] > self.swarm.bounds[1][1] :
            v[1] = -10
            
        return 0;

main()
