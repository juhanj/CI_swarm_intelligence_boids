import random
import numpy as np
# http://www.kfish.org/boids/pseudocode.html

def main() :
    X_LIM = 10
    Y_LIM = 10
    swarm = Swarm( 10, X_LIM, Y_LIM )

    for i in range(0,100) :
        drawSwarm( swarm )
        swarm.updateSwarm()

    return;

def drawSwarm( swarm ) :
    temp = np.array([0,0], dtype=np.float64)
    for boid in swarm.list :
        temp = temp + boid.position
    print( temp / swarm.sizeOfFlock )
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
                if abs(boid.position - self.position) < 100 :
                    c = c - (boid.position - self.position)

        return c

    def rule2_alignment(self) :
        perceivedVelocity = np.array([0,0], dtype=np.float64)

        for boid in self.swarm.list :
            if boid != self :
                perceivedVelocity = perceivedVelocity + boid.velocity

        perceivedVelocity = perceivedVelocity / (self.swarm.sizeOfFlock-1)
        perceivedVelocity = (perceivedVelocity - self.velocity) / 8;

        return perceivedVelocity;

    def rule3_cohesion(self) :
        perceivedCenter = np.array([0,0], dtype=np.float64)

        for b in self.swarm.list :
            if b != self :
                perceivedCenter = perceivedCenter + b.position;

        perceivedCenter = perceivedCenter / (self.swarm.sizeOfFlock-1)
        perceivedCenter = (perceivedCenter - self.position) / 100

        return perceivedCenter;

main()
