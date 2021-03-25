import maze
import generateMaze
import sys
import random

# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solveDfs(m):
    stack = []
    current_cell = 0
    visited_cells = 1

    while current_cell != m.total_cells -1:
        print('current cell = ',current_cell)
        unvisited_neighbors = m.cell_neighbors(current_cell)
        if len(unvisited_neighbors) >= 1:
            # choose random neighbor to be new cell
            new_cell_index = random.randint(0, len(unvisited_neighbors) - 1)
            new_cell, compass_index = unvisited_neighbors[new_cell_index]
            # knock down wall between it and current cell using visited_cell
            m.visit_cell(current_cell, new_cell, compass_index)
            # push current cell to stack
            stack.append(current_cell)
            # set current cell to new cell
            current_cell = new_cell
            # add 1 to visited cells
            visited_cells += 1
        else:
            m.backtrack(current_cell)
            current_cell = stack.pop()
            print("run")
        m.refresh_maze_view()
    m.state = 'idle'


# Solve maze using BFS algorithm, terminate with solution
def solveBfs(m):
    """
    create a queue
    set current cell to 0
    set in direction to 0b0000
    set visited cells to 0
    enqueue (current cell, in direction)
    while current cell not goal and queue not empty
        dequeue to current cell, in direction
        visit current cell with bfs_visit_cell
        add 1 to visited cells
        call refresh_maze_view to update visualization
        get unvisited neighbors of current cell using cell_neighbors, add to queue
    trace solution path and update cells with solution data using reconstruct_solution
    set state to 'idle'
    """
    queue = []
    cur_cell = 0
    in_direction = 0b0000
    visited_cells = 0
    queue.insert(0, (cur_cell, in_direction))
    while not cur_cell == len(m.maze_array) - 1 and len(queue) > 0:
        cur_cell, in_direction = queue.pop()
        m.bfs_visit_cell(cur_cell, in_direction)
        visited_cells += 1
        m.refresh_maze_view()
        neighbors = m.cell_neighbors(cur_cell)
        for neighbor in neighbors:
            queue.insert(0, neighbor)
    m.reconstruct_solution(cur_cell)
    m.state = "idle"


def main(solver='dfs'):
    currentMaze = maze.Maze('create')
    generateMaze.createDfs(currentMaze)
    if solver == 'dfs':
        solveDfs(currentMaze)
    elif solver == 'bfs':
        solveBfs(currentMaze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()