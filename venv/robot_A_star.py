import os
class Node:
    def __init__(self, parent = None, position = None):
        self.position = position
        self.parent = parent
        self.g = 0  # distance to start
        self.h = 0  # estimate distance to start
        self.f = 0


def GBF(grid ,start, end):
    start_node = Node(None, start)
    start_node.h=start_node.f=0
    end_node = Node(None, end)
    end_node.h = end_node.f = 0
    open_list = []
    close_list = []
    open_list.append(start_node)
    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        close_list.append(current_node)

        if current_node.position == end_node.position:
            path = []
            cost = []
            current = current_node
            while current is not None:
                char_location = get_char_path(current)
                path.append(char_location)
                cost.append(current.f)
                current = current.parent
            return path[::-1], cost
        children = []
        (row, col) = current_node.position
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        # get the next position if position out of board dont give add it to the next possible node
        for new_position in neighbors:
            counter = 0
            for i in close_list:
                if new_position == i.position:
                    counter += 1
            if counter > 0:
                continue
            if (((new_position[0]) or (new_position[1])) < 0):
                continue
            elif ((new_position[0] > len(grid[0]) - 1) or (new_position[1] > len(grid[0]) - 1)):
                continue
            elif new_position[1] < 0:
                continue
            elif grid[new_position[0]][new_position[1]] == 'W':
                continue

            else:
                node_position = (new_position[0], new_position[1])
                # node_position  = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                new_node = Node(current_node, node_position)
                # print(new_node.position)
                children.append(new_node)
        for child in children:
            for close_child in close_list:
                if child == close_child:
                    continue

            if grid[child.position[0]][child.position[1]] == 'R':
                child.h = (abs(child.position[0] - end_node.position[0])) + (abs(child.position[1] - end_node.position[1]))
                child.f = child.h

            # if grid[child.position[0]][child.position[1]] == 'R':
            #     child.h = 1
            #     child.f = child.h

            elif grid[child.position[0]][child.position[1]] == 'D':
                child.h = (abs(child.position[0] - end_node.position[0])) + (abs(child.position[1] - end_node.position[1]))
                child.f = child.h


            # this is if the rode value is as the HM descricbe
            # elif grid[child.position[0]][child.position[1]] == 'D':
            #     child.h = 4
            #     child.f = child.h
            #
            open_list.append(child)


#this function conver the node position to Letters
def get_char_path(current_node):
    (row, col) = current_node.position
    if current_node.parent == None:
       return '0'
    elif current_node.parent.position == (row-1,col):
        return 'D'
    elif current_node.parent.position == (row+1,col):
        return 'U'
    elif current_node.parent.position == (row,col-1):
        return 'R'
    elif current_node.parent.position == (row,col+1):
        return 'L'


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
                cost = []
                current = current_node
                while current is not None:
                    char_location = get_char_path(current)
                    path.append(char_location)
                    cost.append(current.g)
                    current = current.parent
                return path[::-1] ,cost

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
                 new_node=Node(current_node , node_position)
                 children.append(new_node)
            for child in children:
                for close_child in close_list:
                    if child == close_child:
                        continue

                if grid[child.position[0]][child.position[1]] == 'R':
                    child.g = 1
                    child.h = (abs(child.position[0] - end_node.position[0])) + (abs(child.position[1] - end_node.position[1]))
                    child.f = child.g + child.h

                elif grid[child.position[0]][child.position[1]] == 'D':
                    child.g = 4
                    child.h = (abs(child.position[0] - end_node.position[0]) ) + (abs(child.position[1] - end_node.position[1]))
                    child.f = child.g + child.h

                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue
                open_list.append(child)

#this function check if grid input is OK
def check_grid(grid, board_size):
    numOfBolck = 0
    for i in grid:
       numOfBolck+=len(i)
    if(numOfBolck != (board_size * board_size)):
        print("there are missing info to solve the problem please fix and try again ")
    return
#this is help function use in dev mode
# def get_all_index(grid):
#     all_position=[]
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             all_position.append((i,j))
#     return (all_position)

#this function found the start node
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
#this function found the goel node
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
    if countFailure == borad_size:
        print("there is no start position please check the input file")
    raise Exception("sorry there is problem with end point please chack")


def calc_cost(real_cost):
    cost = 0
    for x in real_cost:
        cost = x + cost
    return cost

def main():
    try:
       # filename = "C:\Liran_Collage\College\Fourth year\second simester\ML course\HM1\/files\input.txt"
       with open('input.txt','r') as input_file:
          lines = input_file.read().splitlines()
          algorithem_type=lines[0]
          borad_size = int(lines[1])
          grid=[]
          currentBoard = 0
          count = 0
          for line in lines[2:]:
           grid.append(list(line))
       check_grid(grid ,borad_size)
       start = foundStart(grid,borad_size)
       end = foundEnd(grid ,borad_size)
       print(grid)
       print("the start position : %s "  %(start,) )
       print("the end position : %s "  %(end,) )
       if algorithem_type == 'A*':
          path = astar(grid, start, end)
       elif algorithem_type == 'greedy best first':
          path = GBF(grid, start ,end)
       else:
          print("none")
       real_path = path[0]
       real_cost = path [1]
       print_cost = calc_cost(real_cost)
       print(real_path)
       print(print_cost)
       outF = open("output.txt",'w')
       for i in real_path:
          if i == '0':continue
          else:
            outF.write(i + '-')
       outF.write(str(print_cost))
       outF.close()
    except :
        outF = open("output.txt", 'w')
        outF.write("No path found ")
        outF.close()
        print("there is problem in the program ")




if __name__ == '__main__':
    main()
