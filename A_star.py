grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost,heuristic):
    # ----------------------------------------
    # modify the code below
    # ----------------------------------------
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1

    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    
    f_func = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    
    g_value = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]
    open_f = [[heuristic[x][y], x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    
    count = 0
    
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            g_value[x2][y2] = g2
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1

        #print expand
    for i in range(len(grid[0])): 
        for j in range(len(grid)): 
            f_func[j][i] = g_value[j][i] + heuristic[j][i]
    
    found = False
    
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1
    
    while found == False:
        
        open_f.sort()
        open_f.reverse()
        next = open_f.pop()
        x = next[1]
        y = next[2]
        expand[x][y] = count
        count += 1
        
        if(x == goal[0] and y == goal[1]):
            found = True
        else:    
        
            for i in range(len(delta)):
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                    if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                        open_f.append([f_func[x2][y2], x2, y2])
                        closed[x2][y2] = 1
        
    return expand
print search(grid,init,goal,cost,heuristic)