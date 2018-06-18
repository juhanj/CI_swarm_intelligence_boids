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

    pygame.display.flip()
    pygame.time.delay(10)

    return;

def drawSwarm( swarm ) :
    return;

class Swarm :
    def __init__(self, sizeOfFlock, xAxis, yAxis) :
        self.sizeOfFlock = sizeOfFlock # For calculating averages
        self.bounds = [xAxis, yAxis]
        self.list = []
        for i in range( 1, sizeOfFlock ) :
##            xAxis = random.randint( xAxis[0], xAxis[1] )
##            yAxis = random.randint( yAxis[0], yAxis[1] )
            # For initial velocity, random values between -1 and 1, for both x and y
            velocity = [ random.randint(-1,1), random.randint(-1,1) ]
            self.list.append(
                Boid( random.randint( xAxis[0], xAxis[1] ),
                      random.randint( yAxis[0], yAxis[1] ),
                      velocity, self
            ))

    def updateSwarm(self) :

        for boid in self.list :
            ## Three main rules
            v1 = boid.rule1_separation() # separation, avoiding collision
            v2 = boid.rule2_alignment()  # alignment, matching velocity
            v3 = boid.rule3_cohesion()   # cohesion, staying close to others
            ## Extra rules
            v4 = boid.rule4_bounds() # bounds, boid should stay inside visible boundaries

##            print( np.round(boid.velocity,1), end=' + ' )
##            print( np.round(v1,1), end=' + ' )
##            print( np.round(v2,1), end=' + ' )
##            print( np.round(v3,1), end=' + ' )
##            print( np.round(v4,1), end='' )
##            print('')
            
            boid.velocity = boid.velocity + v1 + v2 + v3 + v4
            # speed limit, no arbitarily fast speeds
            boid.limitVelocity()
            # Apply new position according to new velocity
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
        correction = np.array([0,0], dtype=np.float64)

        for boid in self.swarm.list :
            if boid != self :
                differenceMagnitude = np.linalg.norm( boid.position - self.position )

                if differenceMagnitude < 10 :
                    correction = correction - (boid.position - self.position)

        return correction;

    def rule2_alignment(self) :
        correction = np.array([0,0], dtype=np.float64)

        for boid in self.swarm.list :
            if boid != self :
                correction = correction + boid.velocity

        correction = correction / (self.swarm.sizeOfFlock-1)
        correction = (correction - self.velocity) / 10;

        return correction;

    def rule3_cohesion(self) :
        correction = np.array([0,0], dtype=np.float64)

        for boid in self.swarm.list :
            if boid != self :
                correction = correction + boid.position

        correction = correction / (self.swarm.sizeOfFlock-1)
        correction = (correction - self.position) / 50

        return correction;

    def rule4_bounds(self) :
        correction = np.array([0,0], dtype=np.float64)

        # Horizontal bounds
        if self.position[0] < self.swarm.bounds[0][0] : # xmin
            correction[0] = 10
        elif self.position[0] > self.swarm.bounds[0][1] : # xmax
            correction[0] = -10

        # Vertical bounds
        if self.position[1] < self.swarm.bounds[1][0] : # ymin
            correction[1] = 10
        elif self.position[1] > self.swarm.bounds[1][1] : # ymax
            correction[1] = -10
            
        return correction;
                
    def limitVelocity(self):
        vlim = 10.0
        
        velMagnitude = np.linalg.norm( self.velocity )
        
        # Limit speed if necessary
        if velMagnitude > vlim:
            self.velocity = (self.velocity / velMagnitude) * vlim
main()
