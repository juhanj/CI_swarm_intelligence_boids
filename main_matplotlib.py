# http://www.kfish.org/boids/pseudocode.html
import swarm_plot
import numpy as np
import matplotlib.pyplot as plt


X_LIM = [ -100, 100 ]
Y_LIM = [ -100, 100 ]
swarm = Swarm( 10, X_LIM, Y_LIM )

plt.ion()
f=plt.figure()
plt.axis([0,1000,0,1])

for i in range(0,1000) :
    swarm.simplePrintSwarm()
    swarm.updateSwarm()
    
    colors = (0,0,0)
    area = np.pi*3
    x = np.random.rand(20)
    y = np.random.rand(20)

    plt.clear()
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.draw()
    plt.pause(0.5)
        
