from queue import PriorityQueue
class Node:
    def __init__(self, parent = None, position = None):
        self.position = position
        self.parent = parent
        self.g = 0 #distance to start
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return other.position == self.position


def astar(grid, start, end ,cost):
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
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                    return path[::-1]



def check_grid(grid, board_size):
    numOfBolck = 0
    for i in grid:
       numOfBolck+=len(i)
    if(numOfBolck != (board_size * board_size)):
        print("there are missing info to solve the problem please fix and try again ")
    return
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
    input_file = open('files\input.txt','r')
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
    cost={'road': 1 , 'dirt_road' : 4}
    check_grid(grid ,borad_size)
    start = foundStart(grid,borad_size)
    end = foundEnd(grid ,borad_size)
    print("the start position : %s "  %(start,) )
    print("the end position : %s "  %(end,) )
    astar(grid, start, end, cost)
    #runRobot(start,grid,cost,movement)

if __name__ == '__main__':
    main()
