# Heavily based on https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            flag=False
            for closed_child in closed_list:
                if child == closed_child:
                    flag=True
                    break
            if flag:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            flag=False
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    flag=True
                    break
            if flag:
                continue

            # Add the child to the open list
            open_list.append(child)


ox=[]
oy=[]
ox, oy = [], []
for i in range(60):
    ox.append(i)
    oy.append(0.0)
for i in range(60):
    ox.append(60.0)
    oy.append(i)
for i in range(61):
    ox.append(i)
    oy.append(60.0)
for i in range(61):
    ox.append(0.0)
    oy.append(i)
for i in range(40):
    ox.append(20.0)
    oy.append(i)
for i in range(40):
    ox.append(40.0)
    oy.append(60.0 - i)

maze = [[0 for j in range(7)] for i in range(7)]
for i in range(0,len(ox)):
    maze[int(oy[i])//10][int(ox[i])//10]=1
#print("\n".join([" ".join([str(i) for i in j]) for j in maze]))
start = (1, 1)
end = (5, 5)
steps = astar(maze, start, end)
cx=[i[1]*10 for i in steps]
cy=[i[0]*10 for i in steps]
print("Custom AStar",steps)

from HybridAStar.hybrid_a_star import hybrid_a_star_planning
import HybridAStar.hybrid_a_star as k
import numpy as np
k.show_animation=False
path=hybrid_a_star_planning([10.,10.,np.deg2rad(90.0)],[50.,50.,np.deg2rad(-90.0)],ox,oy,2,np.deg2rad(15.0))
x = path.x_list
y = path.y_list
yaw = path.yaw_list
print("HybridAStar",[(x[i],y[i]) for i in range(len(x))])
import matplotlib.pyplot as plt
plt.cla()
plt.plot(ox, oy, ".k")
plt.plot(x, y, label="Hybrid A* path")
plt.plot(cx, cy, label="Custom A* path")
plt.legend()
plt.grid(True)
plt.show()
input()