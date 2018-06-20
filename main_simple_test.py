from swarm_boid import *
import time as t


X_LIM = [-100, 100]
Y_LIM = [-100, 100]
swarm = Swarm(6, X_LIM, Y_LIM)

for i in range(0, 1000):
    
    swarm.simplePrintSwarm()
    swarm.updateSwarm()
    t.sleep(.25)
