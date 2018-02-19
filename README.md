## A_star

It is based on the heuristic function. <br /> 
h(x, y) <= Distance to goal from x,y. <br /> 
g = Number of steps until reaching that position <br />
f = g + h(x,y) <br />


## Compute value

Creates a function compute_value which returns a grid of values. The value of a cell is the minimum number of moves required to get from the cell to the goal.

If a cell is a wall or it is impossible to reach the goal from a cell, assing that cell a value of 99.

## Optimum policy 

Returns a grid which shows the optimum policy for robot motion. There should be an optimum direction associated with each navigable cell which the goal can be reached. 

## Left turn policy

Compute and return the car's optimal path to the position specified in goal: the costs of each motion are as defined in cost. 
