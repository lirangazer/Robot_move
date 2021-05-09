import os
from queue import PriorityQueue
class Node:
    def __init__(self, parent = None, position = None):
        self.position = position
        self.parent = parent
        self.g = 0 #distance to start
        self.h = 0
        self.f = 0
    # def __eq__(self, other):
    #     return other.position == self.position
def GFS(grid ,start, end):
    start_node = Node(None, start, end)
    start_node.h=0

def astar(grid, start, end ):
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        open_list = []
        close_list = []

        open_list.append(start_node)

        while len(open_list) > 0 :
            current_node = open_list[0]
            current_index = 0
            for index , item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            open_list.pop(current_index)
            close_list.append(current_node)

            if current_node.position == end_node.position:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    path.append(current.g)
                    current = current.parent
                return path[::-1]
            children = []
            #all_position = get_all_index(grid)
            (row,col) = current_node.position
            neighbors = [(row-1,col), (row+1,col), (row,col-1), (row,col+1)]
            #get the next position if position out of board dont give add it to the next possible node
            for new_position in neighbors:
                counter = 0
                for i in close_list:
                    if new_position == i.position:
                       counter+=1
                if counter > 0 :
                    continue
                if (((new_position[0]) or (new_position[1])) < 0):
                    continue
                elif ((new_position[0] > len(grid[0])-1) or (new_position[1] > len(grid[0])-1)):
                    continue
                elif new_position[1] < 0:
                    continue
                elif grid[new_position[0]][new_position[1]] == 'W':
                    continue

                else:
                 node_position  = (new_position[0], new_position[1])
                 #node_position  = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                 new_node=Node(current_node , node_position)
                 print(new_node.position)
                 children.append(new_node)
            for child in children:
                for close_child in close_list:
                    if child == close_child:
                        continue

                if grid[child.position[0]][child.position[1]] == 'R':
                    child.g = 1
                    child.h = (abs(child.position[0] - end_node.position[0])) + (abs(child.position[1] - end_node.position[1]))
                    child.f = child.g + child.h
                    print (child.position)
                    print (child.h)
                    print (child.f)
                elif grid[child.position[0]][child.position[1]] == 'D':
                    child.g = 4
                    child.h = (abs(child.position[0] - end_node.position[0]) ) + (abs(child.position[1] - end_node.position[1]))
                    child.f = child.g + child.h
                    print (child.position)
                    print (child.h)
                    print (child.f)
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue
                open_list.append(child)


def check_grid(grid, board_size):
    numOfBolck = 0
    for i in grid:
       numOfBolck+=len(i)
    if(numOfBolck != (board_size * board_size)):
        print("there are missing info to solve the problem please fix and try again ")
    return
def get_all_index(grid):
    all_position=[]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            all_position.append((i,j))
    return (all_position)
def foundStart(grid , board_size):

    #new and algant way
    # val = 'A'
    # start = [(index,row.index(val)) for index, row in enumerate(grid) if val in row]
    # print(start[0])
    #
    # return start[0]


#opation 1 old and good  way
    countFailure = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
         if grid[x][y] == 'A':

             return (x,y)
        else:
            countFailure+=1
    if countFailure == board_size:
        print("there is no start position please check the input file")
    return
def foundEnd(grid ,borad_size):
  # new and algant way
    # val = 'A'
    # start = [(index,row.index(val)) for index, row in enumerate(grid) if val in row]
    #
    # return start[0]

    countFailure = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 'B':
                return (x,y)
        else:
            countFailure += 1
    if countFailure == board_size:
        print("there is no start position please check the input file")
    return

def main():
    filename = "C:\Liran_Collage\College\Fourth year\second simester\ML course\HM1\/files\input.txt"
    with open(filename,'r') as input_file:
        lines = input_file.read().splitlines()
        algorithem_type=lines[0]
        borad_size = int(lines[1])
        grid=[]
        currentBoard = 0
        count = 0
        for line in lines[2:]:
         grid.append(list(line))
    print(grid)
    movement =['U','D','R','L']
    check_grid(grid ,borad_size)
    start = foundStart(grid,borad_size)
    end = foundEnd(grid ,borad_size)
    print("the start position : %s "  %(start,) )
    print("the end position : %s "  %(end,) )
    path = astar(grid, start, end)
    print(path)
    #runRobot(start,grid,cost,movement)

if __name__ == '__main__':
    main()
