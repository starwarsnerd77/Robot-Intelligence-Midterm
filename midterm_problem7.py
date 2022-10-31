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
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def test():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print(path)
ox=[]
oy=[]
ox, oy = [], []
for i in range(-10, 60):
    ox.append(i)
    oy.append(-10.0)
for i in range(-10, 60):
    ox.append(60.0)
    oy.append(i)
for i in range(-10, 61):
    ox.append(i)
    oy.append(60.0)
for i in range(-10, 61):
    ox.append(-10.0)
    oy.append(i)
for i in range(-10, 40):
    ox.append(20.0)
    oy.append(i)
for i in range(0, 40):
    ox.append(40.0)
    oy.append(60.0 - i)
import time
out=[]
from AStar.a_star import AStarPlanner
import AStar.a_star as k
k.show_animation=False
t1=time.time()
for i in range(10):
    astar=AStarPlanner(ox,oy,1,1)
    steps=astar.planning(10,10,50,50)
t2=time.time()
out.append(("AStar",len(steps[0]),(t2-t1)/10))

from Dijkstra.dijkstra import Dijkstra
import Dijkstra.dijkstra as k
k.show_animation=False
t1=time.time()
for i in range(10):
    dijkstra=Dijkstra(ox,oy,1,1)
    steps=dijkstra.planning(10,10,50,50)
t2=time.time()
out.append(("Dijkstra",len(steps[0]),(t2-t1)/10))

from BidirectionalAStar.bidirectional_a_star import BidirectionalAStarPlanner
import BidirectionalAStar.bidirectional_a_star as k
k.show_animation=False
t1=time.time()
for i in range(10):
    bidirectional_star_planner=BidirectionalAStarPlanner(ox,oy,1,1)
    steps=bidirectional_star_planner.planning(10,10,50,50)
t2=time.time()
out.append(("BidirectionalAStar",len(steps[0]),(t2-t1)/10))

from BreadthFirstSearch.breadth_first_search import BreadthFirstSearchPlanner
import BreadthFirstSearch.breadth_first_search as k
k.show_animation=False
t1=time.time()
for i in range(10):
    breadth_first_search=BreadthFirstSearchPlanner(ox,oy,1,1)
    steps=breadth_first_search.planning(10,10,50,50)
t2=time.time()
print(steps)
out.append(("BreadthFirstSearch",len(steps[0]),(t2-t1)/10))

from RRTStar.rrt_star import RRTStar
length=0
from math import sqrt
t1=time.time()
for i in range(1):
    rrt_star = RRTStar(
            start=[10, 10],
            goal=[50, 50],
            rand_area=[-10, 60],
            obstacle_list=[[ox[i],oy[i],1] for i in range(len(ox))],
            expand_dis=5,
            robot_radius=0.8,
            max_iter=3000)
    steps=rrt_star.planning(animation=False)
    for step in range(1,len(steps)):
        length+=sqrt((steps[step-1][0]-steps[step][0])**2+(steps[step-1][1]-steps[step][1])**2)
t2=time.time()
out.append(("RRTStar",length/10,(t2-t1)/10))
print("\n".join([" ".join([str(j) for j in i]) for i in out]))