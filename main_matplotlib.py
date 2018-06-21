# http://www.kfish.org/boids/pseudocode.html
from swarm_boid import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


X_LIM = [ -300, 300 ]
Y_LIM = [ -300, 300 ]
swarm = Swarm( 20, X_LIM, Y_LIM )

fig = plt.figure()
ax = plt.axes( xlim=X_LIM, ylim=Y_LIM )
graph, = ax.plot([], [], 'o')


def update(i) :
    #swarm.simplePrintSwarm()
    swarm.updateSwarm()

    boid_pos_x = []
    boid_pos_y = []
    
    #data_vel = []

    for boid in swarm.list :
        boid_pos_x.append( boid.position[0] )
        boid_pos_y.append( boid.position[1] )
        #data_vel.append( boid.velocity )
        
    graph.set_data(boid_pos_x, boid_pos_y)

    return graph


ani = animation.FuncAnimation(fig, update, frames=30, interval=50)

plt.show()
