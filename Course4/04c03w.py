# The first line indicates the number of cities. Each city is a point in 
# the plane, and each subsequent line indicates the x- and y-coordinates 
# of a single city.

# The distance between two cities is defined as the Euclidean distance --- 
# that is, two cities at locations (x,y)(x,y) and (z,w)(z,w) have distance 
# sqrt{(x-z)^2 + (y-w)^2} between them.

# You should implement the nearest neighbor heuristic:

# Start the tour at the first city.
# Repeatedly visit the closest city that the tour hasn't visited yet. 
# In case of a tie, go to the closest city with the lowest index. 
# For example, if both the third and fifth cities have the same distance 
# from the first city (and are closer than any other city), then the tour 
# should begin by going from the first city to the third city.
# Once every city has been visited exactly once, return to the first city 
# to complete the tour.
# In the box below, enter the cost of the traveling salesman tour computed 
# by the nearest neighbor heuristic for this instance, rounded down 
# to the nearest integer.

# [Hint: when constructing the tour, you might find it simpler to work with 
# squared Euclidean distances (i.e., the formula above but without the 
# square root) than Euclidean distances. But don't forget to report the 
# length of the tour in terms of standard Euclidean distance.]

import numpy as np

node_x_y = np.loadtxt("nn.txt", skiprows=1)
v = node_x_y[:, 0]
x = node_x_y[:, 1]
y = node_x_y[:, 2]

G = {i: [x[i], y[i]] for i in range(33708)}

def count_dist_sq(c1, c2):
    return (G[c1][0]-G[c2][0])**2+(G[c1][1]-G[c2][1])**2

sum_tr = 0
path = [0]
Gc = G.copy()
Gc.pop(0)

while Gc:
    pl = 1000000000
    for node in Gc:
        d = count_dist_sq(path[-1], node)
        if d < pl:
            pl = d
            city = node
    sum_tr += np.sqrt(pl)
    path.append(city)
    Gc.pop(city)

tr = np.sqrt(count_dist_sq(0, path[-1]))
sum_tr += tr

answer_ex = int(sum_tr)

